"""API for depreciations in the asset module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.asset.api.base import BaseAssetApi
from essabu.common.models import PageResponse


class DepreciationApi(BaseAssetApi):
    """CRUD operations for depreciations."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List depreciations with pagination."""
        return self._list(self._path("depreciations"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of depreciations."""
        return self._list_all(self._path("depreciations"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new depreciation."""
        return self._create(self._path("depreciations"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a depreciation by ID."""
        return self._retrieve(self._path("depreciations", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a depreciation."""
        return self._update(self._path("depreciations", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a depreciation."""
        return self._delete(self._path("depreciations", resource_id))
