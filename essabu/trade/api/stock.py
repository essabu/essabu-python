"""API client for stock operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class StockApi(BaseApi):
    """API client for stock operations."""

    _resource_path = "/stock"
