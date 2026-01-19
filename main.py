from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import random
from typing import Optional
import uvicorn
from responses import LIES

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Lies as a Service (LaaS)",
    description="A humorous API that generates believable lies across various categories",
    version="1.0.0",
    docs_url="/",
)

# Add rate limiting error handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/lie")
@limiter.limit("120/minute")
async def get_lie(
    request: Request,
    category: Optional[str] = Query(None, description="Category of lie to return")
):
    """
    Get a random humorous workplace excuse/lie.
    
    - **category**: Optional category filter (sick, meeting, deadline, remote, technical, manager, tech, random)
    """
    if category:
        category = category.lower()
        if category not in LIES:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid category. Available categories: {', '.join(LIES.keys())}"
            )
        lie = random.choice(LIES[category])
        return JSONResponse(content={
            "lie": lie,
            "category": category
        })
    
    # Random category if none specified
    category = random.choice(list(LIES.keys()))
    lie = random.choice(LIES[category])
    
    return JSONResponse(content={
        "lie": lie,
        "category": category
    })


@app.get("/api/categories")
@limiter.limit("120/minute")
async def get_categories(request: Request):
    """
    Get all available lie categories.
    """
    return JSONResponse(content={
        "categories": list(LIES.keys()),
        "total": len(LIES.keys())
    })


@app.get("/health")
async def health_check():
    """
    Health check endpoint.
    """
    return JSONResponse(content={"status": "healthy", "service": "Lies as a Service"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
