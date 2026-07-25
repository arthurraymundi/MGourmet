from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.order.repository import OrderRepository
from app.order.service import OrderService
from app.product.repository import ProductRepository


def get_order_service(session: AsyncSession = Depends(get_session)) -> OrderService:
    return OrderService(OrderRepository(session), ProductRepository(session))
