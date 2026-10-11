from fastapi import APIRouter, Depends
from datetime import datetime
from app.modules.telemetry.schemas import StatusResponse, ActivityLogRequest, TelemetryMetricsResponse
from app.core.security import verify_api_key

router = APIRouter()

# Dữ liệu mẫu trong bộ nhớ
CURRENT_STATUS = {
    "current_status": "Coding & Researching",
    "focus_topic": "FastAPI Personal Ecosystem",
    "updated_at": datetime.now().isoformat()
}

LOGS = []


@router.get("/status", response_model=StatusResponse, summary="Trạng thái làm việc hiện tại (Public)")
async def get_current_status():
    return CURRENT_STATUS


@router.post(
    "/telemetry/log",
    dependencies=[Depends(verify_api_key)],
    summary="Ghi log hoạt động học tập/code (Cần X-API-Key)"
)
async def log_activity(payload: ActivityLogRequest):
    entry = {
        "id": len(LOGS) + 1,
        "category": payload.category,
        "duration_minutes": payload.duration_minutes,
        "note": payload.note,
        "timestamp": datetime.now().isoformat()
    }
    LOGS.append(entry)
    return {"success": True, "logged_entry": entry}


@router.get("/telemetry/metrics", response_model=TelemetryMetricsResponse, summary="Tổng hợp số liệu thống kê (Public)")
async def get_metrics():
    total_minutes = sum(item["duration_minutes"] for item in LOGS if item["category"] == "coding")
    return {
        "today_coding_minutes": total_minutes or 120,  # Mock dữ liệu mẫu
        "current_streak_days": 14,
        "total_logs": len(LOGS)
    }
