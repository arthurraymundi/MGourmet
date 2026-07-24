from decimal import Decimal
from typing import Annotated

from pydantic import Field, HttpUrl, field_serializer

from app.core.schemas import APIModel
from app.product.models import ProductCategory

ProductId = Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", min_length=3, max_length=100)]


class NutritionInfo(APIModel):
    calories: int = Field(ge=0)
    protein: int = Field(ge=0)
    carbs: int = Field(ge=0)
    fat: int = Field(ge=0)


class ProductCreate(APIModel):
    id: ProductId
    name: str = Field(min_length=2, max_length=160)
    description: str = Field(min_length=2, max_length=5000)
    image_url: HttpUrl
    price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    category: ProductCategory
    ingredients: list[str] = Field(min_length=1, max_length=50)
    nutrition: NutritionInfo
    featured: bool = False


class ProductUpdate(APIModel):
    name: str | None = Field(default=None, min_length=2, max_length=160)
    description: str | None = Field(default=None, min_length=2, max_length=5000)
    image_url: HttpUrl | None = None
    price: Decimal | None = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    category: ProductCategory | None = None
    ingredients: list[str] | None = Field(default=None, min_length=1, max_length=50)
    nutrition: NutritionInfo | None = None
    featured: bool | None = None


class ProductResponse(APIModel):
    id: str
    name: str
    description: str
    image_url: str
    price: Decimal
    category: ProductCategory
    ingredients: list[str]
    nutrition: NutritionInfo
    featured: bool

    @field_serializer("price")
    def serialize_price(self, value: Decimal) -> float:
        return float(value)

    @classmethod
    def from_product(cls, product: object) -> "ProductResponse":
        return cls(
            id=getattr(product, "id"),
            name=getattr(product, "name"),
            description=getattr(product, "description"),
            image_url=getattr(product, "image_url"),
            price=getattr(product, "price"),
            category=getattr(product, "category"),
            ingredients=getattr(product, "ingredients"),
            nutrition=NutritionInfo(
                calories=getattr(product, "calories"),
                protein=getattr(product, "protein"),
                carbs=getattr(product, "carbs"),
                fat=getattr(product, "fat"),
            ),
            featured=getattr(product, "featured"),
        )
