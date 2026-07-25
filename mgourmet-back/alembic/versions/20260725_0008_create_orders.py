"""create orders

Revision ID: 20260725_0008
Revises: 20260725_0007
Create Date: 2026-07-25 00:00:00
"""

import sqlalchemy as sa
from alembic import op


revision = "20260725_0008"
down_revision = "20260725_0007"
branch_labels = None
depends_on = None


delivery_method = sa.Enum("pickup", "delivery", name="delivery_method")
order_status = sa.Enum(
    "Recebido", "Preparando", "Saiu para entrega", "Finalizado", "Cancelado", name="order_status"
)


def upgrade() -> None:
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("customer_name", sa.String(length=160), nullable=False),
        sa.Column("customer_phone", sa.String(length=50), nullable=False),
        sa.Column("delivery_method", delivery_method, nullable=False),
        sa.Column("street", sa.String(length=255)),
        sa.Column("number", sa.String(length=40)),
        sa.Column("neighborhood", sa.String(length=160)),
        sa.Column("complement", sa.String(length=255)),
        sa.Column("notes", sa.Text()),
        sa.Column("status", order_status, nullable=False),
        sa.Column("total", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint("total >= 0", name=op.f("ck_orders_order_total_non_negative")),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_orders")),
    )
    op.create_index(op.f("ix_orders_status"), "orders", ["status"], unique=False)
    op.create_table(
        "order_items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("order_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.String(length=100), nullable=False),
        sa.Column("product_name", sa.String(length=160), nullable=False),
        sa.Column("unit_price", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.CheckConstraint("quantity > 0", name=op.f("ck_order_items_order_item_quantity_positive")),
        sa.CheckConstraint("unit_price >= 0", name=op.f("ck_order_items_order_item_unit_price_non_negative")),
        sa.ForeignKeyConstraint(["order_id"], ["orders.id"], name=op.f("fk_order_items_order_id_orders"), ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_order_items")),
    )
    op.create_index(op.f("ix_order_items_order_id"), "order_items", ["order_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_order_items_order_id"), table_name="order_items")
    op.drop_table("order_items")
    op.drop_index(op.f("ix_orders_status"), table_name="orders")
    op.drop_table("orders")
    order_status.drop(op.get_bind(), checkfirst=True)
    delivery_method.drop(op.get_bind(), checkfirst=True)
