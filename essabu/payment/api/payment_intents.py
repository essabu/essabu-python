"""API client for payment intents operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class PaymentIntentsApi(BaseApi):
    """API client for payment intents operations."""

    _resource_path = "/payment-intents"
