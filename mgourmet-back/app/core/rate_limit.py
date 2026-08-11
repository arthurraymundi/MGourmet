from collections import defaultdict, deque
from time import monotonic

from fastapi import Request, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Basic per-process guard; production deployments should also rate-limit at the gateway."""

    def __init__(self, app) -> None:
        super().__init__(app)
        self._requests: dict[tuple[str, str], deque[float]] = defaultdict(deque)
        self._limits = {"/api/v1/auth/login": (5, 60), "/api/v1/orders": (20, 60)}

    async def dispatch(self, request: Request, call_next):
        limit = self._limits.get(request.url.path)
        if limit and request.method == "POST":
            client = request.client.host if request.client else "unknown"
            bucket = self._requests[(request.url.path, client)]
            now = monotonic()
            while bucket and bucket[0] <= now - limit[1]:
                bucket.popleft()
            if len(bucket) >= limit[0]:
                return JSONResponse({"detail": "Muitas requisições."}, status_code=status.HTTP_429_TOO_MANY_REQUESTS, headers={"Retry-After": str(limit[1])})
            bucket.append(now)
        return await call_next(request)
