# Getting Started

## Installation

Install the Essabu Python SDK from PyPI using your preferred package manager. The SDK requires Python 3.10 or higher and depends on `httpx` and `pydantic`. No additional configuration is needed after installation.

```bash
pip install essabu
```

## Authentication

The SDK requires an API key and tenant ID. You can provide them explicitly or via environment variables.

### Explicit configuration

Create an Essabu client by passing your API key and tenant ID directly as constructor arguments. The `api_key` parameter accepts either a live key (prefixed `esa_live_`) or a test key (prefixed `esa_test_`). The `tenant_id` identifies the organization whose data you want to access. Both parameters are required unless set via environment variables.

```python
from essabu import Essabu

client = Essabu(
    api_key="esa_live_your_api_key",
    tenant_id="your-tenant-id",
)
```

### Environment variables

Set the `ESSABU_API_KEY` and `ESSABU_TENANT_ID` environment variables in your shell or `.env` file. These are read automatically when no explicit arguments are provided to the constructor. This approach is recommended for production deployments to avoid hardcoding secrets in source code.

```bash
export ESSABU_API_KEY=esa_live_your_api_key
export ESSABU_TENANT_ID=your-tenant-id
```

When environment variables are set, the client can be instantiated with no arguments. All configuration values are loaded from the corresponding environment variables automatically. Missing required values raise a `ConfigurationError` at instantiation time.

```python
from essabu import Essabu

client = Essabu()  # reads from environment
```

### Configuration options

| Parameter     | Env Variable       | Default                   | Description              |
|---------------|--------------------|---------------------------|--------------------------|
| `api_key`     | `ESSABU_API_KEY`   | -                         | Your API key             |
| `tenant_id`   | `ESSABU_TENANT_ID` | -                         | Your tenant identifier   |
| `base_url`    | `ESSABU_BASE_URL`  | `https://api.essabu.com`  | API base URL             |
| `timeout`     | `ESSABU_TIMEOUT`   | `30.0`                    | Request timeout (seconds)|
| `max_retries` | `ESSABU_MAX_RETRIES`| `3`                      | Max retry attempts       |

## Basic Usage

Initialize the client and perform standard CRUD operations on any module resource. The example below demonstrates creating an employee, listing with pagination, retrieving by ID, updating, and deleting. All `create` and `update` methods accept keyword arguments matching the API fields and return a dictionary. The `delete` method performs a soft delete and returns a confirmation.

```python
from essabu import Essabu

client = Essabu(api_key="esa_live_xxx", tenant_id="tenant-id")

# Create a resource
employee = client.hr.employees.create(
    first_name="Jean",
    last_name="Mukendi",
    email="jean@example.com",
)

# List with pagination
page = client.hr.employees.list(page=1, page_size=25)
print(f"Total: {page.total}")

# Retrieve by ID
emp = client.hr.employees.retrieve("employee-uuid")

# Update
client.hr.employees.update("employee-uuid", position_id="new-position")

# Delete
client.hr.employees.delete("employee-uuid")

# Always close when done
client.close()
```

## Context Manager

Use the context manager pattern to ensure the HTTP client is properly closed when done, even if an exception occurs. The `with` statement calls `client.close()` automatically when the block exits. This is the recommended approach for scripts and short-lived operations.

```python
with Essabu(api_key="esa_live_xxx", tenant_id="tenant-id") as client:
    employees = client.hr.employees.list()
    # client is automatically closed
```

## Error Handling

The SDK provides a hierarchy of typed exceptions for different HTTP error codes. Import the specific exceptions you want to handle from `essabu.common.exceptions`. Each exception exposes `status_code`, `message`, and (for `ValidationError`) an `errors` list with per-field details. Always catch `EssabuError` as the fallback to handle unexpected API errors.

```python
from essabu.common.exceptions import (
    EssabuError,
    NotFoundError,
    ValidationError,
    AuthenticationError,
    RateLimitError,
)

try:
    client.hr.employees.retrieve("nonexistent")
except NotFoundError:
    print("Employee not found")
except ValidationError as e:
    print(f"Invalid data: {e.errors}")
except AuthenticationError:
    print("Check your API key")
except RateLimitError as e:
    print(f"Retry after {e.retry_after} seconds")
except EssabuError as e:
    print(f"API error {e.status_code}: {e.message}")
```

## Pagination

All `list()` methods return a `PageResponse` with metadata such as `total`, `page`, `total_pages`, and `has_next`. Use `list_all()` to get a generator that automatically iterates through every page. The `page_size` parameter controls how many items are fetched per request (default 25, maximum 100).

```python
# Single page
page = client.hr.employees.list(page=2, page_size=50)
print(f"Page {page.page}/{page.total_pages}")

# All pages iterator
for page in client.hr.employees.list_all(page_size=100):
    for employee in page.data:
        process(employee)
```
