"""Verification models."""

from typing import Any

from pydantic import BaseModel


class VerifyInvoiceRequest(BaseModel):
    """Request to verify an invoice."""

    invoice_id: str


class VerificationResponse(BaseModel):
    """Response from invoice verification."""

    invoice_id: str
    is_valid: bool
    verified_at: str
    details: dict[str, Any] | None = None
    errors: list[str] | None = None
