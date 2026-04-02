"""Session models."""

from pydantic import BaseModel


class SessionResponse(BaseModel):
    id: str
    user_id: str
    ip_address: str | None = None
    user_agent: str | None = None
    is_current: bool = False
    last_active_at: str
    created_at: str
