"""API for documents in the trade module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class DocumentApi(BaseTradeApi):
    """CRUD operations for documents."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List documents with pagination."""
        return self._list(self._path("documents"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of documents."""
        return self._list_all(self._path("documents"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new document."""
        return self._create(self._path("documents"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a document by ID."""
        return self._retrieve(self._path("documents", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a document."""
        return self._update(self._path("documents", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a document."""
        return self._delete(self._path("documents", resource_id))
