from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.product.repository import ProductRepository
from app.product.service import ProductService


def get_product_service(session: AsyncSession = Depends(get_session)) -> ProductService:
    return ProductService(ProductRepository(session))
