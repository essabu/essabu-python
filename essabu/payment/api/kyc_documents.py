"""API client for kyc documents operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class KycDocumentsApi(BaseApi):
    """API client for kyc documents operations."""

    _resource_path = "/kyc-documents"
