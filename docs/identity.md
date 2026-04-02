# Identity Module

Authentication, user management, roles, permissions, tenants, branches, API keys, and session management.

## Available Classes

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `AuthApi` | `/api/identity/auth` | Authentication (login, register, tokens) |
| `UserApi` | `/api/identity/users` | User management |
| `RoleApi` | `/api/identity/roles` | Role-based access control |
| `PermissionApi` | `/api/identity/permissions` | Permission definitions |
| `TenantApi` | `/api/identity/tenants` | Multi-tenant management |
| `CompanyApi` | `/api/identity/companies` | Company profiles |
| `BranchApi` | `/api/identity/branches` | Branch/location management |
| `ProfileApi` | `/api/identity/profiles` | User profiles |
| `SessionApi` | `/api/identity/sessions` | Active sessions |
| `ApiKeyApi` | `/api/identity/api_keys` | API key management |

## AuthApi Methods

```python
login(*, email: str, password: str, **data: Any) -> dict[str, Any]
    # POST /api/identity/auth/login

register(**data: Any) -> dict[str, Any]
    # POST /api/identity/auth/register

refresh(*, refresh_token: str) -> dict[str, Any]
    # POST /api/identity/auth/refresh

logout() -> dict[str, Any]
    # POST /api/identity/auth/logout

forgot_password(*, email: str) -> dict[str, Any]
    # POST /api/identity/auth/forgot-password

reset_password(*, token: str, password: str) -> dict[str, Any]
    # POST /api/identity/auth/reset-password

verify_email(*, token: str) -> dict[str, Any]
    # POST /api/identity/auth/verify-email

me() -> dict[str, Any]
    # GET /api/identity/auth/me
```

## Standard CRUD Methods

All other classes (`UserApi`, `RoleApi`, `PermissionApi`, `TenantApi`, `CompanyApi`, `BranchApi`, `ProfileApi`, `SessionApi`, `ApiKeyApi`) share:

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## Code Examples

### Authentication

```python
from essabu import Essabu

client = Essabu(base_url="https://api.essabu.com")

# Login
tokens = client.identity.auth.login(email="admin@company.com", password="secret")
access_token = tokens["accessToken"]
refresh_token = tokens["refreshToken"]

# Get current user
me = client.identity.auth.me()

# Refresh token
new_tokens = client.identity.auth.refresh(refresh_token=refresh_token)

# Password reset flow
client.identity.auth.forgot_password(email="user@company.com")
client.identity.auth.reset_password(token="reset-token", password="new-password")

# Email verification
client.identity.auth.verify_email(token="verification-token")

# Logout
client.identity.auth.logout()
```

### User Management

```python
users = client.identity.users.list(page=1, page_size=20)
user = client.identity.users.create(
    email="new.user@company.com",
    first_name="Alice",
    last_name="Martin",
    role_id="role-uuid",
)
client.identity.users.update("user-uuid", first_name="Updated")
client.identity.users.delete("user-uuid")
```

### Roles and Permissions

```python
roles = client.identity.roles.list()
role = client.identity.roles.create(
    name="Accountant",
    permissions=["accounting.read", "accounting.write", "reports.view"],
)
permissions = client.identity.permissions.list()
```

### Tenants and Branches

```python
tenants = client.identity.tenants.list()
tenant = client.identity.tenants.create(name="ACME Corp", plan="enterprise")
branches = client.identity.branches.list(tenant_id="tenant-uuid")
branch = client.identity.branches.create(
    name="Kinshasa Office",
    address="123 Boulevard du 30 Juin",
    tenant_id="tenant-uuid",
)
```

### API Keys

```python
keys = client.identity.api_keys.list()
key = client.identity.api_keys.create(name="CI/CD Pipeline", scopes=["read", "write"])
client.identity.api_keys.delete("key-uuid")
```

### Sessions

```python
sessions = client.identity.sessions.list(user_id="user-uuid")
client.identity.sessions.delete("session-uuid")  # Revoke a session
```
