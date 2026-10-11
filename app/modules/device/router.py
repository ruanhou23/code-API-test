from fastapi import APIRouter, Depends
from datetime import datetime
from app.modules.device.schemas import HeartbeatRequest, SensorDataRequest
from app.core.security import verify_api_key

router = APIRouter()

DEVICES_STATUS = {}


@router.post(
    "/heartbeat",
    dependencies=[Depends(verify_api_key)],
    summary="Ping định kỳ từ phần cứng IoT / Raspberry Pi (Cần X-API-Key)"
)
async def device_heartbeat(payload: HeartbeatRequest):
    DEVICES_STATUS[payload.device_id] = {
        "uptime_seconds": payload.uptime_seconds,
        "ip_address": payload.ip_address,
        "last_seen": datetime.now().isoformat(),
        "status": "online"
    }
    return {
        "status": "acknowledged",
        "device_id": payload.device_id,
        "server_time": datetime.now().isoformat()
    }


@router.post(
    "/sensor",
    dependencies=[Depends(verify_api_key)],
    summary="Gửi dữ liệu cảm biến (Cần X-API-Key)"
)
async def record_sensor_data(payload: SensorDataRequest):
    return {
        "status": "recorded",
        "device_id": payload.device_id,
        "received_metrics": payload.metrics
    }
