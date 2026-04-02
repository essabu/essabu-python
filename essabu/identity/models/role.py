"""Role models."""

from pydantic import BaseModel


class RoleResponse(BaseModel):
    id: str
    name: str
    description: str | None = None
    permissions: list[str] | None = None
    created_at: str
    updated_at: str
