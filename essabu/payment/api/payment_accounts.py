"""API client for payment accounts operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class PaymentAccountsApi(BaseApi):
    """API client for payment accounts operations."""

    _resource_path = "/payment-accounts"
