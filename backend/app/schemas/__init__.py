"""
Pydantic schemas for Imaro Backend

Contains request/response models for API validation and serialization.
"""

# Import all schemas for easy access
from .auth import (
    PhoneSendOTPRequest,
    PhoneVerifyOTPRequest,
    GoogleLoginRequest,
    CompleteProfileRequest,
    RefreshTokenRequest,
    AuthResponse,
    OTPResponse
)
from .user import (
    UserBase,
    UserCreate,
    UserUpdate,
    UserResponse,
    UserProfile
)

__all__ = [
    # Auth schemas
    "PhoneSendOTPRequest",
    "PhoneVerifyOTPRequest", 
    "GoogleLoginRequest",
    "CompleteProfileRequest",
    "RefreshTokenRequest",
    "AuthResponse",
    "OTPResponse",
    # User schemas
    "UserBase",
    "UserCreate",
    "UserUpdate", 
    "UserResponse",
    "UserProfile"
]