from typing import Annotated

from fastapi import APIRouter, Depends, Query, status

from app.auth.dependencies import CurrentAdminDep
from app.core.schemas import ListResponse
from app.order.dependencies import get_order_service
from app.order.models import OrderStatus
from app.order.schemas import AdminOrderCreate, OrderCreate, OrderResponse, OrderStatusUpdate
from app.order.service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])
ServiceDep = Annotated[OrderService, Depends(get_order_service)]


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED, summary="Cria pedido")
async def create_order(payload: OrderCreate, service: ServiceDep) -> OrderResponse:
    return await service.create(payload)


@router.post("/admin", response_model=OrderResponse, status_code=status.HTTP_201_CREATED, summary="Cria pedido manual")
async def create_admin_order(
    payload: AdminOrderCreate, _: CurrentAdminDep, service: ServiceDep
) -> OrderResponse:
    return await service.create_admin(payload)


@router.get("", response_model=ListResponse[OrderResponse], summary="Lista pedidos")
async def list_orders(
    _: CurrentAdminDep,
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=50, ge=1, le=100),
    search: str | None = Query(default=None, min_length=1, max_length=160),
    status: OrderStatus | None = None,
) -> ListResponse[OrderResponse]:
    return await service.list(page=page, page_size=page_size, search=search, status=status)


@router.get("/{order_id}", response_model=OrderResponse, summary="Obtém pedido")
async def get_order(order_id: int, _: CurrentAdminDep, service: ServiceDep) -> OrderResponse:
    return await service.get(order_id)


@router.put("/{order_id}/status", response_model=OrderResponse, summary="Atualiza status do pedido")
async def update_order_status(
    order_id: int, payload: OrderStatusUpdate, _: CurrentAdminDep, service: ServiceDep
) -> OrderResponse:
    return await service.update_status(order_id, payload)


@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Exclui pedido")
async def delete_order(order_id: int, _: CurrentAdminDep, service: ServiceDep) -> None:
    await service.delete(order_id)
