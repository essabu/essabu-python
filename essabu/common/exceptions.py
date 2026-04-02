"""Unified exception hierarchy for the Essabu SDK.

All SDK exceptions inherit from EssabuError, allowing callers
to catch a single base type for uniform error handling.
"""

from __future__ import annotations

from typing import Any


class EssabuError(Exception):
    """Base exception for all Essabu SDK errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}

    def __str__(self) -> str:
        if self.status_code:
            return f"[{self.status_code}] {self.message}"
        return self.message


class AuthenticationError(EssabuError):
    """Raised when authentication fails (401)."""

    def __init__(self, message: str = "Authentication failed", **kwargs: Any) -> None:
        super().__init__(message, status_code=401, **kwargs)


class AuthorizationError(EssabuError):
    """Raised when the user lacks permissions (403)."""

    def __init__(self, message: str = "Forbidden", **kwargs: Any) -> None:
        super().__init__(message, status_code=403, **kwargs)


class NotFoundError(EssabuError):
    """Raised when a resource is not found (404)."""

    def __init__(self, message: str = "Resource not found", **kwargs: Any) -> None:
        super().__init__(message, status_code=404, **kwargs)


class ValidationError(EssabuError):
    """Raised when request validation fails (400/422)."""

    def __init__(
        self,
        message: str = "Validation failed",
        errors: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(message, status_code=422, **kwargs)
        self.errors = errors or {}


class RateLimitError(EssabuError):
    """Raised when the API rate limit is exceeded (429)."""

    def __init__(
        self,
        message: str = "Rate limit exceeded",
        retry_after: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(message, status_code=429, **kwargs)
        self.retry_after = retry_after


class ServerError(EssabuError):
    """Raised when the server returns a 5xx error."""

    def __init__(self, message: str = "Internal server error", **kwargs: Any) -> None:
        super().__init__(message, status_code=500, **kwargs)
