from math import ceil
import re
import unicodedata

from app.core.exceptions import EntityNotFoundError
from app.core.schemas import ListResponse, PaginationMeta
from app.product.models import Product, ProductCategory
from app.product.repository import ProductRepository
from app.product.schemas import AdminProductCreate, ProductCreate, ProductResponse, ProductUpdate


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self._repository = repository

    async def get(self, product_id: str) -> ProductResponse:
        product = await self._repository.get_by_id(product_id)
        if product is None:
            raise EntityNotFoundError("Produto não encontrado.")
        return ProductResponse.from_product(product)

    async def list(
        self,
        *,
        page: int,
        page_size: int,
        category: ProductCategory | None = None,
        featured: bool | None = None,
        search: str | None = None,
        sort: str = "name",
        descending: bool = False,
    ) -> ListResponse[ProductResponse]:
        products, total = await self._repository.list(
            category=category,
            featured=featured,
            is_available=True,
            search=search,
            sort=sort,
            descending=descending,
            offset=(page - 1) * page_size,
            limit=page_size,
        )
        return ListResponse[ProductResponse](
            items=[ProductResponse.from_product(product) for product in products],
            meta=PaginationMeta(
                page=page,
                page_size=page_size,
                total=total,
                total_pages=ceil(total / page_size) if total else 0,
            ),
        )

    async def list_admin(self, *, page: int, page_size: int) -> ListResponse[ProductResponse]:
        products, total = await self._repository.list(
            category=None,
            featured=None,
            is_available=None,
            search=None,
            sort="name",
            descending=False,
            offset=(page - 1) * page_size,
            limit=page_size,
        )
        return ListResponse[ProductResponse](
            items=[ProductResponse.from_product(product) for product in products],
            meta=PaginationMeta(
                page=page,
                page_size=page_size,
                total=total,
                total_pages=ceil(total / page_size) if total else 0,
            ),
        )

    async def create(self, payload: ProductCreate) -> ProductResponse:
        existing = await self._repository.get_by_id(payload.id)
        if existing is not None:
            raise ValueError("Já existe um produto com este identificador.")
        product = Product(
            id=payload.id,
            name=payload.name,
            description=payload.description,
            image_url=str(payload.image_url),
            price=payload.price,
            category=payload.category,
            ingredients=payload.ingredients,
            calories=payload.nutrition.calories,
            protein=payload.nutrition.protein,
            carbs=payload.nutrition.carbs,
            fat=payload.nutrition.fat,
            featured=payload.featured,
            is_available=True,
        )
        return ProductResponse.from_product(await self._repository.create(product))

    async def create_admin(self, payload: AdminProductCreate) -> ProductResponse:
        product = Product(
            id=await self._next_product_id(payload.name),
            name=payload.name,
            description=payload.description,
            image_url=str(payload.image_url),
            price=payload.price,
            category=payload.category,
            ingredients=payload.ingredients,
            calories=payload.nutrition.calories,
            protein=payload.nutrition.protein,
            carbs=payload.nutrition.carbs,
            fat=payload.nutrition.fat,
            featured=payload.featured,
            is_available=payload.is_available,
        )
        return ProductResponse.from_product(await self._repository.create(product))

    async def update(self, product_id: str, payload: ProductUpdate) -> ProductResponse:
        product = await self._repository.get_by_id(product_id)
        if product is None:
            raise EntityNotFoundError("Produto não encontrado.")
        changes = payload.model_dump(exclude_unset=True)
        nutrition = changes.pop("nutrition", None)
        if nutrition is not None:
            for field, value in nutrition.items():
                setattr(product, field, value)
        for field, value in changes.items():
            setattr(product, field, str(value) if field == "image_url" else value)
        return ProductResponse.from_product(await self._repository.update(product))

    async def delete(self, product_id: str) -> None:
        product = await self._repository.get_by_id(product_id)
        if product is None:
            raise EntityNotFoundError("Produto não encontrado.")
        await self._repository.delete(product)

    async def _next_product_id(self, name: str) -> str:
        normalized = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode("ascii")
        base_id = re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")[:90] or "produto"
        candidate = base_id
        suffix = 2
        while await self._repository.get_by_id(candidate) is not None:
            candidate = f"{base_id[: 100 - len(str(suffix)) - 1]}-{suffix}"
            suffix += 1
        return candidate
