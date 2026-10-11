from fastapi import APIRouter
from app.modules.content.schemas import ProfileResponse, ProjectsResponse

router = APIRouter()

# Dữ liệu tĩnh minh họa (có thể kết nối Database sau)
PROFILE_DATA = {
    "name": "Personal Hub Admin",
    "headline": "Backend & Cloud Engineer",
    "bio": "Xây dựng hệ sinh thái API cá nhân và các hệ thống tự động hóa tập trung.",
    "location": "Vietnam",
    "skills": ["Python", "FastAPI", "PostgreSQL", "Redis", "Docker", "Linux"],
    "socials": [
        {"platform": "GitHub", "url": "https://github.com"},
        {"platform": "LinkedIn", "url": "https://linkedin.com"}
    ]
}

PROJECTS_DATA = [
    {
        "id": "proj-1",
        "title": "Personal Hub API Ecosystem",
        "description": "Digital brain hợp nhất toàn bộ dữ liệu, activity và notification.",
        "tags": ["FastAPI", "Python", "Telegram Bot", "PostgreSQL"],
        "status": "in-progress",
        "github_url": "https://github.com/your-username/personal-hub-api",
        "demo_url": "http://localhost:8000/docs"
    },
    {
        "id": "proj-2",
        "title": "Personal Portfolio & Blog",
        "description": "Trang web cá nhân hiển thị dữ liệu live từ Personal Hub API.",
        "tags": ["Next.js", "TailwindCSS"],
        "status": "planned",
        "github_url": None,
        "demo_url": None
    }
]


@router.get("/profile", response_model=ProfileResponse, summary="Lấy thông tin profile công khai")
async def get_profile():
    return PROFILE_DATA


@router.get("/projects", response_model=ProjectsResponse, summary="Lấy danh sách dự án")
async def get_projects():
    return {
        "total": len(PROJECTS_DATA),
        "projects": PROJECTS_DATA
    }
