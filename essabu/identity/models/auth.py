"""Auth models."""

from pydantic import BaseModel


class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    phone: str | None = None


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int


class TwoFactorResponse(BaseModel):
    secret: str
    qr_code_url: str
    recovery_codes: list[str] | None = None
