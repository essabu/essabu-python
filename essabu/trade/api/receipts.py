"""API client for receipts operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class ReceiptsApi(BaseApi):
    """API client for receipts operations."""

    _resource_path = "/receipts"
