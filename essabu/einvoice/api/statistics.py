"""Statistics API module."""

from typing import Any

from essabu.common.http_client import HttpClient
from essabu.einvoice.models.statistics import (
    StatisticsRequest,
    StatisticsResponse,
)


class StatisticsApi:
    """Synchronous statistics API."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def get(self, params: dict[str, Any] | StatisticsRequest | None = None) -> StatisticsResponse:
        """Get statistics."""
        query_params = None
        if params:
            query_params = params.model_dump(exclude_none=True) if isinstance(params, StatisticsRequest) else params
        response = self._http.get("/statistics", params=query_params)
        return StatisticsResponse(**response)

