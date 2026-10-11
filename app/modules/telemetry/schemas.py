from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class StatusResponse(BaseModel):
    current_status: str
    focus_topic: str
    updated_at: str


class ActivityLogRequest(BaseModel):
    category: str  # Ví dụ: "coding", "reading", "research"
    duration_minutes: int
    note: Optional[str] = None


class TelemetryMetricsResponse(BaseModel):
    today_coding_minutes: int
    current_streak_days: int
    total_logs: int
