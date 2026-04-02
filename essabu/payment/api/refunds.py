"""API client for refunds operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class RefundsApi(BaseApi):
    """API client for refunds operations."""

    _resource_path = "/refunds"
