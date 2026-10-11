# Personal Hub API Ecosystem

Hệ thống điều phối dữ liệu & tự động hóa trung tâm (Digital Brain) xây dựng bằng **Python (FastAPI)**.

---

## 🚀 Hướng dẫn cài đặt & Khởi chạy

### 1. Tạo Virtual Environment & Cài đặt thư viện
```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt trên Windows (PowerShell / Command Prompt)
.\venv\Scripts\activate

# Cài đặt dependencies
pip install -r requirements.txt
```

### 2. Cấu hình biến môi trường
File `.env` đã được tạo sẵn trong thư mục gốc. Nếu muốn test gửi tin nhắn về Telegram, hãy điền:
* `TELEGRAM_BOT_TOKEN`: Lấy từ `@BotFather`
* `TELEGRAM_CHAT_ID`: Chat ID của bạn (lấy từ `@userinfobot` hoặc `@getmyid_bot`)
* `API_KEY`: Key dùng cho các endpoint admin/device (mặc định: `phub_dev_key_123456`)

### 3. Chạy Server
```bash
uvicorn app.main:app --reload --port 8000
```

Mở trình duyệt truy cập Swagger UI: **http://127.0.0.1:8000/docs**

---

## 📌 Tổng hợp Endpoint theo 4 phân hệ

### 1. Content & Portfolio Hub (Public)
* `GET /api/v1/profile`: Trả về bio, skills, socials cho portfolio.
* `GET /api/v1/projects`: Danh sách dự án cá nhân, repo github, tags.

### 2. Notification & Dispatch Hub
* `POST /api/v1/notify/message`: Gửi tin nhắn liên hệ từ website về Telegram bot cá nhân.
* `POST /api/v1/notify/alert`: Bắn cảnh báo sự cố máy chủ (Yêu cầu header `X-API-Key`).

### 3. Activity & Telemetry Hub
* `GET /api/v1/status`: Trạng thái làm việc hiện tại (Online, Coding, Researching,...).
* `POST /api/v1/telemetry/log`: Ghi nhận log giờ code/nghiên cứu (Yêu cầu `X-API-Key`).
* `GET /api/v1/telemetry/metrics`: Số liệu thống kê để hiển thị biểu đồ trên website.

### 4. Hardware / Edge Bridge
* `POST /api/v1/device/heartbeat`: Ping sống/chết từ thiết bị IoT (Yêu cầu `X-API-Key`).
* `POST /api/v1/device/sensor`: Thu thập dữ liệu nhiệt độ/môi trường (Yêu cầu `X-API-Key`).
