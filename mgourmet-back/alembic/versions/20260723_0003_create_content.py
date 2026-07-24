"""create testimonials and faqs

Revision ID: 20260723_0003
Revises: 20260723_0002
Create Date: 2026-07-23 00:00:02
"""

from alembic import op
import sqlalchemy as sa

revision = "20260723_0003"
down_revision = "20260723_0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    for table_name, content_column, content_type in (
        ("testimonials", "quote", sa.Text()),
        ("faqs", "answer", sa.Text()),
    ):
        label_column = "name" if table_name == "testimonials" else "question"
        label_type = sa.String(length=120 if table_name == "testimonials" else 500)
        columns = [
            sa.Column("id", sa.String(length=100), nullable=False),
            sa.Column(label_column, label_type, nullable=False),
        ]
        if table_name == "testimonials":
            columns.append(sa.Column("role", sa.String(length=120), nullable=False))
        columns.extend(
            [
                sa.Column(content_column, content_type, nullable=False),
                sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()),
                sa.Column(
                    "created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()
                ),
                sa.Column(
                    "updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()
                ),
                sa.PrimaryKeyConstraint("id", name=f"pk_{table_name}"),
            ]
        )
        op.create_table(table_name, *columns)
        op.create_index(f"ix_{table_name}_active", table_name, ["active"])


def downgrade() -> None:
    for table_name in ("faqs", "testimonials"):
        op.drop_index(f"ix_{table_name}_active", table_name=table_name)
        op.drop_table(table_name)
