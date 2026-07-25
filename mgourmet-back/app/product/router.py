from typing import Annotated, Literal

from fastapi import APIRouter, Depends, Query, status

from app.auth.dependencies import CurrentAdminDep
from app.core.schemas import ListResponse
from app.product.dependencies import get_product_service
from app.product.models import ProductCategory
from app.product.schemas import AdminProductCreate, ProductResponse, ProductUpdate
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


@router.get("/admin", response_model=ListResponse[ProductResponse], summary="Lista produtos para administração")
async def list_admin_products(
    _: CurrentAdminDep,
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=100, ge=1, le=100),
) -> ListResponse[ProductResponse]:
    return await service.list_admin(page=page, page_size=page_size)


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED, summary="Cria produto")
async def create_product(
    payload: AdminProductCreate, _: CurrentAdminDep, service: ServiceDep
) -> ProductResponse:
    return await service.create_admin(payload)


@router.put("/{product_id}", response_model=ProductResponse, summary="Atualiza produto")
async def update_product(
    product_id: str, payload: ProductUpdate, _: CurrentAdminDep, service: ServiceDep
) -> ProductResponse:
    return await service.update(product_id, payload)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Exclui produto")
async def delete_product(product_id: str, _: CurrentAdminDep, service: ServiceDep) -> None:
    await service.delete(product_id)


@router.get("/{product_id}", response_model=ProductResponse, summary="Obtém um produto")
async def get_product(product_id: str, service: ServiceDep) -> ProductResponse:
    return await service.get(product_id)
