"""API client for financial accounts operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class FinancialAccountsApi(BaseApi):
    """API client for financial accounts operations."""

    _resource_path = "/financial-accounts"
