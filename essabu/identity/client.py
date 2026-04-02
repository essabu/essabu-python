"""Identity module client for the Essabu SDK."""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.identity.api.api_keys import ApiKeysApi
from essabu.identity.api.auth import AuthApi
from essabu.identity.api.branches import BranchesApi
from essabu.identity.api.companies import CompaniesApi
from essabu.identity.api.permissions import PermissionsApi
from essabu.identity.api.profiles import ProfilesApi
from essabu.identity.api.roles import RolesApi
from essabu.identity.api.sessions import SessionsApi
from essabu.identity.api.tenants import TenantsApi
from essabu.identity.api.users import UsersApi


class IdentityClient:
    """Identity module client providing access to all Identity API resources."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    def set_token(self, token: str) -> None:
        """Update the bearer token for subsequent requests."""
        self._http.set_token(token)

    @cached_property
    def auth(self) -> AuthApi:
        return AuthApi(self._http)

    @cached_property
    def users(self) -> UsersApi:
        return UsersApi(self._http)

    @cached_property
    def profiles(self) -> ProfilesApi:
        return ProfilesApi(self._http)

    @cached_property
    def companies(self) -> CompaniesApi:
        return CompaniesApi(self._http)

    @cached_property
    def tenants(self) -> TenantsApi:
        return TenantsApi(self._http)

    @cached_property
    def roles(self) -> RolesApi:
        return RolesApi(self._http)

    @cached_property
    def permissions(self) -> PermissionsApi:
        return PermissionsApi(self._http)

    @cached_property
    def branches(self) -> BranchesApi:
        return BranchesApi(self._http)

    @cached_property
    def api_keys(self) -> ApiKeysApi:
        return ApiKeysApi(self._http)

    @cached_property
    def sessions(self) -> SessionsApi:
        return SessionsApi(self._http)
