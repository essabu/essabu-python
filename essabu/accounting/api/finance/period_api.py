"""API for periods in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class PeriodApi(BaseAccountingApi):
    """CRUD operations for periods."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List periods with pagination."""
        return self._list(self._path("periods"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of periods."""
        return self._list_all(self._path("periods"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new period."""
        return self._create(self._path("periods"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a period by ID."""
        return self._retrieve(self._path("periods", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a period."""
        return self._update(self._path("periods", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a period."""
        return self._delete(self._path("periods", resource_id))
