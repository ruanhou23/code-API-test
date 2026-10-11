from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class SocialLink(BaseModel):
    platform: str
    url: str


class ProfileResponse(BaseModel):
    name: str
    headline: str
    bio: str
    location: str
    skills: List[str]
    socials: List[SocialLink]


class Project(BaseModel):
    id: str
    title: str
    description: str
    tags: List[str]
    status: str
    github_url: Optional[str] = None
    demo_url: Optional[str] = None


class ProjectsResponse(BaseModel):
    total: int
    projects: List[Project]
