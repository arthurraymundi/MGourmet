from typing import Annotated

from fastapi import APIRouter, Depends, Query, status

from app.auth.dependencies import CurrentAdminDep
from app.core.schemas import ListResponse
from app.order.dependencies import get_order_service
from app.order.schemas import OrderCreate, OrderResponse, OrderStatusUpdate
from app.order.service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])
ServiceDep = Annotated[OrderService, Depends(get_order_service)]


@router.post("", response_model=OrderResponse, status_code=status.HTTP_201_CREATED, summary="Cria pedido")
async def create_order(payload: OrderCreate, service: ServiceDep) -> OrderResponse:
    return await service.create(payload)


@router.get("", response_model=ListResponse[OrderResponse], summary="Lista pedidos")
async def list_orders(
    _: CurrentAdminDep,
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=50, ge=1, le=100),
) -> ListResponse[OrderResponse]:
    return await service.list(page=page, page_size=page_size)


@router.get("/{order_id}", response_model=OrderResponse, summary="Obtém pedido")
async def get_order(order_id: int, _: CurrentAdminDep, service: ServiceDep) -> OrderResponse:
    return await service.get(order_id)


@router.put("/{order_id}/status", response_model=OrderResponse, summary="Atualiza status do pedido")
async def update_order_status(
    order_id: int, payload: OrderStatusUpdate, _: CurrentAdminDep, service: ServiceDep
) -> OrderResponse:
    return await service.update_status(order_id, payload)
