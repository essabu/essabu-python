"""API client for managing account resources."""

from __future__ import annotations

from typing import Any

from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest


class AccountApi(BaseApi):
    """API client for managing account resources.

    Base path: /api/accounting/accounts
    """

    BASE_PATH = "/api/accounting/accounts"

    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)

    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)

    def get(self, account_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{account_id}")

    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)

    def update(self, account_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{account_id}", request)

    def deactivate(self, account_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{account_id}/deactivate")

    def initialize_chart(self, company_id: str) -> None:
        self._http.post_empty(f"{self.BASE_PATH}/initialize-chart?companyId={company_id}")
