"""API client for managing training resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/trainings"


class TrainingApi(BaseApi):
    """Training management operations.

    Base path: /api/hr/trainings
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new training."""
        return self._http.post(_BASE_PATH, request)

    def get(self, training_id: str) -> dict[str, Any]:
        """Retrieve a training by ID."""
        return self._http.get(f"{_BASE_PATH}/{training_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List trainings with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def update(self, training_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Update an existing training."""
        return self._http.put(f"{_BASE_PATH}/{training_id}", request)

    def delete(self, training_id: str) -> None:
        """Delete a training."""
        self._http.delete(f"{_BASE_PATH}/{training_id}")

    def get_expiring(self, within_days: int) -> list[dict[str, Any]]:
        """Get trainings expiring within a given number of days."""
        return self._http.get(f"{_BASE_PATH}/expiring?withinDays={within_days}")

    def compliance_report(self) -> list[dict[str, Any]]:
        """Get the training compliance report."""
        return self._http.get(f"{_BASE_PATH}/compliance-report")
