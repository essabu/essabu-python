"""Essabu SDK exception hierarchy."""

from __future__ import annotations

from typing import Any


class EssabuError(Exception):
    """Base exception for all Essabu SDK errors."""

    def __init__(
        self,
        message: str = "An error occurred with the Essabu API",
        status_code: int | None = None,
        body: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.body = body or {}
        self.headers = headers or {}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message={self.message!r}, status_code={self.status_code})"


class AuthenticationError(EssabuError):
    """Raised when authentication fails (401)."""

    def __init__(self, message: str = "Invalid API key or authentication token", **kwargs: Any) -> None:
        super().__init__(message=message, status_code=401, **kwargs)


class AuthorizationError(EssabuError):
    """Raised when authorization fails (403)."""

    def __init__(self, message: str = "You do not have permission to perform this action", **kwargs: Any) -> None:
        super().__init__(message=message, status_code=403, **kwargs)


class NotFoundError(EssabuError):
    """Raised when a resource is not found (404)."""

    def __init__(self, message: str = "Resource not found", **kwargs: Any) -> None:
        super().__init__(message=message, status_code=404, **kwargs)


class ValidationError(EssabuError):
    """Raised when request validation fails (422)."""

    def __init__(
        self,
        message: str = "Validation error",
        errors: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(message=message, status_code=422, **kwargs)
        self.errors = errors or []


class ConflictError(EssabuError):
    """Raised when a resource conflict occurs (409)."""

    def __init__(self, message: str = "Resource conflict", **kwargs: Any) -> None:
        super().__init__(message=message, status_code=409, **kwargs)


class RateLimitError(EssabuError):
    """Raised when rate limit is exceeded (429)."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        retry_after: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(message=message, status_code=429, **kwargs)
        self.retry_after = retry_after


class ServerError(EssabuError):
    """Raised when the server returns a 5xx error."""

    def __init__(self, message: str = "Internal server error", status_code: int = 500, **kwargs: Any) -> None:
        super().__init__(message=message, status_code=status_code, **kwargs)
