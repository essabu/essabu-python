"""API for training in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class TrainingApi(BaseHrApi):
    """CRUD operations for training."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List training with pagination."""
        return self._list(self._path("training"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of training."""
        return self._list_all(self._path("training"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new training."""
        return self._create(self._path("training"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a training by ID."""
        return self._retrieve(self._path("training", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a training."""
        return self._update(self._path("training", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a training."""
        return self._delete(self._path("training", resource_id))
