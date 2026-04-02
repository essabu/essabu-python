"""API client for customers operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class CustomersApi(BaseApi):
    """API client for customers operations."""

    _resource_path = "/customers"
