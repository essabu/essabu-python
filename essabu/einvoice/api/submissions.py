"""API for submissions in the einvoice module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.einvoice.api.base import BaseEinvoiceApi


class SubmissionApi(BaseEinvoiceApi):
    """CRUD operations for submissions."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List submissions with pagination."""
        return self._list(self._path("submissions"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of submissions."""
        return self._list_all(self._path("submissions"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new submission."""
        return self._create(self._path("submissions"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a submission by ID."""
        return self._retrieve(self._path("submissions", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a submission."""
        return self._update(self._path("submissions", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a submission."""
        return self._delete(self._path("submissions", resource_id))

    def submit(self, resource_id: str) -> dict[str, Any]:
        """Submit an e-invoice to the tax authority."""
        return self._http.post(self._path("submissions", resource_id, "submit"), json={})

    def check_status(self, resource_id: str) -> dict[str, Any]:
        """Check the submission status."""
        return self._retrieve(self._path("submissions", resource_id, "status"))
