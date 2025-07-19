"""
API endpoints for Imaro Backend

Contains all endpoint definitions for authentication, user management, and health checks.
"""

from .auth import router as auth_router
from .users import router as users_router
from .health import router as health_router

__all__ = ["auth_router", "users_router", "health_router"]