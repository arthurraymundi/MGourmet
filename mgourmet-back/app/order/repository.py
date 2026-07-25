from collections.abc import Sequence

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.order.models import Order, OrderItem


class OrderRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create(self, order: Order) -> Order:
        self._session.add(order)
        await self._session.commit()
        return await self.get_by_id(order.id) or order

    async def get_by_id(self, order_id: int) -> Order | None:
        statement: Select[tuple[Order]] = (
            select(Order).options(joinedload(Order.items)).where(Order.id == order_id)
        )
        return (await self._session.scalars(statement)).unique().one_or_none()

    async def list(self, *, offset: int, limit: int) -> tuple[Sequence[Order], int]:
        statement: Select[tuple[Order]] = (
            select(Order)
            .options(joinedload(Order.items))
            .order_by(Order.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        orders = (await self._session.scalars(statement)).unique().all()
        total = (await self._session.scalar(select(func.count()).select_from(Order))) or 0
        return orders, total

    async def update(self, order: Order) -> Order:
        await self._session.commit()
        return await self.get_by_id(order.id) or order
