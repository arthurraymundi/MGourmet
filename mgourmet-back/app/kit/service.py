from math import ceil

from app.core.exceptions import EntityNotFoundError
from app.core.schemas import ListResponse, PaginationMeta
from app.kit.models import Kit
from app.kit.repository import KitRepository
from app.kit.schemas import KitCreate, KitResponse, KitUpdate


class KitService:
    def __init__(self, repository: KitRepository) -> None:
        self._repository = repository

    async def get(self, kit_id: str) -> KitResponse:
        kit = await self._repository.get_by_id(kit_id)
        if kit is None:
            raise EntityNotFoundError("Kit não encontrado.")
        return KitResponse.model_validate(kit)

    async def list(
        self, *, page: int, page_size: int, sort: str = "meals", descending: bool = False
    ) -> ListResponse[KitResponse]:
        kits, total = await self._repository.list(
            sort=sort,
            descending=descending,
            offset=(page - 1) * page_size,
            limit=page_size,
        )
        return ListResponse[KitResponse](
            items=[KitResponse.model_validate(kit) for kit in kits],
            meta=PaginationMeta(
                page=page,
                page_size=page_size,
                total=total,
                total_pages=ceil(total / page_size) if total else 0,
            ),
        )

    async def create(self, payload: KitCreate) -> KitResponse:
        if await self._repository.get_by_id(payload.id) is not None:
            raise ValueError("Já existe um kit com este identificador.")
        kit = Kit(id=payload.id, **payload.model_dump(exclude={"id"}))
        return KitResponse.model_validate(await self._repository.create(kit))

    async def update(self, kit_id: str, payload: KitUpdate) -> KitResponse:
        kit = await self._repository.get_by_id(kit_id)
        if kit is None:
            raise EntityNotFoundError("Kit não encontrado.")
        changes = payload.model_dump(exclude_unset=True)
        candidate = KitResponse.model_validate({**KitResponse.model_validate(kit).model_dump(), **changes})
        for field, value in candidate.model_dump(exclude={"id"}).items():
            setattr(kit, field, value)
        return KitResponse.model_validate(await self._repository.update(kit))
