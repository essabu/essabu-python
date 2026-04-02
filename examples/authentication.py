"""Example: Authentication flows with the Identity module.

Demonstrates API key authentication, email/password login to obtain JWT tokens,
retrieving the current user profile, refreshing tokens, listing users (admin only),
and listing roles. Catches AuthenticationError for invalid credentials.
"""

from essabu import Essabu
from essabu.common.exceptions import AuthenticationError

# Initialize the client with an API key and tenant ID. This is the most common
# authentication method for server-side applications. The API key is passed in the
# Authorization header of every request.
client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

# Authenticate with email and password to obtain an access token and refresh token.
# The access token is a short-lived JWT used for API requests. The refresh token is
# longer-lived and can be exchanged for a new access token without re-entering
# credentials. Raises AuthenticationError if the email or password is incorrect.
try:
    tokens = client.identity.auth.login(email="admin@company.com", password="secure-password")
    print(f"Access token: {tokens['access_token'][:20]}...")
    print(f"Refresh token: {tokens['refresh_token'][:20]}...")

    # Retrieve the profile of the currently authenticated user. Returns a dictionary
    # with fields like email, first_name, last_name, role, and tenant_id. This is
    # useful for displaying the logged-in user's information in a UI.
    me = client.identity.auth.me()
    print(f"Logged in as: {me.get('email')}")

    # Exchange the refresh token for a new access token. This avoids requiring the
    # user to log in again when the access token expires. Returns a new token pair.
    # The old refresh token is invalidated after use.
    new_tokens = client.identity.auth.refresh(refresh_token=tokens["refresh_token"])
    print("Token refreshed successfully")

    # List all user accounts with pagination. Requires admin privileges. The page_size
    # parameter controls how many users are returned per page (default 25, max 100).
    # Returns a PageResponse with total count and user data.
    users = client.identity.users.list(page=1, page_size=10)
    print(f"\nUsers ({users.total} total):")
    for user in users.data:
        print(f"  - {user.get('email')} ({user.get('role', 'N/A')})")

    # List all defined roles with their descriptions. Roles group permissions that
    # control access to different modules and operations. Each role includes a name,
    # description, and a list of associated permission identifiers.
    roles = client.identity.roles.list()
    print(f"\nRoles ({roles.total} total):")
    for role in roles.data:
        print(f"  - {role.get('name')}: {role.get('description', '')}")

except AuthenticationError as e:
    print(f"Authentication failed: {e.message}")
finally:
    client.close()
