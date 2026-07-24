from collections.abc import Sequence

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.kit.models import Kit


class KitRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, kit_id: str) -> Kit | None:
        return await self._session.get(Kit, kit_id)

    async def list(
        self, *, sort: str, descending: bool, offset: int, limit: int
    ) -> tuple[Sequence[Kit], int]:
        sort_column = {"name": Kit.name, "meals": Kit.meals, "price": Kit.discounted_price}[sort]
        statement: Select[tuple[Kit]] = select(Kit).order_by(
            sort_column.desc() if descending else sort_column.asc()
        )
        kits = (await self._session.scalars(statement.offset(offset).limit(limit))).all()
        total = (await self._session.scalar(select(func.count()).select_from(Kit))) or 0
        return kits, total

    async def create(self, kit: Kit) -> Kit:
        self._session.add(kit)
        await self._session.commit()
        await self._session.refresh(kit)
        return kit

    async def update(self, kit: Kit) -> Kit:
        await self._session.commit()
        await self._session.refresh(kit)
        return kit
