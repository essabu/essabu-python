"""Compliance models."""

from typing import Any

from pydantic import BaseModel


class ComplianceReportRequest(BaseModel):
    """Request to generate a compliance report."""

    start_date: str
    end_date: str
    format: str = "json"
    filters: dict[str, Any] | None = None


class ComplianceReportResponse(BaseModel):
    """Response from compliance report generation."""

    report_id: str
    start_date: str
    end_date: str
    generated_at: str
    total_invoices: int
    compliant_count: int
    non_compliant_count: int
    compliance_rate: float
    details: list[dict[str, Any]] | None = None
    download_url: str | None = None
