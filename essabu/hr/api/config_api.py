"""API for config in the hr module."""

from __future__ import annotations

from typing import Any

from essabu.hr.api.base import BaseHrApi


class ConfigApi(BaseHrApi):
    """Operations for config."""

    def get_settings(self, **params: Any) -> dict[str, Any]:
        """Get HR module settings."""
        return self._http.get(self._path("config", "settings"), params=params or None)

    def update_settings(self, **data: Any) -> dict[str, Any]:
        """Update HR module settings."""
        return self._http.post(self._path("config", "settings"), json=data)

    def get_leave_types(self, **params: Any) -> dict[str, Any]:
        """Get leave type configuration."""
        return self._http.get(self._path("config", "leave-types"), params=params or None)

    def get_pay_grades(self, **params: Any) -> dict[str, Any]:
        """Get pay grade configuration."""
        return self._http.get(self._path("config", "pay-grades"), params=params or None)
