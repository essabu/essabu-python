"""Tenant models."""

from pydantic import BaseModel


class TenantResponse(BaseModel):
    id: str
    name: str
    slug: str
    domain: str | None = None
    status: str
    status_label: str
    status_color: str
    created_at: str
    updated_at: str
