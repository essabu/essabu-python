"""API for balances in the accounting module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.accounting.api.base import BaseAccountingApi


class BalanceApi(BaseAccountingApi):
    """CRUD operations for balances."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List balances with pagination."""
        return self._list(self._path("balances"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of balances."""
        return self._list_all(self._path("balances"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new balance."""
        return self._create(self._path("balances"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a balance by ID."""
        return self._retrieve(self._path("balances", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a balance."""
        return self._update(self._path("balances", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a balance."""
        return self._delete(self._path("balances", resource_id))
