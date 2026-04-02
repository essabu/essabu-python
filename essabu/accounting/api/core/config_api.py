"""API client for managing accounting configuration resources."""

from __future__ import annotations

from typing import Any

from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient


class ConfigApi(BaseApi):
    """API client for managing accounting configuration.

    Base path: /api/accounting/config
    """

    BASE_PATH = "/api/accounting/config"

    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)

    def get(self, company_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}?companyId={company_id}")

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)

    def update(self, config_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{config_id}", request)
