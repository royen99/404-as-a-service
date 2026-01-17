"""
API routes for JSON responses.
External sites can call these endpoints to get 404 data.
"""

from fastapi import APIRouter

from app.services.reason_service import get_all_reasons, get_random_reason

router = APIRouter()


@router.get("/404")
async def get_404():
    """
    Get a random 404 error with a creative reason.

    Returns:
        JSON with status_code, message, and reason
    """
    reason_data = await get_random_reason()
    return {"status_code": 404, "error": "Not Found", **reason_data}


@router.get("/404/random")
async def get_random_404():
    """Alias for /404 endpoint - some folks like explicit naming."""
    return await get_404()


@router.get("/reasons")
async def list_all_reasons():
    """
    Get all available 404 reasons.
    Useful for debugging or building your own selection logic.
    """
    reasons = await get_all_reasons()
    return {"total": len(reasons), "reasons": reasons}
