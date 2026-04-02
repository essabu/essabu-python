"""Company models."""

from pydantic import BaseModel


class CompanyResponse(BaseModel):
    id: str
    name: str
    tin: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    status: str
    status_label: str
    status_color: str
    created_at: str
    updated_at: str
