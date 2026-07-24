from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError


class EntityNotFoundError(Exception):
    """Raised when a requested entity does not exist."""


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(EntityNotFoundError)
    async def entity_not_found_handler(_: Request, exc: EntityNotFoundError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": str(exc) or "Recurso não encontrado."},
        )

    @app.exception_handler(IntegrityError)
    async def integrity_error_handler(_: Request, __: IntegrityError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": "A operação viola uma restrição de dados."},
        )
