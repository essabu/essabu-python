"""Example: Create and manage invoices in the Accounting module."""

from essabu import Essabu

client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

# Create an invoice
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

# List recent invoices
invoices = client.accounting.invoices.list(page=1, page_size=10, status="draft")
print(f"\nDraft invoices: {invoices.total}")
for inv in invoices.data:
    print(f"  - {inv['id']}: {inv.get('total', '?')} {inv.get('currency', '')}")

# Record a payment
payment = client.accounting.payments.create(
    invoice_id=invoice["id"],
    amount="6500.00",
    currency="USD",
    payment_method="bank_transfer",
    reference="WIRE-20240115-001",
)
print(f"\nPayment recorded: {payment['id']}")

client.close()
