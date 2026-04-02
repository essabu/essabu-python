"""API client for kyc profiles operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class KycProfilesApi(BaseApi):
    """API client for kyc profiles operations."""

    _resource_path = "/kyc-profiles"
