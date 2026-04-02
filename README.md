# Essabu Python SDK

Unified Python SDK for all Essabu services. One package, one client, all modules.

## Installation

```bash
pip install essabu
```

## Quick Start

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key", tenant_id="your-tenant-id")

# HR
employee = client.hr.employees.create({"first_name": "Jean", "last_name": "Mukendi"})
employees = client.hr.employees.list()

# Accounting
invoice = client.accounting.invoices.create({...})
client.accounting.invoices.finalize(invoice["id"])

# Identity
token = client.identity.auth.login(email="user@example.com", password="secret")

# Trade
contact = client.trade.contacts.create({"name": "Acme Corp"})

# Payment
intent = client.payment.payment_intents.create({"amount": 10000, "currency": "BIF"})

# EInvoice
normalized = client.einvoice.invoices.normalize({...})

# Project
project = client.project.projects.create({"name": "New Project"})

# Asset
asset = client.asset.assets.create({"name": "Laptop #42"})
```

## Available Modules

| Module | Access | Resources |
|--------|--------|-----------|
| **HR** | `client.hr` | employees, departments, positions, contracts, attendance, leaves, payroll, recruitment, training, and more |
| **Accounting** | `client.accounting` | accounts, invoices, journals, payments, tax rates, currencies, fiscal years, inventory, and more |
| **Identity** | `client.identity` | auth, users, roles, permissions, companies, tenants, branches, sessions, API keys |
| **Trade** | `client.trade` | customers, products, sales orders, purchase orders, deliveries, contacts, CRM, and more |
| **Payment** | `client.payment` | payment intents, subscriptions, loans, KYC, financial accounts, refunds, and more |
| **EInvoice** | `client.einvoice` | invoice normalization, submissions, verification, compliance, statistics |
| **Project** | `client.project` | projects, milestones, tasks, comments, resource allocations, reports |
| **Asset** | `client.asset` | assets, depreciation, vehicles, fuel logs, trip logs, maintenance |

## Configuration

```python
from essabu import Essabu, EssabuConfig

# Simple
client = Essabu(api_key="xxx", tenant_id="xxx")

# With options
client = Essabu(
    api_key="xxx",
    tenant_id="xxx",
    base_url="https://custom-api.essabu.com",
    timeout=60.0,
    max_retries=5,
)

# Per-service URLs
client = Essabu(
    api_key="xxx",
    service_urls={
        "hr": "https://hr.essabu.com",
        "accounting": "https://accounting.essabu.com",
    },
)

# From config object
config = EssabuConfig(api_key="xxx", tenant_id="xxx")
client = Essabu(config=config)
```

## Error Handling

```python
from essabu import Essabu, EssabuError, NotFoundError, ValidationError

client = Essabu(api_key="xxx")

try:
    employee = client.hr.employees.get("non-existent-id")
except NotFoundError as e:
    print(f"Not found: {e}")
except ValidationError as e:
    print(f"Validation failed: {e.errors}")
except EssabuError as e:
    print(f"API error [{e.status_code}]: {e.message}")
```

## Pagination

```python
from essabu import PageRequest

page = client.hr.employees.list(PageRequest.of(page=0, size=50))
print(f"Total: {page.total_elements}, Page: {page.page}")

while page.has_next:
    page = client.hr.employees.list(PageRequest.of(page=page.page + 1, size=50))
```

## License

MIT
