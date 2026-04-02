"""API for vehicles in the asset module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.asset.api.base import BaseAssetApi


class VehicleApi(BaseAssetApi):
    """CRUD operations for vehicles."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List vehicles with pagination."""
        return self._list(self._path("vehicles"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of vehicles."""
        return self._list_all(self._path("vehicles"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new vehicle."""
        return self._create(self._path("vehicles"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a vehicle by ID."""
        return self._retrieve(self._path("vehicles", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a vehicle."""
        return self._update(self._path("vehicles", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a vehicle."""
        return self._delete(self._path("vehicles", resource_id))
