"""Profiles API module."""

from essabu.identity.api.base import CrudApi
from essabu.common.http_client import HttpClient
from essabu.identity.models.profile import ProfileResponse


class ProfilesApi(CrudApi):
    def __init__(self, http: HttpClient) -> None:
        super().__init__(http, "/profiles", ProfileResponse)
