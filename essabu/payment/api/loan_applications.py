"""API client for loan applications operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class LoanApplicationsApi(BaseApi):
    """API client for loan applications operations."""

    _resource_path = "/loan-applications"
