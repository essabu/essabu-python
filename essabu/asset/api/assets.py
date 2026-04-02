"""Assets API."""

from __future__ import annotations

from typing import Any

from essabu.asset.api.base import BaseApi
from essabu.asset.models.asset import Asset
from essabu.asset.models.pagination import PaginatedResponse


class AssetsApi(BaseApi):
    """API operations for assets."""

    def list(self, params: dict[str, Any] | None = None) -> PaginatedResponse:
        """List all assets."""
        data = self._http.get("/assets", params=params)
        return PaginatedResponse(**data)

    def get(self, asset_id: str) -> Asset:
        """Get an asset by ID."""
        data = self._http.get(f"/assets/{asset_id}")
        return Asset(**data)

    def create(self, payload: dict[str, Any]) -> Asset:
        """Create a new asset."""
        data = self._http.post("/assets", data=payload)
        return Asset(**data)

    def update(self, asset_id: str, payload: dict[str, Any]) -> Asset:
        """Update an existing asset."""
        data = self._http.patch(f"/assets/{asset_id}", data=payload)
        return Asset(**data)

    def delete(self, asset_id: str) -> None:
        """Delete an asset."""
        self._http.delete(f"/assets/{asset_id}")
