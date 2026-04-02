"""API for reports in the project module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.project.api.base import BaseProjectApi


class ReportApi(BaseProjectApi):
    """CRUD operations for reports."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List reports with pagination."""
        return self._list(self._path("reports"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of reports."""
        return self._list_all(self._path("reports"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new report."""
        return self._create(self._path("reports"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a report by ID."""
        return self._retrieve(self._path("reports", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a report."""
        return self._update(self._path("reports", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a report."""
        return self._delete(self._path("reports", resource_id))
