"""API client for inventory operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class InventoryApi(BaseApi):
    """API client for inventory operations."""

    _resource_path = "/inventory"
