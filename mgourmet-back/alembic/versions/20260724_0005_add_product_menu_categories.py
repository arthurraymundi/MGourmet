"""add product menu categories

Revision ID: 20260724_0005
Revises: 20260723_0004
Create Date: 2026-07-24 00:00:00
"""

from alembic import op


revision = "20260724_0005"
down_revision = "20260723_0004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Append values to the existing PostgreSQL enum without changing stored rows."""
    for category in (
        "Prato Fitness",
        "Mini Prato Fitness",
        "Prato Kids",
        "Sopa",
        "Proteína",
        "Premium",
    ):
        op.execute(f"ALTER TYPE product_category ADD VALUE IF NOT EXISTS '{category}'")


def downgrade() -> None:
    """PostgreSQL does not safely support removing enum values; keep them intact."""
    pass
