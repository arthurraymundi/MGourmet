from typing import Annotated, Literal

from fastapi import APIRouter, Depends, Query

from app.core.schemas import ListResponse
from app.kit.dependencies import get_kit_service
from app.kit.schemas import KitResponse
from app.kit.service import KitService

router = APIRouter(prefix="/kits", tags=["Kits"])
ServiceDep = Annotated[KitService, Depends(get_kit_service)]


@router.get("", response_model=ListResponse[KitResponse], summary="Lista kits promocionais")
async def list_kits(
    service: ServiceDep,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=100),
    sort: Literal["name", "meals", "price"] = "meals",
    direction: Literal["asc", "desc"] = "asc",
) -> ListResponse[KitResponse]:
    return await service.list(
        page=page, page_size=page_size, sort=sort, descending=direction == "desc"
    )


@router.get("/{kit_id}", response_model=KitResponse, summary="Obtém um kit")
async def get_kit(kit_id: str, service: ServiceDep) -> KitResponse:
    return await service.get(kit_id)
