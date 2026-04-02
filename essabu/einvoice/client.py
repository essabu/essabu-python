"""EInvoice module client for the Essabu SDK."""

from __future__ import annotations

from functools import cached_property

from essabu.common.http_client import HttpClient
from essabu.einvoice.api.compliance import ComplianceApi
from essabu.einvoice.api.invoices import InvoicesApi
from essabu.einvoice.api.statistics import StatisticsApi
from essabu.einvoice.api.submissions import SubmissionsApi
from essabu.einvoice.api.verification import VerificationApi


class EInvoiceClient:
    """EInvoice module client providing access to all EInvoice API resources."""

    def __init__(self, http: HttpClient) -> None:
        self._http = http

    @cached_property
    def invoices(self) -> InvoicesApi:
        return InvoicesApi(self._http)

    @cached_property
    def submissions(self) -> SubmissionsApi:
        return SubmissionsApi(self._http)

    @cached_property
    def verification(self) -> VerificationApi:
        return VerificationApi(self._http)

    @cached_property
    def compliance(self) -> ComplianceApi:
        return ComplianceApi(self._http)

    @cached_property
    def statistics(self) -> StatisticsApi:
        return StatisticsApi(self._http)
