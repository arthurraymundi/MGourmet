from fastapi import APIRouter, HTTPException, status

from app.auth.dependencies import AdminServiceDep, CurrentAdminDep
from app.auth.schemas import AccessTokenResponse, AdminLogin, AdminResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])
@router.post("/login", response_model=AccessTokenResponse)
async def login(payload: AdminLogin, service: AdminServiceDep) -> AccessTokenResponse:
    try:
        return await service.login(payload)
    except PermissionError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc


@router.get("/me", response_model=AdminResponse)
async def get_current_authenticated_admin(admin: CurrentAdminDep) -> AdminResponse:
    return admin
