import hashlib
import secrets


def generate_secure_api_key(prefix: str = "phub") -> tuple[str, str]:
    """
    Tạo ra một API Key ngẫu nhiên an toàn mật mã học (cryptographically secure)
    và mã băm SHA-256 tương ứng của nó.
    
    Returns:
        (raw_key, key_hash)
    """
    random_bytes = secrets.token_hex(24)
    raw_key = f"{prefix}_{random_bytes}"
    key_hash = hashlib.sha256(raw_key.encode("utf-8")).hexdigest()
    return raw_key, key_hash


if __name__ == "__main__":
    raw, hashed = generate_secure_api_key()
    print("=" * 60)
    print("🔑 CÔNG CỤ TẠO API KEY BẢO MẬT CHO PERSONAL HUB API")
    print("=" * 60)
    print(f"\n[1] RAW API KEY (Đưa cho client / IoT thiết bị / script sử dụng):")
    print(f"👉  {raw}")
    print(f"\n[2] SHA-256 HASH (Lưu vào .env hoặc database máy chủ - API_KEY_HASH):")
    print(f"👉  {hashed}")
    print("\nLưu ý: Không bao giờ commit Raw Key lên GitHub!")
    print("=" * 60)
