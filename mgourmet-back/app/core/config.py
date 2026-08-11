from functools import lru_cache
from typing import Literal
from typing import Literal
from typing import Literal

from pydantic import PostgresDsn, RedisDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações carregadas exclusivamente por variáveis de ambiente."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "M Gourmet API"
    environment: Literal["development", "staging", "production"]
    debug: bool = False
    database_url: PostgresDsn
    redis_url: RedisDsn
    cors_origins: str = "http://localhost:5173"
    jwt_secret_key: SecretStr
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 480

    def validate_for_production(self) -> None:
        if self.environment == "production":
            if self.debug:
                raise ValueError("DEBUG não pode estar ativo em produção.")
            if len(self.jwt_secret_key.get_secret_value()) < 32:
                raise ValueError("JWT_SECRET_KEY deve ter pelo menos 32 caracteres.")
            if any("localhost" in origin or "127.0.0.1" in origin for origin in self.cors_origin_list):
                raise ValueError("CORS de desenvolvimento não pode ser usado em produção.")
            if "ssl=" not in str(self.database_url):
                raise ValueError("DATABASE_URL de produção deve exigir SSL.")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.validate_for_production()
    return settings
