from math import ceil
from collections.abc import Sequence
from typing import TypeVar

from app.content.models import ContentSection
from app.content.repository import ContentRepository
from app.content.schemas import ContactInfoResponse, FaqResponse, TestimonialResponse
from app.core.exceptions import EntityNotFoundError
from app.core.schemas import APIModel, ListResponse, PaginationMeta

ResponseT = TypeVar("ResponseT", bound=APIModel)


class ContentService:
    def __init__(self, repository: ContentRepository) -> None:
        self._repository = repository

    async def get_testimonial(self, testimonial_id: str) -> TestimonialResponse:
        testimonial = await self._repository.get_testimonial(testimonial_id)
        if testimonial is None:
            raise EntityNotFoundError("Depoimento não encontrado.")
        return TestimonialResponse.model_validate(testimonial)

    async def list_testimonials(
        self, *, page: int, page_size: int, active_only: bool = True
    ) -> ListResponse[TestimonialResponse]:
        items, total = await self._repository.list_testimonials(
            active_only=active_only, offset=(page - 1) * page_size, limit=page_size
        )
        return self._list_response(items, total, page, page_size, TestimonialResponse)

    async def get_faq(self, faq_id: str) -> FaqResponse:
        faq = await self._repository.get_faq(faq_id)
        if faq is None:
            raise EntityNotFoundError("Pergunta frequente não encontrada.")
        return FaqResponse.model_validate(faq)

    async def list_faqs(
        self, *, page: int, page_size: int, active_only: bool = True
    ) -> ListResponse[FaqResponse]:
        items, total = await self._repository.list_faqs(
            active_only=active_only, offset=(page - 1) * page_size, limit=page_size
        )
        return self._list_response(items, total, page, page_size, FaqResponse)

    async def get_contact_info(self) -> ContactInfoResponse:
        contact_info = await self._repository.get_contact_info()
        if contact_info is None:
            raise EntityNotFoundError("Informações de contato não encontradas.")
        return ContactInfoResponse.model_validate(contact_info)

    async def list_content_items(
        self, *, section: ContentSection, page: int, page_size: int
    ) -> ListResponse[str]:
        items, total = await self._repository.list_content_items(
            section=section, offset=(page - 1) * page_size, limit=page_size
        )
        return ListResponse[str](
            items=[item.text for item in items],
            meta=PaginationMeta(
                page=page,
                page_size=page_size,
                total=total,
                total_pages=ceil(total / page_size) if total else 0,
            ),
        )

    @staticmethod
    def _list_response(
        items: Sequence[object], total: int, page: int, page_size: int, schema: type[ResponseT]
    ) -> ListResponse[ResponseT]:
        return ListResponse[ResponseT](
            items=[schema.model_validate(item) for item in items],
            meta=PaginationMeta(
                page=page,
                page_size=page_size,
                total=total,
                total_pages=ceil(total / page_size) if total else 0,
            ),
        )
