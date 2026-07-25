from datetime import UTC, datetime, timedelta

import jwt
from pwdlib import PasswordHash

from app.auth.models import AdminUser
from app.auth.repository import AdminRepository
from app.auth.schemas import AccessTokenResponse, AdminLogin, AdminRegister, AdminResponse
from app.core.config import Settings

_password_hash = PasswordHash.recommended()


class AdminService:
    def __init__(self, repository: AdminRepository, settings: Settings) -> None:
        self._repository = repository
        self._settings = settings

    async def register_initial_admin(self, payload: AdminRegister) -> AdminResponse:
        if await self._repository.count() > 0:
            raise PermissionError("O administrador inicial já foi cadastrado.")

        admin = AdminUser(
            name=payload.name.strip(),
            email=payload.email,
            hashed_password=_password_hash.hash(payload.password),
        )
        return AdminResponse.from_admin(await self._repository.create(admin))

    async def login(self, payload: AdminLogin) -> AccessTokenResponse:
        admin = await self._repository.get_by_email(payload.email)
        if admin is None or not _password_hash.verify(payload.password, admin.hashed_password):
            raise PermissionError("E-mail ou senha inválidos.")

        expires_at = datetime.now(UTC) + timedelta(minutes=self._settings.jwt_access_token_expire_minutes)
        token = jwt.encode(
            {"sub": str(admin.id), "exp": expires_at},
            self._settings.jwt_secret_key.get_secret_value(),
            algorithm=self._settings.jwt_algorithm,
        )
        return AccessTokenResponse(access_token=token)

    async def get_authenticated_admin(self, token: str) -> AdminResponse:
        try:
            payload = jwt.decode(
                token,
                self._settings.jwt_secret_key.get_secret_value(),
                algorithms=[self._settings.jwt_algorithm],
            )
            subject = payload.get("sub")
            admin_id = int(subject)
        except (jwt.InvalidTokenError, TypeError, ValueError):
            raise PermissionError("Token de acesso inválido.") from None

        admin = await self._repository.get_by_id(admin_id)
        if admin is None:
            raise PermissionError("Token de acesso inválido.")
        return AdminResponse.from_admin(admin)
