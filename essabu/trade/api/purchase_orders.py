"""API client for purchase orders operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class PurchaseOrdersApi(BaseApi):
    """API client for purchase orders operations."""

    _resource_path = "/purchase-orders"
