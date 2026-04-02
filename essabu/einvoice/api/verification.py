"""Verification API module."""

from essabu.common.http_client import HttpClient
from essabu.einvoice.models.verification import VerificationResponse


class VerificationApi:
    """Synchronous verification API."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def verify(self, invoice_id: str) -> VerificationResponse:
        """Verify an invoice."""
        response = self._http.post("/verification/verify", data={"invoice_id": invoice_id})
        return VerificationResponse(**response)

