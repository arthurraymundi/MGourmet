from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.models import AdminUser


class AdminRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def count(self) -> int:
        return (await self._session.scalar(select(func.count()).select_from(AdminUser))) or 0

    async def get_by_email(self, email: str) -> AdminUser | None:
        return await self._session.scalar(select(AdminUser).where(AdminUser.email == email))

    async def get_by_id(self, admin_id: int) -> AdminUser | None:
        return await self._session.get(AdminUser, admin_id)

    async def create(self, admin: AdminUser) -> AdminUser:
        self._session.add(admin)
        await self._session.commit()
        await self._session.refresh(admin)
        return admin
