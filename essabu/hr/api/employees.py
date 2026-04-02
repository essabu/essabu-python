"""API for employees in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class EmployeeApi(BaseHrApi):
    """CRUD operations for employees."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List employees with pagination."""
        return self._list(self._path("employees"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of employees."""
        return self._list_all(self._path("employees"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new employee."""
        return self._create(self._path("employees"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a employee by ID."""
        return self._retrieve(self._path("employees", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a employee."""
        return self._update(self._path("employees", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a employee."""
        return self._delete(self._path("employees", resource_id))
