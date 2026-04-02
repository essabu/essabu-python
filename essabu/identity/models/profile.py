"""Profile models."""

from typing import Any

from pydantic import BaseModel


class ProfileResponse(BaseModel):
    id: str
    user_id: str
    avatar_url: str | None = None
    bio: str | None = None
    locale: str | None = None
    timezone: str | None = None
    metadata: dict[str, Any] | None = None
    created_at: str
    updated_at: str
