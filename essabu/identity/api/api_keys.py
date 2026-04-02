"""API Keys API module."""

from typing import Any

from essabu.identity.api.base import CrudApi
from essabu.common.http_client import HttpClient
from essabu.identity.models.api_key import ApiKeyResponse


class ApiKeysApi(CrudApi):
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http, "/api-keys", ApiKeyResponse)

    def revoke(self, api_key_id: str) -> dict[str, Any]:
        return self._http.post(f"/api-keys/{api_key_id}/revoke")
