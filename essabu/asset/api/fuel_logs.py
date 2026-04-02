"""API for fuel logs in the asset module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.asset.api.base import BaseAssetApi


class FuelLogApi(BaseAssetApi):
    """CRUD operations for fuel logs."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List fuel logs with pagination."""
        return self._list(self._path("fuel_logs"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of fuel logs."""
        return self._list_all(self._path("fuel_logs"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new fuel log."""
        return self._create(self._path("fuel_logs"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a fuel log by ID."""
        return self._retrieve(self._path("fuel_logs", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a fuel log."""
        return self._update(self._path("fuel_logs", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a fuel log."""
        return self._delete(self._path("fuel_logs", resource_id))
