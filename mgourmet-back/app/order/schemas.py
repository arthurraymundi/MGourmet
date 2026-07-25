from datetime import datetime
from decimal import Decimal

from pydantic import Field, field_serializer, model_validator

from app.core.schemas import APIModel
from app.order.models import DeliveryMethod, OrderStatus
from app.product.schemas import ProductId


class OrderItemCreate(APIModel):
    product_id: ProductId
    quantity: int = Field(ge=1, le=100)


class OrderCreate(APIModel):
    customer_name: str = Field(min_length=2, max_length=160)
    customer_phone: str = Field(min_length=3, max_length=50)
    delivery_method: DeliveryMethod
    street: str | None = Field(default=None, max_length=255)
    number: str | None = Field(default=None, max_length=40)
    neighborhood: str | None = Field(default=None, max_length=160)
    complement: str | None = Field(default=None, max_length=255)
    notes: str | None = Field(default=None, max_length=5000)
    items: list[OrderItemCreate] = Field(min_length=1, max_length=100)

    @model_validator(mode="after")
    def validate_delivery_address(self) -> "OrderCreate":
        if self.delivery_method == DeliveryMethod.DELIVERY:
            required_fields = (self.street, self.number, self.neighborhood)
            if not all(field and field.strip() for field in required_fields):
                raise ValueError("Rua, número e bairro são obrigatórios para entrega.")
        return self


class OrderStatusUpdate(APIModel):
    status: OrderStatus


class OrderItemResponse(APIModel):
    id: int
    product_id: str
    product_name: str
    unit_price: Decimal
    quantity: int

    @field_serializer("unit_price")
    def serialize_unit_price(self, value: Decimal) -> float:
        return float(value)


class OrderResponse(APIModel):
    id: int
    customer_name: str
    customer_phone: str
    delivery_method: DeliveryMethod
    street: str | None
    number: str | None
    neighborhood: str | None
    complement: str | None
    notes: str | None
    status: OrderStatus
    total: Decimal
    created_at: datetime
    items: list[OrderItemResponse]

    @field_serializer("total")
    def serialize_total(self, value: Decimal) -> float:
        return float(value)

    @classmethod
    def from_order(cls, order: object) -> "OrderResponse":
        return cls.model_validate(order)
