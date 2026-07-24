from typing import Annotated

from pydantic import Field

from app.content.models import ContentSection
from app.core.schemas import APIModel

ContentId = Annotated[str, Field(pattern=r"^[a-z0-9]+(?:-[a-z0-9]+)*$", min_length=1, max_length=100)]


class TestimonialCreate(APIModel):
    id: ContentId
    name: str = Field(min_length=2, max_length=120)
    role: str = Field(min_length=2, max_length=120)
    quote: str = Field(min_length=2, max_length=5000)
    active: bool = True


class TestimonialUpdate(APIModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    role: str | None = Field(default=None, min_length=2, max_length=120)
    quote: str | None = Field(default=None, min_length=2, max_length=5000)
    active: bool | None = None


class TestimonialResponse(APIModel):
    id: str
    name: str
    role: str
    quote: str


class FaqCreate(APIModel):
    id: ContentId
    question: str = Field(min_length=2, max_length=500)
    answer: str = Field(min_length=2, max_length=5000)
    active: bool = True


class FaqUpdate(APIModel):
    question: str | None = Field(default=None, min_length=2, max_length=500)
    answer: str | None = Field(default=None, min_length=2, max_length=5000)
    active: bool | None = None


class FaqResponse(APIModel):
    id: str
    question: str
    answer: str


class ContentItemCreate(APIModel):
    id: ContentId
    section: ContentSection
    text: str = Field(min_length=2, max_length=500)
    position: int = Field(ge=0)
    active: bool = True


class ContentItemUpdate(APIModel):
    text: str | None = Field(default=None, min_length=2, max_length=500)
    position: int | None = Field(default=None, ge=0)
    active: bool | None = None


class ContentItemResponse(APIModel):
    id: str
    text: str
    position: int


class ContactInfoUpdate(APIModel):
    whatsapp: str = Field(min_length=3, max_length=50)
    instagram: str = Field(min_length=2, max_length=100)
    address: str = Field(min_length=2, max_length=500)
    business_hours: str = Field(min_length=2, max_length=500)


class ContactInfoResponse(ContactInfoUpdate):
    pass
