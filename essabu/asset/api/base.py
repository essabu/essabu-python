"""Base API class for the Asset module."""

from __future__ import annotations

from essabu.common.http_client import HttpClient


class BaseApi:
    """Base class for all Asset API resource classes."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
