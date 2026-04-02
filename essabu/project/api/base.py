"""Base API class for the Project module."""

from __future__ import annotations

from essabu.common.http_client import HttpClient


class BaseApi:
    """Base class for all Project API resource classes."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
