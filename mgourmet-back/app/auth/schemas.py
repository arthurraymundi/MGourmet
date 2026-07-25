from datetime import datetime

from pydantic import Field, field_validator

from app.core.schemas import APIModel


class AdminRegister(APIModel):
    name: str = Field(min_length=2, max_length=160)
    email: str = Field(min_length=5, max_length=320)
    password: str = Field(min_length=12, max_length=128)

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        normalized = value.strip().lower()
        if normalized.count("@") != 1 or normalized.startswith("@") or normalized.endswith("@"):
            raise ValueError("Informe um e-mail válido.")
        return normalized


class AdminLogin(APIModel):
    email: str = Field(min_length=5, max_length=320)
    password: str = Field(min_length=1, max_length=128)

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        return value.strip().lower()


class AdminResponse(APIModel):
    id: int
    name: str
    email: str
    created_at: datetime

    @classmethod
    def from_admin(cls, admin: object) -> "AdminResponse":
        return cls(
            id=getattr(admin, "id"),
            name=getattr(admin, "name"),
            email=getattr(admin, "email"),
            created_at=getattr(admin, "created_at"),
        )


class AccessTokenResponse(APIModel):
    access_token: str
    token_type: str = "bearer"
