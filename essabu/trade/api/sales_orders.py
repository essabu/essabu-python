"""API client for sales orders operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class SalesOrdersApi(BaseApi):
    """API client for sales orders operations."""

    _resource_path = "/sales-orders"
