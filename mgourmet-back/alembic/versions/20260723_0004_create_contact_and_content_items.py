"""create contact info and content items

Revision ID: 20260723_0004
Revises: 20260723_0003
Create Date: 2026-07-23 00:00:03
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "20260723_0004"
down_revision = "20260723_0003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    content_section = postgresql.ENUM(
        "benefits",
        "how-it-works",
        name="content_section",
        create_type=False,
    )

    content_section.create(op.get_bind(), checkfirst=True)
    op.create_table(
        "content_items",
        sa.Column("id", sa.String(length=100), nullable=False),
        sa.Column("section", content_section, nullable=False),
        sa.Column("text", sa.String(length=500), nullable=False),
        sa.Column("position", sa.Integer(), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("position >= 0", name="ck_content_items_content_item_position_non_negative"),
        sa.PrimaryKeyConstraint("id", name="pk_content_items"),
    )
    op.create_index("ix_content_items_section", "content_items", ["section"])
    op.create_index("ix_content_items_active", "content_items", ["active"])
    op.create_table(
        "contact_info",
        sa.Column("id", sa.String(length=100), nullable=False),
        sa.Column("whatsapp", sa.String(length=50), nullable=False),
        sa.Column("instagram", sa.String(length=100), nullable=False),
        sa.Column("address", sa.String(length=500), nullable=False),
        sa.Column("business_hours", sa.String(length=500), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.PrimaryKeyConstraint("id", name="pk_contact_info"),
    )


def downgrade() -> None:
    op.drop_table("contact_info")
    op.drop_index("ix_content_items_active", table_name="content_items")
    op.drop_index("ix_content_items_section", table_name="content_items")
    op.drop_table("content_items")
    postgresql.ENUM(name="content_section").drop(
        op.get_bind(),
        checkfirst=True
    )
