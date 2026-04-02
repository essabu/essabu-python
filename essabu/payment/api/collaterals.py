"""API client for collaterals operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class CollateralsApi(BaseApi):
    """API client for collaterals operations."""

    _resource_path = "/collaterals"
