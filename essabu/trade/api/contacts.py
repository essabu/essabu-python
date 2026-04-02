"""API client for contacts operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class ContactsApi(BaseApi):
    """API client for contacts operations."""

    _resource_path = "/contacts"
