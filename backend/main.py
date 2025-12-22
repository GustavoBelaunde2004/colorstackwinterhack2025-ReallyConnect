from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

# INIT FastAPI
app = FastAPI(
    title="ReallyConnect API",
    description="Mentorship matching platform API",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #FRONT URL HEREE
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint with API information."""
    return {
        "message": "ReallyConnect API",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint for monitoring."""
    return {"status": "healthy"}


# EXAMPLE
# @app.get("/protected")
# async def protected_route(user_id: UUID = Depends(get_current_user)):
#     return {"user_id": str(user_id), "message": "This is a protected route"}

