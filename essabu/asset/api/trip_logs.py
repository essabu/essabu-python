"""API for trip logs in the asset module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.asset.api.base import BaseAssetApi


class TripLogApi(BaseAssetApi):
    """CRUD operations for trip logs."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List trip logs with pagination."""
        return self._list(self._path("trip_logs"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of trip logs."""
        return self._list_all(self._path("trip_logs"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new trip log."""
        return self._create(self._path("trip_logs"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a trip log by ID."""
        return self._retrieve(self._path("trip_logs", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a trip log."""
        return self._update(self._path("trip_logs", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a trip log."""
        return self._delete(self._path("trip_logs", resource_id))
