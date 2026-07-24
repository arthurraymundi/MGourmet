from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.content.repository import ContentRepository
from app.content.service import ContentService
from app.core.database import get_session


def get_content_service(session: AsyncSession = Depends(get_session)) -> ContentService:
    return ContentService(ContentRepository(session))
