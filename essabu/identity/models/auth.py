"""Authentication models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LoginRequest:
    email: str
    password: str


@dataclass
class TokenResponse:
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int = 3600
