"""API client for suppliers operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class SuppliersApi(BaseApi):
    """API client for suppliers operations."""

    _resource_path = "/suppliers"
