from decimal import Decimal
from math import ceil

from app.core.exceptions import EntityNotFoundError
from app.core.schemas import ListResponse, PaginationMeta
from app.order.models import Order, OrderItem, OrderSource, OrderStatus
from app.order.repository import OrderRepository
from app.order.schemas import AdminOrderCreate, OrderCreate, OrderResponse, OrderStatusUpdate
from app.product.repository import ProductRepository


class OrderService:
    def __init__(self, repository: OrderRepository, product_repository: ProductRepository) -> None:
        self._repository = repository
        self._product_repository = product_repository

    async def create(self, payload: OrderCreate) -> OrderResponse:
        return await self._create(payload, status=OrderStatus.RECEIVED, source=OrderSource.WEBSITE, payment_method=None)

    async def create_admin(self, payload: AdminOrderCreate) -> OrderResponse:
        return await self._create(
            payload,
            status=payload.status,
            source=payload.source,
            payment_method=payload.payment_method,
        )

    async def _create(
        self,
        payload: OrderCreate,
        *,
        status: OrderStatus,
        source: OrderSource,
        payment_method: str | None,
    ) -> OrderResponse:
        quantities: dict[str, int] = {}
        for item in payload.items:
            quantities[item.product_id] = quantities.get(item.product_id, 0) + item.quantity

        products = await self._product_repository.get_available_by_ids(list(quantities))
        products_by_id = {product.id: product for product in products}
        if len(products_by_id) != len(quantities):
            raise EntityNotFoundError("Um ou mais produtos não estão disponíveis.")

        items = [
            OrderItem(
                product_id=product_id,
                product_name=product.name,
                unit_price=product.price,
                quantity=quantity,
            )
            for product_id, quantity in quantities.items()
            for product in [products_by_id[product_id]]
        ]
        total = sum((item.unit_price * item.quantity for item in items), start=Decimal("0"))
        order = Order(
            customer_name=payload.customer_name.strip(),
            customer_phone=payload.customer_phone.strip(),
            delivery_method=payload.delivery_method,
            street=self._empty_to_none(payload.street),
            number=self._empty_to_none(payload.number),
            neighborhood=self._empty_to_none(payload.neighborhood),
            complement=self._empty_to_none(payload.complement),
            notes=self._empty_to_none(payload.notes),
            status=status,
            source=source,
            payment_method=self._empty_to_none(payment_method),
            total=total,
            items=items,
        )
        return OrderResponse.from_order(await self._repository.create(order))

    async def get(self, order_id: int) -> OrderResponse:
        order = await self._repository.get_by_id(order_id)
        if order is None:
            raise EntityNotFoundError("Pedido não encontrado.")
        return OrderResponse.from_order(order)

    async def list(
        self, *, page: int, page_size: int, search: str | None, status: OrderStatus | None
    ) -> ListResponse[OrderResponse]:
        orders, total = await self._repository.list(
            offset=(page - 1) * page_size, limit=page_size, search=search, status=status
        )
        return ListResponse[OrderResponse](
            items=[OrderResponse.from_order(order) for order in orders],
            meta=PaginationMeta(
                page=page,
                page_size=page_size,
                total=total,
                total_pages=ceil(total / page_size) if total else 0,
            ),
        )

    async def update_status(self, order_id: int, payload: OrderStatusUpdate) -> OrderResponse:
        order = await self._repository.get_by_id(order_id)
        if order is None:
            raise EntityNotFoundError("Pedido não encontrado.")
        order.status = payload.status
        return OrderResponse.from_order(await self._repository.update(order))

    async def delete(self, order_id: int) -> None:
        order = await self._repository.get_by_id(order_id)
        if order is None:
            raise EntityNotFoundError("Pedido não encontrado.")
        await self._repository.delete(order)

    @staticmethod
    def _empty_to_none(value: str | None) -> str | None:
        normalized = value.strip() if value else ""
        return normalized or None
