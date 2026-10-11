from pydantic import BaseModel
from typing import Optional, Dict, Any


class HeartbeatRequest(BaseModel):
    device_id: str
    uptime_seconds: int
    ip_address: Optional[str] = None


class SensorDataRequest(BaseModel):
    device_id: str
    metrics: Dict[str, Any]  # e.g., {"temperature": 28.5, "humidity": 70, "voltage": 3.3}
