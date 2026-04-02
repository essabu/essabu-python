"""API client for documents operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class DocumentsApi(BaseApi):
    """API client for documents operations."""

    _resource_path = "/documents"
