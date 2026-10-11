from pydantic import BaseModel, EmailStr
from typing import Optional, Literal


class ContactMessageRequest(BaseModel):
    sender_name: str
    sender_email: Optional[str] = None
    message: str


class AlertRequest(BaseModel):
    level: Literal["INFO", "WARNING", "CRITICAL"] = "WARNING"
    source: str
    title: str
    details: Optional[str] = None


class DispatchResponse(BaseModel):
    success: bool
    channel: str
    message: str
