"""API for journals in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class JournalApi(BaseAccountingApi):
    """CRUD operations for journals."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List journals with pagination."""
        return self._list(self._path("journals"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of journals."""
        return self._list_all(self._path("journals"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new journal."""
        return self._create(self._path("journals"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a journal by ID."""
        return self._retrieve(self._path("journals", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a journal."""
        return self._update(self._path("journals", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a journal."""
        return self._delete(self._path("journals", resource_id))
