"""
Main FastAPI application entry point.
Serves creative 404 errors as both JSON API and HTML pages.
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.routers import api, web
from app.core.config import settings

# Setup Jinja2 templates - because templating makes life easier 🎨
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

# Let's make 404s fun again 🚀
app = FastAPI(
    title="404-as-a-Service",
    description="A microservice that serves creative 404 errors with personality",
    version="0.1.0",
    docs_url="/docs",  # Keep Swagger UI accessible
)

# Include routers
app.include_router(api.router, prefix="/api/v1", tags=["API"])
app.include_router(web.router, tags=["Web UI"])


@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "ok", "service": "404-as-a-service"}


# Global 404 handler - serves creative 404s as JSON or HTML
@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    """Catch-all 404 handler that serves creative error messages."""
    accept = request.headers.get("accept", "")
    
    if "application/json" in accept or request.url.path.startswith("/api"):
        # Return JSON response for API clients
        from app.services.reason_service import get_random_reason
        reason_data = await get_random_reason()
        return JSONResponse(
            status_code=404,
            content={
                "error": "Not Found",
                "status_code": 404,
                **reason_data
            }
        )
    else:
        # Render beautiful HTML for browser clients 🎨
        from app.services.reason_service import get_random_reason
        import random
        
        reason_data = await get_random_reason()
        
        return templates.TemplateResponse(
            "404.html",
            {
                "request": request,
                "message": reason_data["message"],
                "reason": reason_data["reason"],
                "category": reason_data.get("category", "modern"),
                "visitor_count": random.randint(1337, 999999)  # Fun fake stat 😜
            },
            status_code=404
        )
