from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.repository import AdminRepository
from app.auth.schemas import AdminResponse
from app.auth.service import AdminService
from app.core.config import Settings, get_settings
from app.core.database import get_session

bearer_scheme = HTTPBearer(auto_error=False)


def get_admin_service(
    session: AsyncSession = Depends(get_session), settings: Settings = Depends(get_settings)
) -> AdminService:
    return AdminService(AdminRepository(session), settings)


AdminServiceDep = Annotated[AdminService, Depends(get_admin_service)]


async def get_current_admin(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
    service: AdminServiceDep,
) -> AdminResponse:
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Autenticação necessária.")
    try:
        return await service.get_authenticated_admin(credentials.credentials)
    except PermissionError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc


CurrentAdminDep = Annotated[AdminResponse, Depends(get_current_admin)]
