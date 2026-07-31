from dataclasses import dataclass
from datetime import UTC, datetime
from decimal import Decimal

import pytest

from app.core.exceptions import EntityNotFoundError
from app.order.models import DeliveryMethod, Order, OrderSource, OrderStatus
from app.order.schemas import AdminOrderCreate, OrderCreate, OrderItemCreate
from app.order.service import OrderService


@dataclass
class FakeProduct:
    id: str
    name: str
    price: Decimal


class FakeProductRepository:
    def __init__(self, products: list[FakeProduct]) -> None:
        self.products = products

    async def get_available_by_ids(self, product_ids: list[str]) -> list[FakeProduct]:
        return [product for product in self.products if product.id in product_ids]


class FakeOrderRepository:
    async def create(self, order: Order) -> Order:
        order.id = 1
        order.created_at = datetime.now(UTC)
        for index, item in enumerate(order.items, start=1):
            item.id = index
        return order


def create_payload(product_id: str = "frango-grelhado-fit") -> OrderCreate:
    return OrderCreate(
        customer_name="Ana Silva",
        customer_phone="11999999999",
        delivery_method=DeliveryMethod.PICKUP,
        items=[OrderItemCreate(product_id=product_id, quantity=2)],
    )


@pytest.mark.asyncio
async def test_order_uses_server_product_snapshot_and_price() -> None:
    service = OrderService(
        FakeOrderRepository(),
        FakeProductRepository([FakeProduct("frango-grelhado-fit", "Frango Fit", Decimal("28.50"))]),
    )

    order = await service.create(create_payload())

    assert order.total == Decimal("57.00")
    assert order.items[0].product_name == "Frango Fit"
    assert order.items[0].unit_price == Decimal("28.50")


@pytest.mark.asyncio
async def test_order_rejects_unavailable_or_missing_product() -> None:
    service = OrderService(FakeOrderRepository(), FakeProductRepository([]))

    with pytest.raises(EntityNotFoundError, match="não estão disponíveis"):
        await service.create(create_payload())


@pytest.mark.asyncio
async def test_manual_order_uses_the_same_product_price_calculation() -> None:
    service = OrderService(
        FakeOrderRepository(),
        FakeProductRepository([FakeProduct("frango-grelhado-fit", "Frango Fit", Decimal("28.50"))]),
    )
    payload = AdminOrderCreate(
        **create_payload().model_dump(),
        source=OrderSource.WHATSAPP,
        payment_method="Pix",
        status=OrderStatus.PREPARING,
    )

    order = await service.create_admin(payload)

    assert order.total == Decimal("57.00")
    assert order.source == OrderSource.WHATSAPP
    assert order.payment_method == "Pix"
    assert order.status == OrderStatus.PREPARING
