"""Example: Loan application workflow with the Payment module.

Demonstrates the full lending lifecycle: listing loan products, creating a KYC
profile, submitting a loan application, approving and disbursing the loan, and
recording a repayment. Uses the client.payment resource.
"""

from essabu import Essabu
from essabu.common.exceptions import EssabuError

# Initialize the client for payment and lending operations.
client = Essabu(api_key="esa_live_xxx", tenant_id="your-tenant-id")

try:
    # List all available loan products. Each product defines lending terms including
    # name, minimum/maximum amounts, interest rate, and term in months. Use this to
    # present borrowers with available options. Returns a PageResponse with the product
    # data array.
    products = client.payment.loan_products.list()
    print("Available loan products:")
    for p in products.data:
        print(f"  - {p.get('name')}: {p.get('min_amount')} - {p.get('max_amount')} ({p.get('interest_rate')}%)")

    # Create a KYC (Know Your Customer) profile for the loan applicant. Required fields
    # are customer_id, id_type (e.g., "national_id", "passport"), id_number, and full_name.
    # The KYC profile must be verified before the loan can be approved. Returns the created
    # profile with its ID and verification status.
    kyc = client.payment.kyc_profiles.create(
        customer_id="cust-001",
        id_type="national_id",
        id_number="ID-123456789",
        full_name="Jean Mukendi",
    )
    print(f"\nKYC profile created: {kyc['id']}")

    # Submit a loan application. Required fields are product_id (referencing a loan product),
    # amount, currency, purpose, duration_months, and customer_id. The application is created
    # with "pending" status and requires admin approval. Returns the application with its ID,
    # status, and calculated repayment schedule preview.
    application = client.payment.loan_applications.create(
        product_id=products.data[0]["id"] if products.data else "lp-default",
        amount="5000.00",
        currency="USD",
        purpose="Business expansion",
        duration_months=12,
        customer_id="cust-001",
    )
    print(f"Loan application submitted: {application['id']} - Status: {application['status']}")

    # Approve the loan application (admin action). Required parameter is the application ID.
    # Optional fields include approved_amount (can differ from requested amount) and notes.
    # Transitions the application status from "pending" to "approved". Raises AuthorizationError
    # if the current user lacks loan approval permissions.
    approved = client.payment.loan_applications.approve(
        application["id"],
        approved_amount="5000.00",
        notes="Good credit history",
    )
    print(f"Loan approved: {approved['status']}")

    # Disburse the approved loan to the customer's financial account. This triggers
    # the actual fund transfer and transitions the application to "disbursed" status.
    # A disbursement transaction is created automatically. The repayment schedule
    # becomes active after disbursement.
    disbursed = client.payment.loan_applications.disburse(application["id"])
    print(f"Loan disbursed: {disbursed['status']}")

    # Record a loan repayment. Required fields are loan_id (the application ID), amount,
    # currency, and payment_method. The repayment is applied against the outstanding balance
    # and the remaining schedule is recalculated. Returns the repayment record with its ID
    # and the updated outstanding balance.
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
