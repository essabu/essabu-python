"""Example: Authentication flows with the Identity module."""

from essabu import Essabu
from essabu.common.exceptions import AuthenticationError

# Method 1: API key authentication (most common for server-side)
client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

# Method 2: Login with email/password to get a token
try:
    tokens = client.identity.auth.login(email="admin@company.com", password="secure-password")
    print(f"Access token: {tokens['access_token'][:20]}...")
    print(f"Refresh token: {tokens['refresh_token'][:20]}...")

    # Get current user profile
    me = client.identity.auth.me()
    print(f"Logged in as: {me.get('email')}")

    # Refresh the token
    new_tokens = client.identity.auth.refresh(refresh_token=tokens["refresh_token"])
    print("Token refreshed successfully")

    # List users (admin only)
    users = client.identity.users.list(page=1, page_size=10)
    print(f"\nUsers ({users.total} total):")
    for user in users.data:
        print(f"  - {user.get('email')} ({user.get('role', 'N/A')})")

    # Manage roles
    roles = client.identity.roles.list()
    print(f"\nRoles ({roles.total} total):")
    for role in roles.data:
        print(f"  - {role.get('name')}: {role.get('description', '')}")

except AuthenticationError as e:
    print(f"Authentication failed: {e.message}")
finally:
    client.close()
