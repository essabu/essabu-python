"""Submissions API module."""

from typing import Any

from essabu.common.http_client import HttpClient
from essabu.einvoice.models.submission import (
    SubmissionResponse,
    SubmissionStatusResponse,
    SubmitInvoiceRequest,
)


class SubmissionsApi:
    """Synchronous submissions API."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def submit(
        self, invoice_id: str, metadata: dict[str, str] | None = None
    ) -> SubmissionResponse:
        """Submit an invoice."""
        payload = SubmitInvoiceRequest(invoice_id=invoice_id, metadata=metadata)
        response = self._http.post("/submissions", data=payload.model_dump(exclude_none=True))
        return SubmissionResponse(**response)

    def check_status(self, submission_id: str) -> SubmissionStatusResponse:
        """Check the status of a submission."""
        response = self._http.get(f"/submissions/{submission_id}/status")
        return SubmissionStatusResponse(**response)

