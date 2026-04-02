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

All classes share these standard methods for paginated listing, iteration, creation, retrieval, update, and deletion of e-invoice resources. The `list` method accepts optional filter keyword arguments such as `status` or `page_size`. The `create` and `update` methods accept keyword arguments matching the resource fields and return the created or updated resource as a dictionary.

```python
list(*, page: int = 1, page_size: int = 25, **filters: Any) -> PageResponse
list_all(*, page_size: int = 25, **filters: Any) -> Generator[PageResponse, None, None]
create(**data: Any) -> dict[str, Any]
retrieve(resource_id: str) -> dict[str, Any]
update(resource_id: str, **data: Any) -> dict[str, Any]
delete(resource_id: str) -> dict[str, Any]
```

## SubmissionApi Extra Methods

The `submit` method sends an e-invoice to the configured tax authority for validation and registration. It transitions the submission status from `"draft"` to `"submitted"`. The `check_status` method polls the tax authority for the current processing status, returning one of `"accepted"`, `"pending"`, or `"rejected"`. Both methods require the submission `resource_id` as their first argument.

```python
submit(resource_id: str) -> dict[str, Any]
    # POST /api/einvoice/submissions/{id}/submit
    # Submit an e-invoice to the tax authority

check_status(resource_id: str) -> dict[str, Any]
    # GET /api/einvoice/submissions/{id}/status
    # Check the submission status with the tax authority
```

## VerificationApi Extra Methods

The `verify` method validates an e-invoice against the tax authority registry using either a QR code URL or a reference number with TIN. It returns a dictionary with a `valid` boolean field indicating whether the invoice is authentic and registered. Throws `NotFoundError` if the invoice cannot be found in the tax authority records.

```python
verify(**data: Any) -> dict[str, Any]
    # POST /api/einvoice/verification/verify
    # Verify an e-invoice by QR code or reference number
```

## Code Examples

### Create and Submit an E-Invoice

Create an e-invoice record, prepare a submission, send it to the tax authority, and check the result. The `invoices.create` method requires `invoice_id` (linking to an accounting invoice), `customer_tin` (tax identification number), `customer_name`, a list of `items` with tax rates, and `currency`. The `submissions.create` method binds the invoice to a tax `authority` (e.g., `"OBR"`). After calling `submit`, use `check_status` to poll for the authority response.

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

Verify an e-invoice authenticity against the tax authority registry. You can verify using either a QR code URL (typically printed on the invoice) or a combination of reference number and TIN. The method returns a dictionary with `valid` (boolean), `invoice_details`, and `authority_response` fields. This is useful for buyers who want to confirm that an invoice is genuine and properly registered.

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

Query e-invoices, submissions, and compliance records using filters. The `list` method supports keyword filters such as `status`, `page_size`, and module-specific fields. The `list_all` method returns a generator that automatically paginates through all results. Use status filters like `"submitted"`, `"accepted"`, or `"rejected"` to narrow results by processing state.

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

Retrieve aggregated e-invoicing statistics for a given period. The `list` method accepts `start_date` and `end_date` to define the reporting window and returns summary data including total invoices, amounts, and status breakdowns. The `retrieve` method fetches statistics for a specific month using the `"YYYY-MM"` format as the identifier.

```python
stats = client.einvoice.statistics.list(
    start_date="2026-01-01",
    end_date="2026-03-31",
)
monthly = client.einvoice.statistics.retrieve("2026-03")
```

### Compliance

Manage compliance records that track e-invoicing adherence for tax reporting periods. The `list` method supports filtering by `status` (e.g., `"compliant"`, `"non_compliant"`). The `create` method registers a compliance record for a given `period` and `authority`, including `total_invoices` and `total_amount` for the period. Use `retrieve` to get detailed compliance information including any discrepancies.

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
