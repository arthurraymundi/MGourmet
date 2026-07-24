from decimal import Decimal
from typing import Annotated

from pydantic import Field, field_serializer, model_validator

from app.core.schemas import APIModel

KitId = Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", min_length=3, max_length=100)]


class KitData(APIModel):
    name: str = Field(min_length=2, max_length=120)
    meals: int = Field(gt=0)
    original_price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)
    discounted_price: Decimal = Field(ge=0, max_digits=10, decimal_places=2)

    @model_validator(mode="after")
    def validate_discount(self) -> "KitData":
        if self.discounted_price > self.original_price:
            raise ValueError("O preço promocional não pode ser maior que o preço original.")
        return self


class KitCreate(KitData):
    id: KitId


class KitUpdate(APIModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    meals: int | None = Field(default=None, gt=0)
    original_price: Decimal | None = Field(default=None, ge=0, max_digits=10, decimal_places=2)
    discounted_price: Decimal | None = Field(default=None, ge=0, max_digits=10, decimal_places=2)


class KitResponse(KitData):
    id: str

    @field_serializer("original_price", "discounted_price")
    def serialize_price(self, value: Decimal) -> float:
        return float(value)
