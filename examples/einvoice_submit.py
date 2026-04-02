"""Example: Submit an electronic invoice for tax compliance.

Demonstrates the full e-invoice workflow: creating an e-invoice record, preparing
a submission, sending it to the tax authority, checking the status, verifying an
invoice by QR code, and querying statistics. Uses the client.einvoice resource.
"""

from essabu import Essabu
from essabu.common.exceptions import EssabuError

# Initialize the client for e-invoice operations.
client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

try:
    # Create an e-invoice record with seller and buyer tax IDs, line items with tax
    # rates, and currency. Required fields are invoice_id (linking to an accounting
    # invoice), seller_tax_id, buyer_tax_id, total_amount, tax_amount, currency, and
    # items. Each item must include description, quantity, unit_price, and tax_rate.
    # Returns the created e-invoice with its generated ID and normalized data.
    einvoice = client.einvoice.invoices.create(
        invoice_id="inv-001",
        seller_tax_id="TAX-SELLER-001",
        buyer_tax_id="TAX-BUYER-002",
        total_amount="1500.00",
        tax_amount="285.00",
        currency="USD",
        items=[
            {
                "description": "Consulting services",
                "quantity": 10,
                "unit_price": "150.00",
                "tax_rate": "19.00",
            }
        ],
    )
    print(f"E-Invoice created: {einvoice['id']}")

    # Create a submission record that binds the e-invoice to a tax authority. The
    # invoice_id references the e-invoice created above. The submission is created
    # in "draft" status and must be explicitly submitted. Returns the submission
    # with its ID and current status.
    submission = client.einvoice.submissions.create(invoice_id=einvoice["id"])
    print(f"Submission created: {submission['id']} - Status: {submission['status']}")

    # Submit the e-invoice to the tax authority for validation and registration.
    # This transitions the submission from "draft" to "submitted" status. The tax
    # authority processes the submission asynchronously. Returns the updated
    # submission with its new status. Raises EssabuError if the submission is invalid.
    result = client.einvoice.submissions.submit(submission["id"])
    print(f"Submitted: {result['status']}")

    # Poll the tax authority for the current processing status of the submission.
    # Returns a dictionary with a status field that can be "accepted", "pending",
    # or "rejected". For rejected submissions, additional error details are included.
    # Poll periodically until the status is no longer "pending".
    status = client.einvoice.submissions.check_status(submission["id"])
    print(f"Submission status: {status.get('status')}")

    # Verify an e-invoice by its QR code URL. This checks the invoice against the
    # tax authority registry and returns a dictionary with a valid boolean field
    # indicating authenticity. Also returns invoice_details if the invoice is found.
    # Raises NotFoundError if the QR code does not match any registered invoice.
    verification = client.einvoice.verification.verify(qr_code="EINV-QR-ABC123")
    print(f"\nVerification result: valid={verification.get('valid')}")

    # List e-invoicing statistics. Returns aggregated data including total invoices,
    # total amounts, and status breakdowns for the tenant. The total property on the
    # PageResponse indicates the number of statistic records available.
    stats = client.einvoice.statistics.list()
    print(f"E-Invoice statistics: {stats.total} records")

except EssabuError as e:
    print(f"Error ({e.status_code}): {e.message}")
finally:
    client.close()
