"""API for compliance in the einvoice module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.models import PageResponse
from essabu.einvoice.api.base import BaseEinvoiceApi


class ComplianceApi(BaseEinvoiceApi):
    """CRUD operations for compliance."""

    def list(self, *, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse:
        """List compliance with pagination."""
        return self._list(self._path("compliance"), page=page, page_size=page_size, params=filters or None)

    def list_all(self, *, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]:
        """Iterate over all pages of compliance."""
        return self._list_all(self._path("compliance"), page_size=page_size, params=filters or None)

    def create(self, **data: Any) -> dict[str, Any]:
        """Create a new compliance."""
        return self._create(self._path("compliance"), data)

    def retrieve(self, resource_id: str) -> dict[str, Any]:
        """Retrieve a compliance by ID."""
        return self._retrieve(self._path("compliance", resource_id))

    def update(self, resource_id: str, **data: Any) -> dict[str, Any]:
        """Update a compliance."""
        return self._update(self._path("compliance", resource_id), data)

    def delete(self, resource_id: str) -> dict[str, Any]:
        """Delete a compliance."""
        return self._delete(self._path("compliance", resource_id))
