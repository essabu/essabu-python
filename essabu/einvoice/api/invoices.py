"""Invoices API module."""

from typing import Any

from essabu.common.http_client import HttpClient
from essabu.einvoice.models.invoice import (
    NormalizedInvoiceResponse,
    NormalizeInvoiceRequest,
)


class InvoicesApi:
    """Synchronous invoices API."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def normalize(self, data: dict[str, Any] | NormalizeInvoiceRequest) -> NormalizedInvoiceResponse:
        """Normalize an invoice."""
        payload = data.model_dump() if isinstance(data, NormalizeInvoiceRequest) else data
        response = self._http.post("/invoices/normalize", data=payload)
        return NormalizedInvoiceResponse(**response)

