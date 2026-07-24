from typing import Annotated, Literal

from fastapi import APIRouter, Depends, Query

from app.core.schemas import ListResponse
from app.product.dependencies import get_product_service
from app.product.models import ProductCategory
from app.product.schemas import ProductResponse
from app.product.service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])
ServiceDep = Annotated[ProductService, Depends(get_product_service)]


@router.get("", response_model=ListResponse[ProductResponse], summary="Lista produtos")
async def list_products(
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
    category: ProductCategory | None = None,
    featured: bool | None = None,
    search: str | None = Query(default=None, min_length=1, max_length=160),
    sort: Literal["name", "price"] = "name",
    direction: Literal["asc", "desc"] = "asc",
) -> ListResponse[ProductResponse]:
    return await service.list(
        page=page,
        page_size=page_size,
        category=category,
        featured=featured,
        search=search,
        sort=sort,
        descending=direction == "desc",
    )


@router.get("/featured", response_model=ListResponse[ProductResponse], summary="Lista produtos em destaque")
async def list_featured_products(
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
) -> ListResponse[ProductResponse]:
    return await service.list(page=page, page_size=page_size, featured=True)


@router.get("/{product_id}", response_model=ProductResponse, summary="Obtém um produto")
async def get_product(product_id: str, service: ServiceDep) -> ProductResponse:
    return await service.get(product_id)
