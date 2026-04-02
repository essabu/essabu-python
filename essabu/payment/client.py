"""Payment module client."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient

if TYPE_CHECKING:
    from essabu.payment.api.collaterals import CollateralApi
    from essabu.payment.api.financial_accounts import FinancialAccountApi
    from essabu.payment.api.kyc_documents import KycDocumentApi
    from essabu.payment.api.kyc_profiles import KycProfileApi
    from essabu.payment.api.loan_applications import LoanApplicationApi
    from essabu.payment.api.loan_products import LoanProductApi
    from essabu.payment.api.loan_repayments import LoanRepaymentApi
    from essabu.payment.api.payment_accounts import PaymentAccountApi
    from essabu.payment.api.payment_intents import PaymentIntentApi
    from essabu.payment.api.refunds import RefundApi
    from essabu.payment.api.reports import ReportApi
    from essabu.payment.api.subscription_plans import SubscriptionPlanApi
    from essabu.payment.api.subscriptions import SubscriptionApi
    from essabu.payment.api.transactions import TransactionApi


class PaymentClient:
    """Client for the Payment module."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
        self._payment_intents: PaymentIntentApi | None = None
        self._payment_accounts: PaymentAccountApi | None = None
        self._transactions: TransactionApi | None = None
        self._refunds: RefundApi | None = None
        self._subscriptions: SubscriptionApi | None = None
        self._subscription_plans: SubscriptionPlanApi | None = None
        self._loan_applications: LoanApplicationApi | None = None
        self._loan_products: LoanProductApi | None = None
        self._loan_repayments: LoanRepaymentApi | None = None
        self._collaterals: CollateralApi | None = None
        self._financial_accounts: FinancialAccountApi | None = None
        self._kyc_documents: KycDocumentApi | None = None
        self._kyc_profiles: KycProfileApi | None = None
        self._reports: ReportApi | None = None

    @property
    def payment_intents(self) -> PaymentIntentApi:
        if self._payment_intents is None:
            from essabu.payment.api.payment_intents import PaymentIntentApi
            self._payment_intents = PaymentIntentApi(self._http)
        return self._payment_intents
    @property
    def payment_accounts(self) -> PaymentAccountApi:
        if self._payment_accounts is None:
            from essabu.payment.api.payment_accounts import PaymentAccountApi
            self._payment_accounts = PaymentAccountApi(self._http)
        return self._payment_accounts
    @property
    def transactions(self) -> TransactionApi:
        if self._transactions is None:
            from essabu.payment.api.transactions import TransactionApi
            self._transactions = TransactionApi(self._http)
        return self._transactions
    @property
    def refunds(self) -> RefundApi:
        if self._refunds is None:
            from essabu.payment.api.refunds import RefundApi
            self._refunds = RefundApi(self._http)
        return self._refunds
    @property
    def subscriptions(self) -> SubscriptionApi:
        if self._subscriptions is None:
            from essabu.payment.api.subscriptions import SubscriptionApi
            self._subscriptions = SubscriptionApi(self._http)
        return self._subscriptions
    @property
    def subscription_plans(self) -> SubscriptionPlanApi:
        if self._subscription_plans is None:
            from essabu.payment.api.subscription_plans import SubscriptionPlanApi
            self._subscription_plans = SubscriptionPlanApi(self._http)
        return self._subscription_plans
    @property
    def loan_applications(self) -> LoanApplicationApi:
        if self._loan_applications is None:
            from essabu.payment.api.loan_applications import LoanApplicationApi
            self._loan_applications = LoanApplicationApi(self._http)
        return self._loan_applications
    @property
    def loan_products(self) -> LoanProductApi:
        if self._loan_products is None:
            from essabu.payment.api.loan_products import LoanProductApi
            self._loan_products = LoanProductApi(self._http)
        return self._loan_products
    @property
    def loan_repayments(self) -> LoanRepaymentApi:
        if self._loan_repayments is None:
            from essabu.payment.api.loan_repayments import LoanRepaymentApi
            self._loan_repayments = LoanRepaymentApi(self._http)
        return self._loan_repayments
    @property
    def collaterals(self) -> CollateralApi:
        if self._collaterals is None:
            from essabu.payment.api.collaterals import CollateralApi
            self._collaterals = CollateralApi(self._http)
        return self._collaterals
    @property
    def financial_accounts(self) -> FinancialAccountApi:
        if self._financial_accounts is None:
            from essabu.payment.api.financial_accounts import FinancialAccountApi
            self._financial_accounts = FinancialAccountApi(self._http)
        return self._financial_accounts
    @property
    def kyc_documents(self) -> KycDocumentApi:
        if self._kyc_documents is None:
            from essabu.payment.api.kyc_documents import KycDocumentApi
            self._kyc_documents = KycDocumentApi(self._http)
        return self._kyc_documents
    @property
    def kyc_profiles(self) -> KycProfileApi:
        if self._kyc_profiles is None:
            from essabu.payment.api.kyc_profiles import KycProfileApi
            self._kyc_profiles = KycProfileApi(self._http)
        return self._kyc_profiles
    @property
    def reports(self) -> ReportApi:
        if self._reports is None:
            from essabu.payment.api.reports import ReportApi
            self._reports = ReportApi(self._http)
        return self._reports
