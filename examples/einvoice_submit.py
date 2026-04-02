"""Example: Submit an electronic invoice for tax compliance."""

from essabu import Essabu
from essabu.common.exceptions import EssabuError

client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

try:
    # Create an e-invoice
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

    # Create a submission
    submission = client.einvoice.submissions.create(invoice_id=einvoice["id"])
    print(f"Submission created: {submission['id']} - Status: {submission['status']}")

    # Submit to the tax authority
    result = client.einvoice.submissions.submit(submission["id"])
    print(f"Submitted: {result['status']}")

    # Check submission status
    status = client.einvoice.submissions.check_status(submission["id"])
    print(f"Submission status: {status.get('status')}")

    # Verify an e-invoice by QR code
    verification = client.einvoice.verification.verify(qr_code="EINV-QR-ABC123")
    print(f"\nVerification result: valid={verification.get('valid')}")

    # Check compliance statistics
    stats = client.einvoice.statistics.list()
    print(f"E-Invoice statistics: {stats.total} records")

except EssabuError as e:
    print(f"Error ({e.status_code}): {e.message}")
finally:
    client.close()
