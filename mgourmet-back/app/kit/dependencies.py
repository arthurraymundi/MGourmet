from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.kit.repository import KitRepository
from app.kit.service import KitService


def get_kit_service(session: AsyncSession = Depends(get_session)) -> KitService:
    return KitService(KitRepository(session))
