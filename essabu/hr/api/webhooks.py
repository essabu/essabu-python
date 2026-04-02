"""API for webhooks in the hr module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class WebhookApi(BaseHrApi):
    """CRUD operations for webhooks."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List webhooks with pagination."""
        return self._list(self._path("webhooks"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of webhooks."""
        return self._list_all(self._path("webhooks"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new webhook."""
        return self._create(self._path("webhooks"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a webhook by ID."""
        return self._retrieve(self._path("webhooks", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a webhook."""
        return self._update(self._path("webhooks", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a webhook."""
        return self._delete(self._path("webhooks", resource_id))
