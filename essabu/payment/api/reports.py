"""API client for reports operations."""

from __future__ import annotations

from essabu.payment.api.base import BaseApi


class ReportsApi(BaseApi):
    """API client for reports operations."""

    _resource_path = "/reports"
