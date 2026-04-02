"""API client for subscriptions operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class SubscriptionsApi(BaseApi):
    """API client for subscriptions operations."""

    _resource_path = "/subscriptions"
