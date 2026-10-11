from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

from app.modules.content.router import router as content_router
from app.modules.notify.router import router as notify_router
from app.modules.telemetry.router import router as telemetry_router
from app.modules.device.router import router as device_router

app = FastAPI(
    title=settings.APP_NAME,
    description="Hệ thống điều phối dữ liệu & tự động hóa trung tâm (Digital Brain Ecosystem)",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware (Cho phép frontend website kết nối)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Sub-services Routes
API_V1_PREFIX = "/api/v1"

app.include_router(content_router, prefix=API_V1_PREFIX, tags=["1. Content & Portfolio"])
app.include_router(notify_router, prefix=f"{API_V1_PREFIX}/notify", tags=["2. Notification & Dispatch"])
app.include_router(telemetry_router, prefix=API_V1_PREFIX, tags=["3. Activity & Telemetry"])
app.include_router(device_router, prefix=f"{API_V1_PREFIX}/device", tags=["4. Hardware & Edge Bridge"])


@app.get("/", tags=["Health Check"])
async def root():
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": "1.0.0",
        "docs": "/docs"
    }
