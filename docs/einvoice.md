# E-Invoice Module

Electronic invoicing: create, normalize, submit to tax authorities, verify, and track compliance.

## Available Classes

| Class | Resource Path | Description |
|-------|--------------|-------------|
| `InvoiceApi` | `/api/einvoice/invoices` | E-invoice management |
| `SubmissionApi` | `/api/einvoice/submissions` | Tax authority submissions |
| `VerificationApi` | `/api/einvoice/verification` | Invoice verification |
| `ComplianceApi` | `/api/einvoice/compliance` | Compliance records |
| `StatisticApi` | `/api/einvoice/statistics` | E-invoice statistics |

## Standard CRUD Methods

All classes share:

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## SubmissionApi Extra Methods

```python
submit(resource_id: str) -> dict[str, Any]
    # POST /api/einvoice/submissions/{id}/submit
    # Submit an e-invoice to the tax authority

check_status(resource_id: str) -> dict[str, Any]
    # GET /api/einvoice/submissions/{id}/status
    # Check the submission status with the tax authority
```

## VerificationApi Extra Methods

```python
verify(**data: Any) -> dict[str, Any]
    # POST /api/einvoice/verification/verify
    # Verify an e-invoice by QR code or reference number
```

## Code Examples

### Create and Submit an E-Invoice

```python
from essabu import Essabu

client = Essabu(api_key="your-api-key")

# Create an e-invoice
einvoice = client.einvoice.invoices.create(
    invoice_id="inv-uuid",
    customer_tin="123456789",
    customer_name="ACME Corp",
    items=[
        {
            "description": "Consulting services",
            "quantity": 10,
            "unit_price": 150.00,
            "tax_rate": 16.0,
        },
    ],
    currency="CDF",
)

# Create a submission
submission = client.einvoice.submissions.create(
    invoice_id=einvoice["id"],
    authority="OBR",
)

# Submit to tax authority
result = client.einvoice.submissions.submit(submission["id"])

# Check submission status
status = client.einvoice.submissions.check_status(submission["id"])
print(status["status"])  # "accepted", "pending", "rejected"
```

### Verify an Invoice

```python
# Verify by QR code
verification = client.einvoice.verification.verify(
    qr_code="https://tax.gov/verify/ABC123",
)

# Verify by reference
verification = client.einvoice.verification.verify(
    reference="EI-2026-00123",
    tin="123456789",
)
```

### List and Filter

```python
# List all invoices with filters
invoices = client.einvoice.invoices.list(status="submitted", page_size=50)

# Iterate all pages
for page in client.einvoice.invoices.list_all():
    for inv in page.data:
        print(inv["reference"], inv["status"])

# List submissions
submissions = client.einvoice.submissions.list(status="accepted")

# List compliance records
records = client.einvoice.compliance.list(year=2026)
```

### Statistics

```python
stats = client.einvoice.statistics.list(
    start_date="2026-01-01",
    end_date="2026-03-31",
)
monthly = client.einvoice.statistics.retrieve("2026-03")
```

### Compliance

```python
compliance = client.einvoice.compliance.list(status="compliant")
record = client.einvoice.compliance.retrieve("comp-uuid")
client.einvoice.compliance.create(
    period="2026-Q1",
    authority="OBR",
    total_invoices=150,
    total_amount=75000.00,
)
```
