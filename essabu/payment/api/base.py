"""Base API class for the payment module."""

from __future__ import annotations

from collections.abc import Generator
from typing import Any

from essabu.common.http_client import HttpClient
from essabu.common.models import PageResponse


class BasePaymentApi:
    """Base class for payment API resources."""

    _base_path: str = "/api/payment"

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def _path(self, *parts: str) -> str:
        return "/".join([self._base_path, *parts])

    def _list(
        self,
        path: str,
        *,
        page: int = 1,
        page_size: int = 25,
        params: dict[str, Any] | None = None,
    ) -> PageResponse:
        p = {"page": page, "pageSize": page_size}
        if params:
            p.update(params)
        return self._http.get_paginated(path, params=p)

    def _list_all(
        self,
        path: str,
        *,
        page_size: int = 25,
        params: dict[str, Any] | None = None,
    ) -> Generator[PageResponse, None, None]:
        return self._http.iter_pages(path, page_size=page_size, params=params)

    def _retrieve(self, path: str) -> dict[str, Any]:
        return self._http.get(path)

    def _create(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        return self._http.post(path, json=data)

    def _update(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        return self._http.patch(path, json=data)

    def _replace(self, path: str, data: dict[str, Any]) -> dict[str, Any]:
        return self._http.put(path, json=data)

    def _delete(self, path: str) -> dict[str, Any]:
        return self._http.delete(path)
