"""API for sessions in the identity module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.identity.api.base import BaseIdentityApi


class SessionApi(BaseIdentityApi):
    """CRUD operations for sessions."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List sessions with pagination."""
        return self._list(self._path("sessions"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of sessions."""
        return self._list_all(self._path("sessions"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new session."""
        return self._create(self._path("sessions"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a session by ID."""
        return self._retrieve(self._path("sessions", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a session."""
        return self._update(self._path("sessions", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a session."""
        return self._delete(self._path("sessions", resource_id))
