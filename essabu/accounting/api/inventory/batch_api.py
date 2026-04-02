"""API for batches in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class BatchApi(BaseAccountingApi):
    """CRUD operations for batches."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List batches with pagination."""
        return self._list(self._path("batches"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of batches."""
        return self._list_all(self._path("batches"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new batch."""
        return self._create(self._path("batches"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a batch by ID."""
        return self._retrieve(self._path("batches", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a batch."""
        return self._update(self._path("batches", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a batch."""
        return self._delete(self._path("batches", resource_id))
