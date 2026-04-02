"""API client for activities operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class ActivitiesApi(BaseApi):
    """API client for activities operations."""

    _resource_path = "/activities"
