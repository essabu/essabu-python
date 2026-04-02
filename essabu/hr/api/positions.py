"""API client for managing position resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/positions"


class PositionApi(BaseApi):
    """Position management operations.

    Base path: /api/hr/positions
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new position."""
        return self._http.post(_BASE_PATH, request)

    def get(self, position_id: str) -> dict[str, Any]:
        """Retrieve a position by ID."""
        return self._http.get(f"{_BASE_PATH}/{position_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List positions with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def update(self, position_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Update an existing position."""
        return self._http.put(f"{_BASE_PATH}/{position_id}", request)

    def delete(self, position_id: str) -> None:
        """Delete a position."""
        self._http.delete(f"{_BASE_PATH}/{position_id}")
