"""Abstract base class shared by all API clients in the Essabu HR module."""

from __future__ import annotations

from typing import Any

from essabu.common.http_client import HttpClient
from essabu.common.models import PageRequest


class BaseApi:
    """Provides common functionality for all HR API modules."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    @staticmethod
    def _with_pagination(base_path: str, page: PageRequest | None) -> str:
        """Append pagination query parameters to a base path."""
        if page is None:
            return base_path
        separator = "&" if "?" in base_path else "?"
        return f"{base_path}{separator}{page.to_query_string()}"

    @staticmethod
    def _with_param(base_path: str, key: str, value: Any) -> str:
        """Append a single query parameter to a base path."""
        if value is None:
            return base_path
        separator = "&" if "?" in base_path else "?"
        return f"{base_path}{separator}{key}={value}"
