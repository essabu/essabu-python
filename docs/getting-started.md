# Getting Started

## Installation

```bash
pip install essabu
```

## Authentication

The SDK requires an API key and tenant ID. You can provide them explicitly or via environment variables.

### Explicit configuration

```python
from essabu import Essabu

client = Essabu(
    api_key="esa_live_your_api_key",
    tenant_id="your-tenant-id",
)
```

### Environment variables

```bash
export ESSABU_API_KEY=esa_live_your_api_key
export ESSABU_TENANT_ID=your-tenant-id
```

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

```python
with Essabu(api_key="esa_live_xxx", tenant_id="tenant-id") as client:
    employees = client.hr.employees.list()
    # client is automatically closed
```

## Error Handling

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

```python
# Single page
page = client.hr.employees.list(page=2, page_size=50)
print(f"Page {page.page}/{page.total_pages}")

# All pages iterator
for page in client.hr.employees.list_all(page_size=100):
    for employee in page.data:
        process(employee)
```
