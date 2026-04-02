"""API client for deliveries operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class DeliveriesApi(BaseApi):
    """API client for deliveries operations."""

    _resource_path = "/deliveries"
