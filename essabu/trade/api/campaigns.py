"""API for campaigns in the trade module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.trade.api.base import BaseTradeApi


class CampaignApi(BaseTradeApi):
    """CRUD operations for campaigns."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List campaigns with pagination."""
        return self._list(self._path("campaigns"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of campaigns."""
        return self._list_all(self._path("campaigns"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new campaign."""
        return self._create(self._path("campaigns"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a campaign by ID."""
        return self._retrieve(self._path("campaigns", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a campaign."""
        return self._update(self._path("campaigns", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a campaign."""
        return self._delete(self._path("campaigns", resource_id))
