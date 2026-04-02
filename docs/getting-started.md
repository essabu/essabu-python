# Getting Started

## Installation

```bash
pip install essabu
```

## Authentication

The SDK requires an API key. Optionally provide a tenant ID for multi-tenant isolation.

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key", tenant_id="your-tenant-id")
```

## Basic Usage

### HR - Manage Employees

```python
# Create an employee
employee = client.hr.employees.create({
    "first_name": "Jean",
    "last_name": "Mukendi",
    "email": "jean.mukendi@example.com",
})

# List employees with pagination
from essabu import PageRequest

page = client.hr.employees.list(PageRequest.of(page=0, size=25))
for emp in page.content:
    print(emp["firstName"], emp["lastName"])
```

### Accounting - Create an Invoice

```python
invoice = client.accounting.invoices.create({
    "companyId": "company-uuid",
    "customerId": "customer-uuid",
    "items": [
        {"description": "Service", "quantity": 1, "unitPrice": 50000}
    ],
})

# Finalize and send
client.accounting.invoices.finalize(invoice["id"])
client.accounting.invoices.send(invoice["id"])
```

### Identity - Login

```python
token = client.identity.auth.login(email="user@example.com", password="secret")
print(token.access_token)
```

### Trade - CRM Operations

```python
contact = client.trade.contacts.create({"name": "Acme Corp", "email": "info@acme.com"})
contacts = client.trade.contacts.list()
```

### Payment - Process a Payment

```python
intent = client.payment.payment_intents.create({
    "amount": 100000,
    "currency": "BIF",
    "payment_method": "mobile_money",
})
```

## Error Handling

```python
from essabu import EssabuError, NotFoundError, ValidationError

try:
    client.hr.employees.get("non-existent")
except NotFoundError:
    print("Employee not found")
except ValidationError as e:
    print(f"Invalid request: {e.errors}")
except EssabuError as e:
    print(f"API error: {e.message}")
```

## Advanced Configuration

### Per-Service URLs

```python
client = Essabu(
    api_key="xxx",
    service_urls={
        "hr": "https://hr-api.essabu.com",
        "accounting": "https://accounting-api.essabu.com",
    },
)
```

### Custom Timeout and Retries

```python
client = Essabu(api_key="xxx", timeout=60.0, max_retries=5)
```

### Context Manager

```python
with Essabu(api_key="xxx") as client:
    employees = client.hr.employees.list()
# HTTP connections are automatically closed
```
