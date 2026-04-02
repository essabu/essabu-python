"""API for expenses in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class ExpenseApi(BaseHrApi):
    """CRUD operations for expenses."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List expenses with pagination."""
        return self._list(self._path("expenses"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of expenses."""
        return self._list_all(self._path("expenses"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new expense."""
        return self._create(self._path("expenses"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a expense by ID."""
        return self._retrieve(self._path("expenses", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a expense."""
        return self._update(self._path("expenses", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a expense."""
        return self._delete(self._path("expenses", resource_id))
