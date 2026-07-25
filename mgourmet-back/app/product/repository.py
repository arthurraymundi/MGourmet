from collections.abc import Sequence

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.product.models import Product, ProductCategory


class ProductRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, product_id: str) -> Product | None:
        return await self._session.get(Product, product_id)

    async def list(
        self,
        *,
        category: ProductCategory | None,
        featured: bool | None,
        is_available: bool | None,
        search: str | None,
        sort: str,
        descending: bool,
        offset: int,
        limit: int,
    ) -> tuple[Sequence[Product], int]:
        filters = []
        if category is not None:
            filters.append(Product.category == category)
        if featured is not None:
            filters.append(Product.featured.is_(featured))
        if is_available is not None:
            filters.append(Product.is_available.is_(is_available))
        if search:
            filters.append(Product.name.ilike(f"%{search}%"))

        statement: Select[tuple[Product]] = select(Product).where(*filters)
        sort_column = {"name": Product.name, "price": Product.price}.get(sort, Product.name)
        statement = statement.order_by(sort_column.desc() if descending else sort_column.asc())
        statement = statement.offset(offset).limit(limit)
        count_statement = select(func.count()).select_from(Product).where(*filters)

        products = (await self._session.scalars(statement)).all()
        total = (await self._session.scalar(count_statement)) or 0
        return products, total

    async def create(self, product: Product) -> Product:
        self._session.add(product)
        await self._session.commit()
        await self._session.refresh(product)
        return product

    async def update(self, product: Product) -> Product:
        await self._session.commit()
        await self._session.refresh(product)
        return product

    async def delete(self, product: Product) -> None:
        await self._session.delete(product)
        await self._session.commit()
