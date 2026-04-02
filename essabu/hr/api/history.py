"""API client for managing history / audit log resources."""

from __future__ import annotations

from typing import Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/history"


class HistoryApi(BaseApi):
    """History / audit log management operations.

    Base path: /api/hr/history
    """

    def list_by_employee(self, employee_id: str, page: Optional[PageRequest] = None) -> PageResponse:
        """List audit log entries for a specific employee."""
        path = self._with_pagination(f"{_BASE_PATH}?employeeId={employee_id}", page)
        data = self._http.get(path)
        return PageResponse.from_dict(data)

    def list_by_entity_type(self, entity_type: str, page: Optional[PageRequest] = None) -> PageResponse:
        """List audit log entries for a specific entity type."""
        path = self._with_pagination(f"{_BASE_PATH}?entityType={entity_type}", page)
        data = self._http.get(path)
        return PageResponse.from_dict(data)
