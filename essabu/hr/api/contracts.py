"""API client for managing contract resources."""

from __future__ import annotations

from typing import Any, Optional

from essabu.hr.api.base import BaseApi
from essabu.common.models import PageRequest, PageResponse

_BASE_PATH = "/api/hr/contracts"


class ContractApi(BaseApi):
    """Contract management operations.

    Base path: /api/hr/contracts
    """

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        """Create a new contract."""
        return self._http.post(_BASE_PATH, request)

    def get(self, contract_id: str) -> dict[str, Any]:
        """Retrieve a contract by ID."""
        return self._http.get(f"{_BASE_PATH}/{contract_id}")

    def list_by_employee(self, employee_id: str) -> list[dict[str, Any]]:
        """List contracts for a specific employee."""
        return self._http.get(self._with_param(_BASE_PATH, "employeeId", employee_id))

    def update(self, contract_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Update an existing contract."""
        return self._http.put(f"{_BASE_PATH}/{contract_id}", request)

    def renew(self, contract_id: str) -> dict[str, Any]:
        """Renew a contract."""
        return self._http.put(f"{_BASE_PATH}/{contract_id}/renew")

    def terminate(self, contract_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Terminate a contract."""
        return self._http.put(f"{_BASE_PATH}/{contract_id}/terminate", request)

    def create_amendment(self, contract_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Create a contract amendment."""
        return self._http.post(f"{_BASE_PATH}/{contract_id}/amendments", request)

    def get_expiring(self, within_days: int) -> PageResponse:
        """Get contracts expiring within a given number of days."""
        data = self._http.get(self._with_param(f"{_BASE_PATH}/expiring", "withinDays", within_days))
        return PageResponse.from_dict(data)
