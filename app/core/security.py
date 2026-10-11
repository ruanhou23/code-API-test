import hashlib
import hmac
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from app.core.config import settings

api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def hash_key(raw_key: str) -> str:
    """
    Băm API Key bằng thuật toán SHA-256.
    Không bao giờ lưu hoặc so sánh key dạng plaintext thô.
    """
    return hashlib.sha256(raw_key.strip().encode("utf-8")).hexdigest()


async def verify_api_key(api_key: str = Security(api_key_header)):
    """
    Xác thực API Key:
    1. Băm key nhận được từ client thành SHA-256 hash.
    2. So sánh với Master Hash cấu hình bằng hmac.compare_digest
       (Chống tấn công timing attack / phân tích thời gian phản hồi).
    """
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing API Key in header X-API-Key"
        )

    # Băm key của client gửi lên
    provided_key_hash = hash_key(api_key)

    # Master hash kỳ vọng từ biến môi trường
    # Nếu env là SHA-256 hash sẵn (64 ký tự hex) thì dùng luôn, nếu là plaintext thì băm
    target_hash = settings.API_KEY_HASH or hash_key(settings.API_KEY)

    # So sánh hmac an toàn chống timing attack
    if not hmac.compare_digest(provided_key_hash, target_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

    return api_key
