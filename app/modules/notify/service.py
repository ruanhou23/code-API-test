import httpx
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)


async def send_telegram_message(text: str) -> bool:
    """
    Gửi tin nhắn về Telegram Chat qua Bot API.
    """
    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID

    if not bot_token or not chat_id:
        logger.warning("Telegram Bot Token hoặc Chat ID chưa được cấu hình trong .env.")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                return True
            else:
                logger.error(f"Telegram API Error: {resp.status_code} - {resp.text}")
                return False
    except Exception as e:
        logger.error(f"Lỗi kết nối Telegram: {e}")
        return False
