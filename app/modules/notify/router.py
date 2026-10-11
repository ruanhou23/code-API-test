from fastapi import APIRouter, Depends
from app.modules.notify.schemas import ContactMessageRequest, AlertRequest, DispatchResponse
from app.modules.notify.service import send_telegram_message
from app.core.security import verify_api_key

router = APIRouter()


@router.post("/message", response_model=DispatchResponse, summary="Gửi tin nhắn liên hệ từ website")
async def send_contact_message(payload: ContactMessageRequest):
    """
    Endpoint công khai (dành cho form liên hệ trên Portfolio/Website).
    Tự động format và bắn notification về Telegram.
    """
    email_text = f" ({payload.sender_email})" if payload.sender_email else ""
    telegram_content = (
        f"📬 *New Contact Message!*\n\n"
        f"👤 *From:* `{payload.sender_name}`{email_text}\n"
        f"💬 *Message:*\n{payload.message}"
    )

    sent = await send_telegram_message(telegram_content)
    return {
        "success": sent,
        "channel": "telegram",
        "message": "Notification dispatched to Telegram" if sent else "Bot not configured or failed to send"
    }


@router.post(
    "/alert",
    response_model=DispatchResponse,
    dependencies=[Depends(verify_api_key)],
    summary="Bắn cảnh báo hệ thống (Yêu cầu X-API-Key)"
)
async def send_system_alert(payload: AlertRequest):
    """
    Endpoint bảo vệ bằng API Key dành cho webhook, script cron hoặc server monitor.
    """
    icon = "🚨" if payload.level == "CRITICAL" else ("⚠️" if payload.level == "WARNING" else "ℹ️")
    telegram_content = (
        f"{icon} *System Alert [{payload.level}]*\n\n"
        f"🏷️ *Source:* `{payload.source}`\n"
        f"📌 *Title:* *{payload.title}*\n"
    )
    if payload.details:
        telegram_content += f"📝 *Details:*\n`{payload.details}`"

    sent = await send_telegram_message(telegram_content)
    return {
        "success": sent,
        "channel": "telegram",
        "message": f"Alert [{payload.level}] dispatched" if sent else "Failed to send alert"
    }
