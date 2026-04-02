"""Base CRUD API class for the Identity module."""

from __future__ import annotations

from typing import Any, TypeVar, Type

from pydantic import BaseModel

from essabu.common.http_client import HttpClient
from essabu.identity.models.common import PaginatedResponse

T = TypeVar("T", bound=BaseModel)


class CrudApi:
    """Base class for CRUD API modules."""

    def __init__(self, http: HttpClient, base_path: str, model: Type[T]) -> None:
        self._http = http
        self._base_path = base_path
        self._model = model

    def list(self, page: int = 1, per_page: int = 25, **filters: Any) -> PaginatedResponse:
        params: dict[str, Any] = {"page": page, "per_page": per_page, **filters}
        response = self._http.get(self._base_path, params=params)
        return PaginatedResponse(**response)

    def get(self, resource_id: str) -> BaseModel:
        response = self._http.get(f"{self._base_path}/{resource_id}")
        return self._model(**response)

    def create(self, data: dict[str, Any]) -> BaseModel:
        response = self._http.post(self._base_path, data=data)
        return self._model(**response)

    def update(self, resource_id: str, data: dict[str, Any]) -> BaseModel:
        response = self._http.patch(f"{self._base_path}/{resource_id}", data=data)
        return self._model(**response)

    def delete(self, resource_id: str) -> dict[str, Any]:
        return self._http.delete(f"{self._base_path}/{resource_id}")
