"""API for statistics in the einvoice module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.einvoice.api.base import BaseEinvoiceApi


class StatisticApi(BaseEinvoiceApi):
    """CRUD operations for statistics."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List statistics with pagination."""
        return self._list(self._path("statistics"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of statistics."""
        return self._list_all(self._path("statistics"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new statistic."""
        return self._create(self._path("statistics"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a statistic by ID."""
        return self._retrieve(self._path("statistics", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a statistic."""
        return self._update(self._path("statistics", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a statistic."""
        return self._delete(self._path("statistics", resource_id))
