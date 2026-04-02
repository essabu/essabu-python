"""API for loans in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class LoanApi(BaseHrApi):
    """CRUD operations for loans."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List loans with pagination."""
        return self._list(self._path("loans"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of loans."""
        return self._list_all(self._path("loans"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new loan."""
        return self._create(self._path("loans"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a loan by ID."""
        return self._retrieve(self._path("loans", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a loan."""
        return self._update(self._path("loans", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a loan."""
        return self._delete(self._path("loans", resource_id))
