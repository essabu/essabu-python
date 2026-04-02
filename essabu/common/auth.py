"""Authentication utilities for the Essabu SDK."""

from __future__ import annotations

from essabu.config import EssabuConfig


def build_auth_headers(config: EssabuConfig) -> dict[str, str]:
    """Build authentication headers from the SDK configuration."""
    headers: dict[str, str] = {
        "Authorization": f"Bearer {config.api_key}",
        "X-Tenant-Id": config.tenant_id,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "essabu-python/0.1.0",
    }
    return headers
