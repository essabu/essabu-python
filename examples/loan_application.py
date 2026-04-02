"""Example: Loan application workflow with the Payment module."""

from essabu import Essabu
from essabu.common.exceptions import EssabuError

client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

try:
    # List available loan products
    products = client.payment.loan_products.list()
    print("Available loan products:")
    for p in products.data:
        print(f"  - {p.get('name')}: {p.get('min_amount')} - {p.get('max_amount')} ({p.get('interest_rate')}%)")

    # Create a KYC profile for the applicant
    kyc = client.payment.kyc_profiles.create(
        customer_id="cust-001",
        id_type="national_id",
        id_number="ID-123456789",
        full_name="Jean Mukendi",
    )
    print(f"\nKYC profile created: {kyc['id']}")

    # Submit a loan application
    application = client.payment.loan_applications.create(
        product_id=products.data[0]["id"] if products.data else "lp-default",
        amount="5000.00",
        currency="USD",
        purpose="Business expansion",
        duration_months=12,
        customer_id="cust-001",
    )
    print(f"Loan application submitted: {application['id']} - Status: {application['status']}")

    # Approve the loan (admin action)
    approved = client.payment.loan_applications.approve(
        application["id"],
        approved_amount="5000.00",
        notes="Good credit history",
    )
    print(f"Loan approved: {approved['status']}")

    # Disburse the loan
    disbursed = client.payment.loan_applications.disburse(application["id"])
    print(f"Loan disbursed: {disbursed['status']}")

    # Record a repayment
    repayment = client.payment.loan_repayments.create(
        loan_id=application["id"],
        amount="450.00",
        currency="USD",
        payment_method="mobile_money",
    )
    print(f"\nRepayment recorded: {repayment['id']}")

except EssabuError as e:
    print(f"Error ({e.status_code}): {e.message}")
finally:
    client.close()
