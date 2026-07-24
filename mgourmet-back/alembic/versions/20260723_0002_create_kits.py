"""create kits

Revision ID: 20260723_0002
Revises: 20260723_0001
Create Date: 2026-07-23 00:00:01
"""

from alembic import op
import sqlalchemy as sa

revision = "20260723_0002"
down_revision = "20260723_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "kits",
        sa.Column("id", sa.String(length=100), nullable=False),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("meals", sa.Integer(), nullable=False),
        sa.Column("original_price", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("discounted_price", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("meals > 0", name="ck_kits_kit_meals_positive"),
        sa.CheckConstraint(
            "original_price >= 0", name="ck_kits_kit_original_price_non_negative"
        ),
        sa.CheckConstraint(
            "discounted_price >= 0", name="ck_kits_kit_discounted_price_non_negative"
        ),
        sa.CheckConstraint(
            "discounted_price <= original_price",
            name="ck_kits_kit_discounted_price_not_greater_than_original",
        ),
        sa.PrimaryKeyConstraint("id", name="pk_kits"),
    )
    op.create_index("ix_kits_name", "kits", ["name"])
    op.create_index("ix_kits_meals", "kits", ["meals"])


def downgrade() -> None:
    op.drop_index("ix_kits_meals", table_name="kits")
    op.drop_index("ix_kits_name", table_name="kits")
    op.drop_table("kits")
