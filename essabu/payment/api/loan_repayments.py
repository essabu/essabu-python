"""API client for loan repayments operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class LoanRepaymentsApi(BaseApi):
    """API client for loan repayments operations."""

    _resource_path = "/loan-repayments"
