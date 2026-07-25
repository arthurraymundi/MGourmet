from decimal import Decimal
from enum import StrEnum

from sqlalchemy import Boolean, CheckConstraint, Enum, Integer, Numeric, String, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import Base, TimestampMixin


class ProductCategory(StrEnum):
    HIGH_PROTEIN = "Hiperproteica"
    LOW_CARB = "Low Carb"
    WEIGHT_LOSS = "Emagrecimento"
    MUSCLE_GAIN = "Ganho de Massa"
    VEGETARIAN = "Vegetariana"
    PRATO_FITNESS = "Prato Fitness"
    MINI_PRATO_FITNESS = "Mini Prato Fitness"
    PRATO_KIDS = "Prato Kids"
    SOPA = "Sopa"
    PROTEINA = "Proteína"
    PREMIUM = "Premium"


class Product(TimestampMixin, Base):
    __tablename__ = "products"
    __table_args__ = (
        CheckConstraint("price >= 0", name="product_price_non_negative"),
        CheckConstraint("calories >= 0", name="product_calories_non_negative"),
        CheckConstraint("protein >= 0", name="product_protein_non_negative"),
        CheckConstraint("carbs >= 0", name="product_carbs_non_negative"),
        CheckConstraint("fat >= 0", name="product_fat_non_negative"),
    )

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    name: Mapped[str] = mapped_column(String(160), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    image_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    category: Mapped[ProductCategory] = mapped_column(
        Enum(
            ProductCategory,
            name="product_category",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
        index=True,
    )
    ingredients: Mapped[list[str]] = mapped_column(ARRAY(String(120)), nullable=False)
    calories: Mapped[int] = mapped_column(Integer, nullable=False)
    protein: Mapped[int] = mapped_column(Integer, nullable=False)
    carbs: Mapped[int] = mapped_column(Integer, nullable=False)
    fat: Mapped[int] = mapped_column(Integer, nullable=False)
    featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
