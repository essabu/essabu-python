"""Abstract base class shared by all API clients in the Essabu Accounting module."""

from __future__ import annotations

from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest


class BaseApi:
    """Abstract base class shared by all Accounting API clients."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def _with_pagination(self, base_path: str, page: PageRequest | None) -> str:
        if page is None:
            return base_path
        separator = "&" if "?" in base_path else "?"
        return base_path + separator + page.to_query_string()

    def _with_param(self, base_path: str, key: str, value: object | None) -> str:
        if value is None:
            return base_path
        separator = "&" if "?" in base_path else "?"
        return f"{base_path}{separator}{key}={value}"
