"""
Tests for reason service logic.
"""

import pytest
from app.services.reason_service import get_random_reason, get_all_reasons, get_random_reason_by_category, clear_cache


@pytest.mark.asyncio
async def test_get_random_reason():
    """Should return a valid reason structure."""
    reason = await get_random_reason()

    assert isinstance(reason, dict)
    assert "message" in reason
    assert "reason" in reason
    assert isinstance(reason["message"], str)
    assert isinstance(reason["reason"], str)


@pytest.mark.asyncio
async def test_get_all_reasons():
    """Should return list of all reasons."""
    reasons = await get_all_reasons()

    assert isinstance(reasons, list)
    assert len(reasons) > 0

    # Each reason should have required structure
    for reason in reasons:
        assert "message" in reason
        assert "reason" in reason


@pytest.mark.asyncio
async def test_clear_cache():
    """Cache clearing should work without errors."""
    # Get reasons to populate cache
    await get_all_reasons()

    # Clear cache
    clear_cache()

    # Should still work after clearing
    reasons = await get_all_reasons()
    assert len(reasons) > 0


@pytest.mark.asyncio
async def test_get_random_reason_by_category():
    """Should return reason from specific category."""
    reason = await get_random_reason_by_category("gaming")

    assert isinstance(reason, dict)
    assert "message" in reason
    assert "reason" in reason
    assert "category" in reason
    # Should be gaming category
    assert reason["category"] == "gaming"


@pytest.mark.asyncio
async def test_get_random_reason_by_invalid_category():
    """Invalid category should fallback to random."""
    reason = await get_random_reason_by_category("this-does-not-exist")

    assert isinstance(reason, dict)
    assert "message" in reason
    assert "reason" in reason
    # Should still return a valid reason, just not the requested category
    assert isinstance(reason.get("category"), str)
