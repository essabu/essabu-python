"""Auth API module."""

from typing import Any

from essabu.common.http_client import HttpClient
from essabu.identity.models.auth import TokenResponse, TwoFactorResponse
from essabu.identity.models.user import UserResponse


class AuthApi:
    """Auth API for login, registration, and token management."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def login(self, email: str, password: str) -> TokenResponse:
        response = self._http.post("/auth/login", data={"email": email, "password": password})
        return TokenResponse(**response)

    def register(self, email: str, password: str, first_name: str, last_name: str, **kwargs: Any) -> UserResponse:
        data = {"email": email, "password": password, "first_name": first_name, "last_name": last_name, **kwargs}
        response = self._http.post("/auth/register", data=data)
        return UserResponse(**response)

    def refresh(self, refresh_token: str) -> TokenResponse:
        response = self._http.post("/auth/refresh", data={"refresh_token": refresh_token})
        return TokenResponse(**response)

    def logout(self) -> dict[str, Any]:
        return self._http.post("/auth/logout")

    def verify_email(self, token: str) -> dict[str, Any]:
        return self._http.post("/auth/verify-email", data={"token": token})

    def reset_password(self, email: str) -> dict[str, Any]:
        return self._http.post("/auth/reset-password", data={"email": email})

    def enable_2fa(self) -> TwoFactorResponse:
        response = self._http.post("/auth/2fa/enable")
        return TwoFactorResponse(**response)
