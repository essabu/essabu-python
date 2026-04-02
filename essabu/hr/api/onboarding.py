"""API client for managing onboarding resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/onboarding-plans"


class OnboardingApi(BaseApi):
    """Onboarding management operations.

    Base path: /api/hr/onboarding-plans
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new onboarding plan."""
        return self._http.post(_BASE_PATH, request)

    def get(self, plan_id: str) -> dict[str, Any]:
        """Retrieve an onboarding plan by ID."""
        return self._http.get(f"{_BASE_PATH}/{plan_id}")

    def list(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List onboarding plans with pagination."""
        data = self._http.get(self._with_pagination(_BASE_PATH, page))
        return PageResponse.from_dict(data)

    def complete_task(self, task_id: str) -> dict[str, Any]:
        """Complete an onboarding task."""
        return self._http.put(f"/api/hr/onboarding-tasks/{task_id}/complete")

    def get_progress(self, plan_id: str) -> int:
        """Get the progress percentage of an onboarding plan."""
        return self._http.get(f"{_BASE_PATH}/{plan_id}/progress")
