"""API client for managing performance resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_CYCLES_PATH = "/api/hr/review-cycles"
_REVIEWS_PATH = "/api/hr/performance-reviews"
_GOALS_PATH = "/api/hr/goals"


class PerformanceApi(BaseApi):
    """Performance management operations including review cycles, reviews, and goals."""

    # --- Review Cycles ---

    def create_cycle(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new review cycle."""
        return self._http.post(_CYCLES_PATH, request)

    def list_cycles(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List review cycles with pagination."""
        data = self._http.get(self._with_pagination(_CYCLES_PATH, page))
        return PageResponse.from_dict(data)

    # --- Reviews ---

    def create_review(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new performance review."""
        return self._http.post(_REVIEWS_PATH, request)

    def get_review(self, review_id: str) -> dict[str, Any]:
        """Retrieve a performance review by ID."""
        return self._http.get(f"{_REVIEWS_PATH}/{review_id}")

    def submit_review(self, review_id: str) -> dict[str, Any]:
        """Submit a performance review."""
        return self._http.put(f"{_REVIEWS_PATH}/{review_id}/submit")

    def acknowledge_review(self, review_id: str) -> dict[str, Any]:
        """Acknowledge a performance review."""
        return self._http.put(f"{_REVIEWS_PATH}/{review_id}/acknowledge")

    # --- Goals ---

    def create_goal(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new goal."""
        return self._http.post(_GOALS_PATH, request)

    def list_goals(self, employee_id: str, page: Optional[PageRequest] = None) -> PageResponse:
        """List goals for an employee with pagination."""
        path = self._with_pagination(f"{_GOALS_PATH}?employeeId={employee_id}", page)
        data = self._http.get(path)
        return PageResponse.from_dict(data)

    def update_progress(self, goal_id: str, progress: int) -> dict[str, Any]:
        """Update the progress of a goal."""
        return self._http.put(
            f"{_GOALS_PATH}/{goal_id}/progress",
            {"progress": progress},
        )
