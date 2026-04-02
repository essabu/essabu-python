"""API for reports in the accounting module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.accounting.api.base import BaseAccountingApi
from essabu.common.models import PageResponse


class ReportApi(BaseAccountingApi):
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

    def balance_sheet(self, **params: Any) -> dict[str, Any]:
        """Get balance sheet report."""
        return self._http.get(self._path("reports", "balance-sheet"), params=params or None)

    def income_statement(self, **params: Any) -> dict[str, Any]:
        """Get income statement report."""
        return self._http.get(self._path("reports", "income-statement"), params=params or None)

    def trial_balance(self, **params: Any) -> dict[str, Any]:
        """Get trial balance report."""
        return self._http.get(self._path("reports", "trial-balance"), params=params or None)

    def cash_flow(self, **params: Any) -> dict[str, Any]:
        """Get cash flow report."""
        return self._http.get(self._path("reports", "cash-flow"), params=params or None)
