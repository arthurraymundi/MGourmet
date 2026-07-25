from datetime import UTC, datetime
from types import SimpleNamespace

import pytest

from app.auth.models import AdminUser
from app.auth.schemas import AdminLogin, AdminRegister
from app.auth.service import AdminService


class FakeAdminRepository:
    def __init__(self) -> None:
        self.admins: list[AdminUser] = []

    async def count(self) -> int:
        return len(self.admins)

    async def get_by_email(self, email: str) -> AdminUser | None:
        return next((admin for admin in self.admins if admin.email == email), None)

    async def get_by_id(self, admin_id: int) -> AdminUser | None:
        return next((admin for admin in self.admins if admin.id == admin_id), None)

    async def create(self, admin: AdminUser) -> AdminUser:
        admin.id = len(self.admins) + 1
        admin.created_at = datetime.now(UTC)
        self.admins.append(admin)
        return admin


def make_service(repository: FakeAdminRepository) -> AdminService:
    settings = SimpleNamespace(
        jwt_secret_key=SimpleNamespace(get_secret_value=lambda: "test-secret-with-at-least-thirty-two-characters"),
        jwt_algorithm="HS256",
        jwt_access_token_expire_minutes=30,
    )
    return AdminService(repository, settings)  # type: ignore[arg-type]


@pytest.mark.asyncio
async def test_initial_admin_can_register_and_login() -> None:
    repository = FakeAdminRepository()
    service = make_service(repository)

    admin = await service.register_initial_admin(
        AdminRegister(name="M Gourmet", email="ADMIN@EXAMPLE.COM", password="senha-segura-123")
    )
    token = await service.login(AdminLogin(email="admin@example.com", password="senha-segura-123"))

    assert admin.email == "admin@example.com"
    assert token.access_token


@pytest.mark.asyncio
async def test_registration_is_blocked_after_initial_admin() -> None:
    repository = FakeAdminRepository()
    service = make_service(repository)
    payload = AdminRegister(name="M Gourmet", email="admin@example.com", password="senha-segura-123")

    await service.register_initial_admin(payload)

    with pytest.raises(PermissionError, match="já foi cadastrado"):
        await service.register_initial_admin(payload)
