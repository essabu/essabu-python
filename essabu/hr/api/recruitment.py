"""API client for managing recruitment resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_JOBS_PATH = "/api/hr/job-postings"
_APPS_PATH = "/api/hr/applications"
_INTERVIEWS_PATH = "/api/hr/interviews"


class RecruitmentApi(BaseApi):
    """Recruitment management operations including job postings, applications, and interviews."""

    # --- Job Postings ---

    def create_job_posting(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new job posting."""
        return self._http.post(_JOBS_PATH, request)

    def get_job_posting(self, posting_id: str) -> dict[str, Any]:
        """Retrieve a job posting by ID."""
        return self._http.get(f"{_JOBS_PATH}/{posting_id}")

    def list_job_postings(self, page: Optional[PageRequest] = None) -> PageResponse:
        """List job postings with pagination."""
        data = self._http.get(self._with_pagination(_JOBS_PATH, page))
        return PageResponse.from_dict(data)

    def publish_job_posting(self, posting_id: str) -> dict[str, Any]:
        """Publish a job posting."""
        return self._http.put(f"{_JOBS_PATH}/{posting_id}/publish")

    def close_job_posting(self, posting_id: str) -> dict[str, Any]:
        """Close a job posting."""
        return self._http.put(f"{_JOBS_PATH}/{posting_id}/close")

    # --- Applications ---

    def create_application(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new application."""
        return self._http.post(_APPS_PATH, request)

    def get_application(self, application_id: str) -> dict[str, Any]:
        """Retrieve an application by ID."""
        return self._http.get(f"{_APPS_PATH}/{application_id}")

    def list_applications(
        self, job_posting_id: str, page: Optional[PageRequest] = None
    ) -> PageResponse:
        """List applications for a job posting with pagination."""
        path = self._with_pagination(
            f"{_APPS_PATH}?jobPostingId={job_posting_id}", page
        )
        data = self._http.get(path)
        return PageResponse.from_dict(data)

    def advance_application(self, application_id: str) -> dict[str, Any]:
        """Advance an application to the next stage."""
        return self._http.put(f"{_APPS_PATH}/{application_id}/advance")

    def reject_application(self, application_id: str) -> dict[str, Any]:
        """Reject an application."""
        return self._http.put(f"{_APPS_PATH}/{application_id}/reject")

    def hire_application(self, application_id: str) -> dict[str, Any]:
        """Hire an applicant (creates an employee)."""
        return self._http.put(f"{_APPS_PATH}/{application_id}/hire")

    # --- Interviews ---

    def schedule_interview(self, request: dict[str, Any]) -> dict[str, Any]:
        """Schedule a new interview."""
        return self._http.post(_INTERVIEWS_PATH, request)

    def get_interview(self, interview_id: str) -> dict[str, Any]:
        """Retrieve an interview by ID."""
        return self._http.get(f"{_INTERVIEWS_PATH}/{interview_id}")

    def complete_interview(self, interview_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Complete an interview with feedback."""
        return self._http.put(f"{_INTERVIEWS_PATH}/{interview_id}/complete", request)
