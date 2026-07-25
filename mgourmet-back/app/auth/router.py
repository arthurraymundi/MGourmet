from fastapi import APIRouter, HTTPException, status

from app.auth.dependencies import AdminServiceDep, CurrentAdminDep
from app.auth.schemas import AccessTokenResponse, AdminLogin, AdminRegister, AdminResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])
@router.post("/register", response_model=AdminResponse, status_code=status.HTTP_201_CREATED)
async def register_initial_admin(payload: AdminRegister, service: AdminServiceDep) -> AdminResponse:
    try:
        return await service.register_initial_admin(payload)
    except PermissionError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc


@router.post("/login", response_model=AccessTokenResponse)
async def login(payload: AdminLogin, service: AdminServiceDep) -> AccessTokenResponse:
    try:
        return await service.login(payload)
    except PermissionError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc


@router.get("/me", response_model=AdminResponse)
async def get_current_authenticated_admin(admin: CurrentAdminDep) -> AdminResponse:
    return admin
