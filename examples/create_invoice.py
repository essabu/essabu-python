"""Example: Create and manage invoices in the Accounting module.

Demonstrates invoice creation with multiple line items, listing draft invoices
with pagination, and recording a payment against an invoice. Uses the
client.accounting.invoices and client.accounting.payments resources.
"""

from essabu import Essabu

# Initialize the client with API key and tenant ID for authentication.
client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

# Create a new invoice with multiple line items. Required fields are customer_id,
# currency, and items (a list of line items with description, quantity, and unit_price).
# Optional fields include due_date and notes. The total is calculated automatically
# from the line items. Returns the created invoice with its generated ID and computed total.
invoice = client.accounting.invoices.create(
    customer_id="cust-001",
    currency="USD",
    due_date="2024-02-28",
    items=[
        {"description": "Consulting services - January", "quantity": 40, "unit_price": "150.00"},
        {"description": "Travel expenses", "quantity": 1, "unit_price": "500.00"},
    ],
    notes="Payment due within 30 days.",
)
print(f"Invoice created: {invoice['id']} - Total: {invoice.get('total', 'N/A')}")

# List invoices filtered by status with pagination. The status filter accepts values
# like "draft", "sent", "paid", or "overdue". Returns a PageResponse with total count
# and the invoice data array. Each invoice includes id, total, currency, and status fields.
invoices = client.accounting.invoices.list(page=1, page_size=10, status="draft")
print(f"\nDraft invoices: {invoices.total}")
for inv in invoices.data:
    print(f"  - {inv['id']}: {inv.get('total', '?')} {inv.get('currency', '')}")

# Record a payment against the invoice. Required fields are invoice_id, amount, currency,
# and payment_method (e.g., "bank_transfer", "mobile_money", "cash"). The optional
# reference field stores an external payment reference. Partial payments are supported;
# the invoice status updates automatically when fully paid.
payment = client.accounting.payments.create(
    invoice_id=invoice["id"],
    amount="6500.00",
    currency="USD",
    payment_method="bank_transfer",
    reference="WIRE-20240115-001",
)
print(f"\nPayment recorded: {payment['id']}")

client.close()
