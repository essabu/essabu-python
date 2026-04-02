"""API client for managing wallet resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class WalletApi(BaseApi):
    """API client for managing wallet resources. Base path: /api/accounting/wallets"""
    BASE_PATH = "/api/accounting/wallets"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, wallet_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{wallet_id}")
    def list(self, company_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?companyId={company_id}", page)
        return self._http.get(path)
    def update(self, wallet_id: str, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(f"{self.BASE_PATH}/{wallet_id}", request)
    def delete(self, wallet_id: str) -> None:
        self._http.delete(f"{self.BASE_PATH}/{wallet_id}")
    def freeze(self, wallet_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{wallet_id}/freeze")
    def unfreeze(self, wallet_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{wallet_id}/unfreeze")
    def close(self, wallet_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{wallet_id}/close")
