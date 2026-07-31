from decimal import Decimal
from enum import StrEnum

from sqlalchemy import CheckConstraint, Enum, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.models import Base, TimestampMixin


class DeliveryMethod(StrEnum):
    PICKUP = "pickup"
    DELIVERY = "delivery"


class OrderStatus(StrEnum):
    RECEIVED = "Recebido"
    PREPARING = "Preparando"
    OUT_FOR_DELIVERY = "Saiu para entrega"
    COMPLETED = "Finalizado"
    CANCELED = "Cancelado"


class OrderSource(StrEnum):
    WEBSITE = "site"
    PHONE = "telefone"
    WHATSAPP = "whatsapp"
    IN_PERSON = "presencial"


class Order(TimestampMixin, Base):
    __tablename__ = "orders"
    __table_args__ = (CheckConstraint("total >= 0", name="order_total_non_negative"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str] = mapped_column(String(160), nullable=False)
    customer_phone: Mapped[str] = mapped_column(String(50), nullable=False)
    delivery_method: Mapped[DeliveryMethod] = mapped_column(
        Enum(
            DeliveryMethod,
            name="delivery_method",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
    )
    street: Mapped[str | None] = mapped_column(String(255))
    number: Mapped[str | None] = mapped_column(String(40))
    neighborhood: Mapped[str | None] = mapped_column(String(160))
    complement: Mapped[str | None] = mapped_column(String(255))
    notes: Mapped[str | None] = mapped_column(Text)
    status: Mapped[OrderStatus] = mapped_column(
        Enum(
            OrderStatus,
            name="order_status",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        default=OrderStatus.RECEIVED,
        nullable=False,
        index=True,
    )
    source: Mapped[OrderSource] = mapped_column(
        Enum(
            OrderSource,
            name="order_source",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        default=OrderSource.WEBSITE,
        nullable=False,
    )
    payment_method: Mapped[str | None] = mapped_column(String(100))
    total: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    items: Mapped[list["OrderItem"]] = relationship(
        back_populates="order", cascade="all, delete-orphan", passive_deletes=True
    )


class OrderItem(Base):
    __tablename__ = "order_items"
    __table_args__ = (
        CheckConstraint("quantity > 0", name="order_item_quantity_positive"),
        CheckConstraint("unit_price >= 0", name="order_item_unit_price_non_negative"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id: Mapped[str] = mapped_column(String(100), nullable=False)
    product_name: Mapped[str] = mapped_column(String(160), nullable=False)
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    order: Mapped[Order] = relationship(back_populates="items")
