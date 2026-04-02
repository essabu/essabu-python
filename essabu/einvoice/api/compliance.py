"""Compliance API module."""

from typing import Any

from essabu.common.http_client import HttpClient
from essabu.einvoice.models.compliance import (
    ComplianceReportRequest,
    ComplianceReportResponse,
)


class ComplianceApi:
    """Synchronous compliance API."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def generate_report(
        self, params: dict[str, Any] | ComplianceReportRequest
    ) -> ComplianceReportResponse:
        """Generate a compliance report."""
        payload = params.model_dump(exclude_none=True) if isinstance(params, ComplianceReportRequest) else params
        response = self._http.post("/compliance/reports", data=payload)
        return ComplianceReportResponse(**response)

