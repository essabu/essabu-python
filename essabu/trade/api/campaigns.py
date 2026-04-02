"""API client for campaigns operations."""

from __future__ import annotations

from essabu.trade.api.base import BaseApi


class CampaignsApi(BaseApi):
    """API client for campaigns operations."""

    _resource_path = "/campaigns"
