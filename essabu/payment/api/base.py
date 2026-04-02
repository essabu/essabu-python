"""Base API class with common CRUD operations for Payment module."""

from __future__ import annotations

from typing import Any

from essabu.common.http_client import HttpClient


class BaseApi:
    """Base class for all Payment API resource classes."""

    _resource_path: str = ""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, params: dict[str, Any] | None = None) -> dict[str, Any]:
        return self._http.get(self._resource_path, params=params)

    def get(self, resource_id: str) -> dict[str, Any]:
        return self._http.get(f"{self._resource_path}/{resource_id}")

    def create(self, data: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(self._resource_path, data=data)

    def update(self, resource_id: str, data: dict[str, Any]) -> dict[str, Any]:
        return self._http.patch(f"{self._resource_path}/{resource_id}", data=data)

    def delete(self, resource_id: str) -> None:
        self._http.delete(f"{self._resource_path}/{resource_id}")
