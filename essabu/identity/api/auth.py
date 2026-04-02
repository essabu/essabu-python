"""API for authentication in the identity module."""

from __future__ import annotations

from typing import Any

from essabu.identity.api.base import BaseIdentityApi


class AuthApi(BaseIdentityApi):
    """Authentication operations."""

    def login(self, *, email: str, password: str, **data: Any) -> dict[str, Any]:
        """Authenticate with email and password."""
        return self._http.post(self._path("auth", "login"), json={"email": email, "password": password, **data})

    def register(self, **data: Any) -> dict[str, Any]:
        """Register a new user account."""
        return self._create(self._path("auth", "register"), data)

    def refresh(self, *, refresh_token: str) -> dict[str, Any]:
        """Refresh an access token."""
        return self._http.post(self._path("auth", "refresh"), json={"refreshToken": refresh_token})

    def logout(self) -> dict[str, Any]:
        """Invalidate the current session."""
        return self._http.post(self._path("auth", "logout"), json={})

    def forgot_password(self, *, email: str) -> dict[str, Any]:
        """Request a password reset email."""
        return self._http.post(self._path("auth", "forgot-password"), json={"email": email})

    def reset_password(self, *, token: str, password: str) -> dict[str, Any]:
        """Reset password using a reset token."""
        return self._http.post(self._path("auth", "reset-password"), json={"token": token, "password": password})

    def verify_email(self, *, token: str) -> dict[str, Any]:
        """Verify an email address."""
        return self._http.post(self._path("auth", "verify-email"), json={"token": token})

    def me(self) -> dict[str, Any]:
        """Get the authenticated user profile."""
        return self._http.get(self._path("auth", "me"))
