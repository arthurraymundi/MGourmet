from decimal import Decimal

from sqlalchemy import CheckConstraint, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import Base, TimestampMixin


class Kit(TimestampMixin, Base):
    __tablename__ = "kits"
    __table_args__ = (
        CheckConstraint("meals > 0", name="kit_meals_positive"),
        CheckConstraint("original_price >= 0", name="kit_original_price_non_negative"),
        CheckConstraint("discounted_price >= 0", name="kit_discounted_price_non_negative"),
        CheckConstraint(
            "discounted_price <= original_price", name="kit_discounted_price_not_greater_than_original"
        ),
    )

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    meals: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    original_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    discounted_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
