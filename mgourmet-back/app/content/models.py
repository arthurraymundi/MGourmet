from enum import StrEnum

from sqlalchemy import Boolean, CheckConstraint, Enum, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.models import Base, TimestampMixin


class Testimonial(TimestampMixin, Base):
    __tablename__ = "testimonials"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str] = mapped_column(String(120), nullable=False)
    quote: Mapped[str] = mapped_column(Text, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)


class Faq(TimestampMixin, Base):
    __tablename__ = "faqs"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    question: Mapped[str] = mapped_column(String(500), nullable=False)
    answer: Mapped[str] = mapped_column(Text, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)


class ContentSection(StrEnum):
    BENEFITS = "benefits"
    HOW_IT_WORKS = "how-it-works"


class ContentItem(TimestampMixin, Base):
    __tablename__ = "content_items"
    __table_args__ = (CheckConstraint("position >= 0", name="content_item_position_non_negative"),)

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    section: Mapped[ContentSection] = mapped_column(
        Enum(
            ContentSection,
            name="content_section",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        nullable=False,
    )
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    position: Mapped[int] = mapped_column(Integer, nullable=False)
    active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)


class ContactInfo(TimestampMixin, Base):
    __tablename__ = "contact_info"

    id: Mapped[str] = mapped_column(String(100), primary_key=True)
    whatsapp: Mapped[str] = mapped_column(String(50), nullable=False)
    instagram: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(500), nullable=False)
    business_hours: Mapped[str] = mapped_column(String(500), nullable=False)
