"""Branch models."""

from pydantic import BaseModel


class BranchResponse(BaseModel):
    id: str
    name: str
    company_id: str
    address: str | None = None
    phone: str | None = None
    status: str
    status_label: str
    status_color: str
    created_at: str
    updated_at: str
