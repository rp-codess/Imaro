from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.router import api_router

# Create FastAPI instance with comprehensive metadata
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="""
    # Imaro Phase 1 API

    A comprehensive authentication and user management API built with FastAPI and Firebase.

    ## Features

    * **Phone Authentication**: OTP-based phone number verification
    * **Google Authentication**: OAuth integration with Google Sign-In
    * **User Management**: Complete user profile management
    * **JWT Tokens**: Secure access and refresh token system
    * **Database Integration**: PostgreSQL with SQLAlchemy ORM

    ## Authentication Methods

    ### Phone Authentication
    1. Send OTP to phone number
    2. Verify OTP to get authentication tokens
    3. Complete profile if new user

    ### Google Authentication
    1. Verify Google ID token
    2. Get authentication tokens
    3. Complete profile if needed

    ## Security
    - JWT tokens with configurable expiration
    - Firebase Admin SDK integration
    - Secure password hashing
    - CORS protection

    ## Database
    - PostgreSQL database
    - User profiles with minimal data collection
    - Privacy and terms acceptance tracking
    """,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", tags=["root"])
def read_root():
    """
    Root endpoint
    
    Returns basic information about the API service.
    """
    return {
        "message": "Imaro Phase 1 API",
        "version": settings.VERSION,
        "docs": "/docs",
        "redoc": "/redoc",
        "health": f"{settings.API_V1_STR}/health"
    }

# Health check at root level
@app.get("/health", tags=["health"])
def root_health_check():
    """
    Quick health check endpoint at root level
    """
    return {"status": "healthy", "service": "Imaro Phase 1 API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG
    )
