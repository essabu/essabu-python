"""API client for managing wallet transaction resources."""
from __future__ import annotations
from typing import Any
from essabu.accounting.api.base_api import BaseApi
from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest

class WalletTransactionApi(BaseApi):
    """API client for managing wallet transaction resources. Base path: /api/accounting/wallet-transactions"""
    BASE_PATH = "/api/accounting/wallet-transactions"
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http)
    def create(self, request: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self.BASE_PATH, request)
    def get(self, transaction_id: str) -> dict[str, Any]:
        return self._http.get(f"{self.BASE_PATH}/{transaction_id}")
    def list(self, wallet_id: str, page: PageRequest | None = None) -> dict[str, Any]:
        path = self._with_pagination(f"{self.BASE_PATH}?walletId={wallet_id}", page)
        return self._http.get(path)
    def confirm(self, transaction_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{transaction_id}/confirm")
    def cancel(self, transaction_id: str) -> dict[str, Any]:
        return self._http.post_empty(f"{self.BASE_PATH}/{transaction_id}/cancel")
