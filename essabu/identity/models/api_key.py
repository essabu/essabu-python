"""API Key models."""

from pydantic import BaseModel


class ApiKeyResponse(BaseModel):
    id: str
    name: str
    key: str | None = None
    prefix: str
    status: str
    status_label: str
    status_color: str
    last_used_at: str | None = None
    expires_at: str | None = None
    created_at: str
    updated_at: str
