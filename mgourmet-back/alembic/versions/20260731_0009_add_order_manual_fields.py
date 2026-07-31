"""add order manual fields

Revision ID: 20260731_0009
Revises: 20260725_0008
Create Date: 2026-07-31 00:00:00
"""

import sqlalchemy as sa
from alembic import op


revision = "20260731_0009"
down_revision = "20260725_0008"
branch_labels = None
depends_on = None


order_source = sa.Enum("site", "telefone", "whatsapp", "presencial", name="order_source")


def upgrade() -> None:
    order_source.create(op.get_bind(), checkfirst=True)
    op.add_column(
        "orders",
        sa.Column("source", order_source, nullable=False, server_default="site"),
    )
    op.add_column("orders", sa.Column("payment_method", sa.String(length=100), nullable=True))
    op.alter_column("orders", "source", server_default=None)
    op.execute(
        "UPDATE contact_info SET whatsapp = '+55 11 97670-2164', "
        "instagram = 'https://www.instagram.com/mgourmet_comidafit.ofc/', "
        "address = 'Entregas em Jundiaí/SP' WHERE id = 'default'"
    )


def downgrade() -> None:
    op.drop_column("orders", "payment_method")
    op.drop_column("orders", "source")
    order_source.drop(op.get_bind(), checkfirst=True)
