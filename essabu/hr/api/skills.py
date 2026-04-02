"""API for skills in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class SkillApi(BaseHrApi):
    """CRUD operations for skills."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List skills with pagination."""
        return self._list(self._path("skills"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of skills."""
        return self._list_all(self._path("skills"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new skill."""
        return self._create(self._path("skills"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a skill by ID."""
        return self._retrieve(self._path("skills", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a skill."""
        return self._update(self._path("skills", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a skill."""
        return self._delete(self._path("skills", resource_id))
