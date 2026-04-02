"""Permission models."""

from pydantic import BaseModel


class PermissionResponse(BaseModel):
    id: str
    name: str
    description: str | None = None
    group: str | None = None
    created_at: str
    updated_at: str
