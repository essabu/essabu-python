"""Submission models."""

from pydantic import BaseModel


class SubmitInvoiceRequest(BaseModel):
    """Request to submit an invoice."""

    invoice_id: str
    metadata: dict[str, str] | None = None


class SubmissionResponse(BaseModel):
    """Response from invoice submission."""

    submission_id: str
    invoice_id: str
    status: str
    status_label: str
    status_color: str
    submitted_at: str
    message: str | None = None


class SubmissionStatusResponse(BaseModel):
    """Response from submission status check."""

    submission_id: str
    invoice_id: str
    status: str
    status_label: str
    status_color: str
    submitted_at: str
    updated_at: str
    message: str | None = None
    errors: list[str] | None = None
