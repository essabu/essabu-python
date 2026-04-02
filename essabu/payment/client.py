"""Payment module client for the Essabu SDK."""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.payment.api.collaterals import CollateralsApi
from essabu.payment.api.financial_accounts import FinancialAccountsApi
from essabu.payment.api.kyc_documents import KycDocumentsApi
from essabu.payment.api.kyc_profiles import KycProfilesApi
from essabu.payment.api.loan_applications import LoanApplicationsApi
from essabu.payment.api.loan_products import LoanProductsApi
from essabu.payment.api.loan_repayments import LoanRepaymentsApi
from essabu.payment.api.payment_accounts import PaymentAccountsApi
from essabu.payment.api.payment_intents import PaymentIntentsApi
from essabu.payment.api.refunds import RefundsApi
from essabu.payment.api.reports import ReportsApi
from essabu.payment.api.subscription_plans import SubscriptionPlansApi
from essabu.payment.api.subscriptions import SubscriptionsApi
from essabu.payment.api.transactions import TransactionsApi


class PaymentClient:
    """Payment module client providing access to all Payment API resources."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    @cached_property
    def payment_intents(self) -> PaymentIntentsApi:
        return PaymentIntentsApi(self._http)

    @cached_property
    def payment_accounts(self) -> PaymentAccountsApi:
        return PaymentAccountsApi(self._http)

    @cached_property
    def transactions(self) -> TransactionsApi:
        return TransactionsApi(self._http)

    @cached_property
    def refunds(self) -> RefundsApi:
        return RefundsApi(self._http)

    @cached_property
    def subscriptions(self) -> SubscriptionsApi:
        return SubscriptionsApi(self._http)

    @cached_property
    def subscription_plans(self) -> SubscriptionPlansApi:
        return SubscriptionPlansApi(self._http)

    @cached_property
    def financial_accounts(self) -> FinancialAccountsApi:
        return FinancialAccountsApi(self._http)

    @cached_property
    def loan_products(self) -> LoanProductsApi:
        return LoanProductsApi(self._http)

    @cached_property
    def loan_applications(self) -> LoanApplicationsApi:
        return LoanApplicationsApi(self._http)

    @cached_property
    def loan_repayments(self) -> LoanRepaymentsApi:
        return LoanRepaymentsApi(self._http)

    @cached_property
    def collaterals(self) -> CollateralsApi:
        return CollateralsApi(self._http)

    @cached_property
    def kyc_profiles(self) -> KycProfilesApi:
        return KycProfilesApi(self._http)

    @cached_property
    def kyc_documents(self) -> KycDocumentsApi:
        return KycDocumentsApi(self._http)

    @cached_property
    def reports(self) -> ReportsApi:
        return ReportsApi(self._http)
