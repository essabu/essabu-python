"""API client for transactions operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class TransactionsApi(BaseApi):
    """API client for transactions operations."""

    _resource_path = "/transactions"
