"""create products

Revision ID: 20260723_0001
Revises:
Create Date: 2026-07-23 00:00:00
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "20260723_0001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    product_category = postgresql.ENUM(
        "Hiperproteica",
        "Low Carb",
        "Emagrecimento",
        "Ganho de Massa",
        "Vegetariana",
        name="product_category",
        create_type=False,
    )
    product_category.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "products",
        sa.Column("id", sa.String(length=100), nullable=False),
        sa.Column("name", sa.String(length=160), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("image_url", sa.String(length=2048), nullable=False),
        sa.Column("price", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("category", product_category, nullable=False),
        sa.Column("ingredients", postgresql.ARRAY(sa.String(length=120)), nullable=False),
        sa.Column("calories", sa.Integer(), nullable=False),
        sa.Column("protein", sa.Integer(), nullable=False),
        sa.Column("carbs", sa.Integer(), nullable=False),
        sa.Column("fat", sa.Integer(), nullable=False),
        sa.Column("featured", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("price >= 0", name="ck_products_product_price_non_negative"),
        sa.CheckConstraint("calories >= 0", name="ck_products_product_calories_non_negative"),
        sa.CheckConstraint("protein >= 0", name="ck_products_product_protein_non_negative"),
        sa.CheckConstraint("carbs >= 0", name="ck_products_product_carbs_non_negative"),
        sa.CheckConstraint("fat >= 0", name="ck_products_product_fat_non_negative"),
        sa.PrimaryKeyConstraint("id", name="pk_products"),
    )
    op.create_index("ix_products_name", "products", ["name"])
    op.create_index("ix_products_category", "products", ["category"])
    op.create_index("ix_products_featured", "products", ["featured"])


def downgrade() -> None:
    op.drop_index("ix_products_featured", table_name="products")
    op.drop_index("ix_products_category", table_name="products")
    op.drop_index("ix_products_name", table_name="products")
    op.drop_table("products")
    postgresql.ENUM(name="product_category").drop(
        op.get_bind(),
        checkfirst=True
    )
