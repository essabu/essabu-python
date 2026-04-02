"""Depreciations API."""

from __future__ import annotations

from typing import Any

from essabu.asset.api.base import BaseApi
from essabu.asset.models.depreciation import Depreciation
from essabu.asset.models.pagination import PaginatedResponse


class DepreciationsApi(BaseApi):
    """API operations for asset depreciations."""

    def list(
        self, asset_id: str, params: dict[str, Any] | None = None
    ) -> PaginatedResponse:
        """List depreciations for an asset."""
        data = self._http.get(f"/assets/{asset_id}/depreciations", params=params)
        return PaginatedResponse(**data)

    def get(self, asset_id: str, depreciation_id: str) -> Depreciation:
        """Get a depreciation record by ID."""
        data = self._http.get(f"/assets/{asset_id}/depreciations/{depreciation_id}")
        return Depreciation(**data)

    def create(self, asset_id: str, payload: dict[str, Any]) -> Depreciation:
        """Create a new depreciation record."""
        data = self._http.post(f"/assets/{asset_id}/depreciations", data=payload)
        return Depreciation(**data)

    def update(
        self, asset_id: str, depreciation_id: str, payload: dict[str, Any]
    ) -> Depreciation:
        """Update a depreciation record."""
        data = self._http.patch(
            f"/assets/{asset_id}/depreciations/{depreciation_id}", data=payload
        )
        return Depreciation(**data)

    def delete(self, asset_id: str, depreciation_id: str) -> None:
        """Delete a depreciation record."""
        self._http.delete(f"/assets/{asset_id}/depreciations/{depreciation_id}")
