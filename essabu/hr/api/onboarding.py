"""API for onboarding in the hr module."""

from __future__ import annotations

from typing import Any, Generator

from essabu.common.models import PageResponse
from essabu.hr.api.base import BaseHrApi


class OnboardingApi(BaseHrApi):
    """CRUD operations for onboarding."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List onboarding with pagination."""
        return self._list(self._path("onboarding"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of onboarding."""
        return self._list_all(self._path("onboarding"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new onboarding."""
        return self._create(self._path("onboarding"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a onboarding by ID."""
        return self._retrieve(self._path("onboarding", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a onboarding."""
        return self._update(self._path("onboarding", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a onboarding."""
        return self._delete(self._path("onboarding", resource_id))
