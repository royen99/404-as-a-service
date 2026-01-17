"""
Business logic for fetching and selecting 404 reasons.
Keeps routes thin and testable.
"""
import json
import random
from pathlib import Path
from typing import Dict, List
from functools import lru_cache
from app.core.config import settings


@lru_cache()
def _load_reasons() -> List[Dict[str, str]]:
    """
    Load reasons from JSON file and cache them.
    Because reading from disk every time is so inefficient 🚀
    """
    reasons_path = Path(settings.reasons_file)
    
    if not reasons_path.exists():
        # Fallback if file doesn't exist yet
        return [{
            "message": "The page you're looking for is on vacation",
            "reason": "It left no forwarding address. Rude, right?",
            "category": "missing"
        }]
    
    with open(reasons_path, "r") as f:
        data = json.load(f)
        return data.get("reasons", [])


async def get_random_reason() -> Dict[str, str]:
    """
    Get a random 404 reason.
    
    Returns:
        Dict with message, reason, and optional category
    """
    reasons = _load_reasons()
    return random.choice(reasons)


async def get_all_reasons() -> List[Dict[str, str]]:
    """Get all available 404 reasons."""
    return _load_reasons()


async def get_random_reason_by_category(category: str) -> Dict[str, str]:
    """
    Get a random 404 reason from a specific category.
    Falls back to random if category not found.
    
    Args:
        category: The category to filter by (e.g., 'gaming', 'tech-humor')
    
    Returns:
        Dict with message, reason, and category
    """
    reasons = _load_reasons()
    filtered = [r for r in reasons if r.get("category") == category]
    
    if not filtered:
        # Category not found, return random instead
        return random.choice(reasons)
    
    return random.choice(filtered)


def clear_cache():
    """Clear the reasons cache. Useful for testing or reloading data."""
    _load_reasons.cache_clear()
