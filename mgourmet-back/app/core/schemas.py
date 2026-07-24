from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

ItemT = TypeVar("ItemT")


class PaginationMeta(BaseModel):
    page: int = Field(ge=1)
    page_size: int = Field(ge=1)
    total: int = Field(ge=0)
    total_pages: int = Field(ge=0)


class ListResponse(BaseModel, Generic[ItemT]):
    items: list[ItemT]
    meta: PaginationMeta


class APIModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        alias_generator=lambda field_name: "".join(
            part.capitalize() if index else part
            for index, part in enumerate(field_name.split("_"))
        ),
    )
