"""API for payroll in the hr module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class PayrollApi(BaseHrApi):
    """CRUD operations for payroll."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List payroll with pagination."""
        return self._list(self._path("payroll"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of payroll."""
        return self._list_all(self._path("payroll"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new payroll."""
        return self._create(self._path("payroll"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a payroll by ID."""
        return self._retrieve(self._path("payroll", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a payroll."""
        return self._update(self._path("payroll", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a payroll."""
        return self._delete(self._path("payroll", resource_id))
