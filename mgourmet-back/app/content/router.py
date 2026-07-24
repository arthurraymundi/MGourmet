from typing import Annotated

from fastapi import APIRouter, Depends, Query

from app.content.dependencies import get_content_service
from app.content.models import ContentSection
from app.content.schemas import ContactInfoResponse, FaqResponse, TestimonialResponse
from app.content.service import ContentService
from app.core.schemas import ListResponse

router = APIRouter(tags=["Content"])
ServiceDep = Annotated[ContentService, Depends(get_content_service)]


@router.get("/testimonials", response_model=ListResponse[TestimonialResponse], summary="Lista depoimentos")
async def list_testimonials(
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> ListResponse[TestimonialResponse]:
    return await service.list_testimonials(page=page, page_size=page_size)


@router.get("/testimonials/{testimonial_id}", response_model=TestimonialResponse, summary="Obtém depoimento")
async def get_testimonial(testimonial_id: str, service: ServiceDep) -> TestimonialResponse:
    return await service.get_testimonial(testimonial_id)


@router.get("/faqs", response_model=ListResponse[FaqResponse], summary="Lista perguntas frequentes")
async def list_faqs(
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> ListResponse[FaqResponse]:
    return await service.list_faqs(page=page, page_size=page_size)


@router.get("/faqs/{faq_id}", response_model=FaqResponse, summary="Obtém pergunta frequente")
async def get_faq(faq_id: str, service: ServiceDep) -> FaqResponse:
    return await service.get_faq(faq_id)


@router.get("/contact", response_model=ContactInfoResponse, summary="Obtém informações de contato")
async def get_contact_info(service: ServiceDep) -> ContactInfoResponse:
    return await service.get_contact_info()


@router.get(
    "/content/benefits", response_model=ListResponse[str], summary="Lista benefícios"
)
async def list_benefits(
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> ListResponse[str]:
    return await service.list_content_items(
        section=ContentSection.BENEFITS, page=page, page_size=page_size
    )


@router.get(
    "/content/how-it-works",
    response_model=ListResponse[str],
    summary="Lista etapas de funcionamento",
)
async def list_how_it_works(
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> ListResponse[str]:
    return await service.list_content_items(
        section=ContentSection.HOW_IT_WORKS, page=page, page_size=page_size
    )
