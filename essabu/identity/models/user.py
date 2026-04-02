"""User models."""

from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    phone: str | None = None
    status: str
    status_label: str
    status_color: str
    email_verified_at: str | None = None
    created_at: str
    updated_at: str
