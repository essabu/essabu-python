"""API for journal entries in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class JournalEntryApi(BaseAccountingApi):
    """CRUD operations for journal entries."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List journal entries with pagination."""
        return self._list(self._path("journal_entries"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of journal entries."""
        return self._list_all(self._path("journal_entries"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new journal entry."""
        return self._create(self._path("journal_entries"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a journal entry by ID."""
        return self._retrieve(self._path("journal_entries", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a journal entry."""
        return self._update(self._path("journal_entries", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a journal entry."""
        return self._delete(self._path("journal_entries", resource_id))
