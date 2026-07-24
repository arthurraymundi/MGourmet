from dataclasses import dataclass
from decimal import Decimal

import pytest

from app.product.models import ProductCategory
from app.product.service import ProductService


@dataclass
class FakeProduct:
    id: str = "frango-grelhado-fit"
    name: str = "Frango Grelhado com Arroz Integral"
    description: str = "Peito de frango grelhado, arroz integral e legumes."
    image_url: str = "https://example.com/frango.jpg"
    price: Decimal = Decimal("24.90")
    category: ProductCategory = ProductCategory.HIGH_PROTEIN
    ingredients: list[str] | None = None
    calories: int = 420
    protein: int = 38
    carbs: int = 39
    fat: int = 11
    featured: bool = True

    def __post_init__(self) -> None:
        if self.ingredients is None:
            self.ingredients = ["Frango", "Arroz integral"]


class FakeRepository:
    def __init__(self, products: list[FakeProduct]) -> None:
        self.products = products

    async def get_by_id(self, product_id: str) -> FakeProduct | None:
        return next((product for product in self.products if product.id == product_id), None)

    async def list(self, **_: object) -> tuple[list[FakeProduct], int]:
        return self.products, len(self.products)


@pytest.mark.asyncio
async def test_list_returns_frontend_compatible_product_shape() -> None:
    result = await ProductService(FakeRepository([FakeProduct()])).list(page=1, page_size=20)

    assert result.meta.total == 1
    assert result.items[0].model_dump(by_alias=True, mode="json") == {
        "id": "frango-grelhado-fit",
        "name": "Frango Grelhado com Arroz Integral",
        "description": "Peito de frango grelhado, arroz integral e legumes.",
        "imageUrl": "https://example.com/frango.jpg",
        "price": 24.9,
        "category": "Hiperproteica",
        "ingredients": ["Frango", "Arroz integral"],
        "nutrition": {"calories": 420, "protein": 38, "carbs": 39, "fat": 11},
        "featured": True,
    }
