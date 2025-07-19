from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/")
def health_check():
    """
    Health check endpoint
    
    Returns the current status of the API service.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "Imaro Phase 1 API",
        "version": "1.0.0"
    }

@router.get("/db")
def database_health():
    """
    Database health check endpoint
    
    Returns the status of the database connection.
    """
    # In a real implementation, you would check database connectivity
    return {
        "status": "healthy",
        "database": "postgresql",
        "timestamp": datetime.utcnow().isoformat()
    }
