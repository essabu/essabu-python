"""API client for warehouses operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class WarehousesApi(BaseApi):
    """API client for warehouses operations."""

    _resource_path = "/warehouses"
