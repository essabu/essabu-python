"""Sessions API module."""

from typing import Any

from essabu.common.http_client import HttpClient
from essabu.identity.models.common import PaginatedResponse
from essabu.identity.models.session import SessionResponse


class SessionsApi:
    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def list(self, page: int = 1, per_page: int = 25) -> PaginatedResponse:
        response = self._http.get("/sessions", params={"page": page, "per_page": per_page})
        return PaginatedResponse(**response)

    def get(self, session_id: str) -> SessionResponse:
        response = self._http.get(f"/sessions/{session_id}")
        return SessionResponse(**response)

    def revoke(self, session_id: str) -> dict[str, Any]:
        return self._http.delete(f"/sessions/{session_id}")

    def revoke_all(self) -> dict[str, Any]:
        return self._http.post("/sessions/revoke-all")
