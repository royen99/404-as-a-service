"""
Web UI routes for HTML responses.
Renders beautiful 404 pages for browser clients with category-specific themes.
"""

import random
from pathlib import Path

from fastapi import APIRouter, Query, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Setup templates - Jinja2 magic happens here ✨
templates = Jinja2Templates(directory=str(Path(__file__).parent.parent / "templates"))

# Available categories for theming
CATEGORIES = [
    "philosophical",
    "sassy",
    "playful",
    "absurd",
    "tech-humor",
    "sarcastic",
    "workplace",
    "fantasy",
    "modern",
    "gaming",
    "science",
    "dark-humor",
]


@router.get("/")
async def home(request: Request):
    """Landing page with service overview and examples."""
    return templates.TemplateResponse("home.html", {"request": request, "categories": CATEGORIES})


@router.get("/404")
async def web_404(request: Request, category: str | None = Query(None)):
    """
    Render a pretty HTML 404 page.
    Optional category parameter for themed 404s.
    """
    from app.services.reason_service import get_random_reason, get_random_reason_by_category

    # Get reason based on category if specified
    if category and category in CATEGORIES:
        reason_data = await get_random_reason_by_category(category)
    else:
        reason_data = await get_random_reason()

    return templates.TemplateResponse(
        "404.html",
        {
            "request": request,
            "message": reason_data["message"],
            "reason": reason_data["reason"],
            "category": reason_data.get("category", "modern"),
            "visitor_count": random.randint(1337, 999999),  # Because stats are fun
        },
        status_code=404,
    )


#     reason_data = await get_random_reason()
#     return templates.TemplateResponse("404.html", {
#         "request": request,
#         **reason_data
#     })
