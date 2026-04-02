"""API client for managing config resources."""

from __future__ import annotations

from typing import Any

from essabu.hr.api.base import BaseApi

_BASE_PATH = "/api/hr/config"


class ConfigApi(BaseApi):
    """Configuration management operations.

    Base path: /api/hr/config
    """

    def get_config(self) -> dict[str, Any]:
        """Get the tenant configuration."""
        return self._http.get(_BASE_PATH)

    def update_config(self, request: dict[str, Any]) -> dict[str, Any]:
        """Update the tenant configuration."""
        return self._http.put(_BASE_PATH, request)

    def get_leave_policies(self) -> list[dict[str, Any]]:
        """Get all leave policies."""
        return self._http.get(f"{_BASE_PATH}/leave-policies")

    def update_leave_policy(self, policy_id: str, request: dict[str, Any]) -> dict[str, Any]:
        """Update a leave policy."""
        return self._http.put(f"{_BASE_PATH}/leave-policies/{policy_id}", request)

    def get_payroll_rules(self) -> list[dict[str, Any]]:
        """Get all payroll rules."""
        return self._http.get(f"{_BASE_PATH}/payroll-rules")

    def get_holidays(self) -> list[dict[str, Any]]:
        """Get all public holidays."""
        return self._http.get(f"{_BASE_PATH}/holidays")

    def add_holiday(self, request: dict[str, Any]) -> dict[str, Any]:
        """Add a public holiday."""
        return self._http.post(f"{_BASE_PATH}/holidays", request)
