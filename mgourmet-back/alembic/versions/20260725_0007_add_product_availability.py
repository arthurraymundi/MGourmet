"""add product availability

Revision ID: 20260725_0007
Revises: 20260725_0006
Create Date: 2026-07-25 00:00:00
"""

import sqlalchemy as sa
from alembic import op


revision = "20260725_0007"
down_revision = "20260725_0006"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "products",
        sa.Column("is_available", sa.Boolean(), server_default=sa.true(), nullable=False),
    )
    op.create_index(op.f("ix_products_is_available"), "products", ["is_available"], unique=False)
    op.alter_column("products", "is_available", server_default=None)


def downgrade() -> None:
    op.drop_index(op.f("ix_products_is_available"), table_name="products")
    op.drop_column("products", "is_available")
