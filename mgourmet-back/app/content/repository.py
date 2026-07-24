from collections.abc import Sequence
from typing import TypeVar

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.content.models import ContactInfo, ContentItem, ContentSection, Faq, Testimonial

ContentModel = TypeVar("ContentModel", Faq, Testimonial)


class ContentRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_testimonial(self, testimonial_id: str) -> Testimonial | None:
        return await self._session.get(Testimonial, testimonial_id)

    async def list_testimonials(
        self, *, active_only: bool, offset: int, limit: int
    ) -> tuple[Sequence[Testimonial], int]:
        return await self._list(Testimonial, active_only=active_only, offset=offset, limit=limit)

    async def get_faq(self, faq_id: str) -> Faq | None:
        return await self._session.get(Faq, faq_id)

    async def list_faqs(
        self, *, active_only: bool, offset: int, limit: int
    ) -> tuple[Sequence[Faq], int]:
        return await self._list(Faq, active_only=active_only, offset=offset, limit=limit)

    async def get_contact_info(self) -> ContactInfo | None:
        return await self._session.get(ContactInfo, "default")

    async def list_content_items(
        self, *, section: ContentSection, offset: int, limit: int
    ) -> tuple[Sequence[ContentItem], int]:
        filters = [ContentItem.section == section, ContentItem.active.is_(True)]
        statement = (
            select(ContentItem)
            .where(*filters)
            .order_by(ContentItem.position)
            .offset(offset)
            .limit(limit)
        )
        items = (await self._session.scalars(statement)).all()
        total = (
            await self._session.scalar(select(func.count()).select_from(ContentItem).where(*filters))
        ) or 0
        return items, total

    async def _list(
        self,
        model: type[ContentModel],
        *,
        active_only: bool,
        offset: int,
        limit: int,
    ) -> tuple[Sequence[ContentModel], int]:
        filters = [model.active.is_(True)] if active_only else []
        statement: Select[tuple[ContentModel]] = select(model).where(*filters).order_by(model.created_at)
        items = (await self._session.scalars(statement.offset(offset).limit(limit))).all()
        total = (await self._session.scalar(select(func.count()).select_from(model).where(*filters))) or 0
        return items, total
