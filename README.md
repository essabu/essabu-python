# Essabu Python SDK

Official Python SDK for the Essabu platform -- unified SaaS billing, accounting, HR, and business management.

## Installation

```bash
pip install essabu
```

## Quick Start

```python
from essabu import Essabu

client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

# HR - Create an employee
employee = client.hr.employees.create(
    first_name="Jean",
    last_name="Mukendi",
    email="jean.mukendi@example.com",
    department_id="dept-001",
)
print(employee)

# Accounting - Create an invoice
invoice = client.accounting.invoices.create(
    customer_id="cust-001",
    items=[
        {"description": "Consulting", "quantity": 10, "unit_price": "150.00"}
    ],
    currency="USD",
)
print(invoice)

# Trade / CRM - List customers
customers = client.trade.customers.list(page=1, page_size=25)
for c in customers.data:
    print(c["name"])

# Payments - Create a payment intent
intent = client.payment.payment_intents.create(
    amount="500.00",
    currency="USD",
    payment_method="mobile_money",
)
print(intent)
```

## Modules

| Module       | Access               | Description                            |
|--------------|----------------------|----------------------------------------|
| HR           | `client.hr`          | Employees, contracts, leaves, payroll  |
| Accounting   | `client.accounting`  | Accounts, invoices, payments, wallets  |
| Identity     | `client.identity`    | Auth, users, roles, tenants            |
| Trade        | `client.trade`       | CRM, customers, opportunities, orders  |
| Payment      | `client.payment`     | Payment intents, loans, subscriptions  |
| E-Invoice    | `client.einvoice`    | Electronic invoicing, compliance       |
| Project      | `client.project`     | Projects, tasks, milestones            |
| Asset        | `client.asset`       | Fixed assets, vehicles, depreciation   |

## Configuration

```python
from essabu import Essabu

# Using environment variables
# ESSABU_API_KEY, ESSABU_TENANT_ID, ESSABU_BASE_URL
client = Essabu()

# Explicit configuration
client = Essabu(
    api_key="esa_live_xxx",
    tenant_id="your-tenant-id",
    base_url="https://api.essabu.com",
    timeout=30.0,
    max_retries=3,
)
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
    employee = client.hr.employees.retrieve("nonexistent-id")
except NotFoundError as e:
    print(f"Not found: {e.message}")
except ValidationError as e:
    print(f"Validation failed: {e.errors}")
except AuthenticationError:
    print("Invalid API key")
except RateLimitError as e:
    print(f"Rate limited. Retry after {e.retry_after}s")
except EssabuError as e:
    print(f"API error: {e.status_code} - {e.message}")
```

## Pagination

```python
# Manual pagination
page = client.hr.employees.list(page=1, page_size=50)
print(f"Total: {page.total}, Pages: {page.total_pages}")

# Iterate all pages
for page in client.hr.employees.list_all(page_size=50):
    for emp in page.data:
        print(emp["first_name"])
```

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Type checking
mypy essabu/

# Linting
ruff check essabu/
```

## License

MIT License - see [LICENSE](LICENSE) for details.
