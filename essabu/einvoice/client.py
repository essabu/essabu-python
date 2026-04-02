"""E-Invoice module client."""

from __future__ import annotations

from typing import TYPE_CHECKING

from essabu.common.http_client import HttpClient

if TYPE_CHECKING:
    from essabu.einvoice.api.invoices import InvoiceApi
    from essabu.einvoice.api.submissions import SubmissionApi
    from essabu.einvoice.api.verification import VerificationApi
    from essabu.einvoice.api.compliance import ComplianceApi
    from essabu.einvoice.api.statistics import StatisticApi


class EInvoiceClient:
    """Client for the E-Invoice module."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http
        self._invoices: InvoiceApi | None = None
        self._submissions: SubmissionApi | None = None
        self._verification: VerificationApi | None = None
        self._compliance: ComplianceApi | None = None
        self._statistics: StatisticApi | None = None

    @property
    def invoices(self) -> InvoiceApi:
        if self._invoices is None:
            from essabu.einvoice.api.invoices import InvoiceApi
            self._invoices = InvoiceApi(self._http)
        return self._invoices
    @property
    def submissions(self) -> SubmissionApi:
        if self._submissions is None:
            from essabu.einvoice.api.submissions import SubmissionApi
            self._submissions = SubmissionApi(self._http)
        return self._submissions
    @property
    def verification(self) -> VerificationApi:
        if self._verification is None:
            from essabu.einvoice.api.verification import VerificationApi
            self._verification = VerificationApi(self._http)
        return self._verification
    @property
    def compliance(self) -> ComplianceApi:
        if self._compliance is None:
            from essabu.einvoice.api.compliance import ComplianceApi
            self._compliance = ComplianceApi(self._http)
        return self._compliance
    @property
    def statistics(self) -> StatisticApi:
        if self._statistics is None:
            from essabu.einvoice.api.statistics import StatisticApi
            self._statistics = StatisticApi(self._http)
        return self._statistics
