"""Customer model."""

from __future__ import annotations

from typing import Any


class Customer:
    """Represents a customer resource."""

    def __init__(self, data: dict[str, Any]):
        self.id: str = data.get("id", "")
        self.status: str = data.get("status", "")
        self.status_label: str = data.get("statusLabel", "")
        self.status_color: str = data.get("statusColor", "")
        self.created_at: str | None = data.get("createdAt")
        self.updated_at: str | None = data.get("updatedAt")
        self._raw = data

    def to_dict(self) -> dict[str, Any]:
        """Return the raw API response data."""
        return self._raw

    def __getattr__(self, name: str) -> Any:
        """Allow access to any field from the raw API response."""
        if name.startswith("_"):
            raise AttributeError(name)
        parts = name.split("_")
        camel = parts[0] + "".join(p.capitalize() for p in parts[1:])
        if camel in self._raw:
            return self._raw[camel]
        if name in self._raw:
            return self._raw[name]
        raise AttributeError(f"no attribute '{name}'")

    def __repr__(self) -> str:
        return f"Customer(id={self.id!r})"
