"""Identity module client."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient

if TYPE_CHECKING:
    from essabu.identity.api.api_keys import ApiKeyApi
    from essabu.identity.api.auth import AuthApi
    from essabu.identity.api.branches import BranchApi
    from essabu.identity.api.companies import CompanyApi
    from essabu.identity.api.permissions import PermissionApi
    from essabu.identity.api.profiles import ProfileApi
    from essabu.identity.api.roles import RoleApi
    from essabu.identity.api.sessions import SessionApi
    from essabu.identity.api.tenants import TenantApi
    from essabu.identity.api.users import UserApi


class IdentityClient:
    """Client for the Identity module."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
        self._auth: AuthApi | None = None
        self._users: UserApi | None = None
        self._roles: RoleApi | None = None
        self._tenants: TenantApi | None = None
        self._branches: BranchApi | None = None
        self._companies: CompanyApi | None = None
        self._permissions: PermissionApi | None = None
        self._profiles: ProfileApi | None = None
        self._sessions: SessionApi | None = None
        self._api_keys: ApiKeyApi | None = None

    @property
    def auth(self) -> AuthApi:
        if self._auth is None:
            from essabu.identity.api.auth import AuthApi
            self._auth = AuthApi(self._http)
        return self._auth
    @property
    def users(self) -> UserApi:
        if self._users is None:
            from essabu.identity.api.users import UserApi
            self._users = UserApi(self._http)
        return self._users
    @property
    def roles(self) -> RoleApi:
        if self._roles is None:
            from essabu.identity.api.roles import RoleApi
            self._roles = RoleApi(self._http)
        return self._roles
    @property
    def tenants(self) -> TenantApi:
        if self._tenants is None:
            from essabu.identity.api.tenants import TenantApi
            self._tenants = TenantApi(self._http)
        return self._tenants
    @property
    def branches(self) -> BranchApi:
        if self._branches is None:
            from essabu.identity.api.branches import BranchApi
            self._branches = BranchApi(self._http)
        return self._branches
    @property
    def companies(self) -> CompanyApi:
        if self._companies is None:
            from essabu.identity.api.companies import CompanyApi
            self._companies = CompanyApi(self._http)
        return self._companies
    @property
    def permissions(self) -> PermissionApi:
        if self._permissions is None:
            from essabu.identity.api.permissions import PermissionApi
            self._permissions = PermissionApi(self._http)
        return self._permissions
    @property
    def profiles(self) -> ProfileApi:
        if self._profiles is None:
            from essabu.identity.api.profiles import ProfileApi
            self._profiles = ProfileApi(self._http)
        return self._profiles
    @property
    def sessions(self) -> SessionApi:
        if self._sessions is None:
            from essabu.identity.api.sessions import SessionApi
            self._sessions = SessionApi(self._http)
        return self._sessions
    @property
    def api_keys(self) -> ApiKeyApi:
        if self._api_keys is None:
            from essabu.identity.api.api_keys import ApiKeyApi
            self._api_keys = ApiKeyApi(self._http)
        return self._api_keys
