"""API for activities in the trade module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class ActivityApi(BaseTradeApi):
    """CRUD operations for activities."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List activities with pagination."""
        return self._list(self._path("activities"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of activities."""
        return self._list_all(self._path("activities"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new activity."""
        return self._create(self._path("activities"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a activity by ID."""
        return self._retrieve(self._path("activities", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a activity."""
        return self._update(self._path("activities", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a activity."""
        return self._delete(self._path("activities", resource_id))
