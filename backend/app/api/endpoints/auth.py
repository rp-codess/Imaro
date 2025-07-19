from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.auth import (
    PhoneSendOTPRequest, 
    PhoneVerifyOTPRequest, 
    GoogleLoginRequest, 
    CompleteProfileRequest,
    AuthResponse,
    RefreshTokenRequest,
    OTPResponse
)
from app.schemas.user import UserResponse
from app.services.auth_service import auth_service
from app.services.user_service import user_service
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/phone/send-otp", response_model=OTPResponse)
async def send_phone_otp(request: PhoneSendOTPRequest):
    """
    Send OTP to phone number
    
    Sends a 6-digit OTP code to the provided phone number for verification.
    The phone number must be in international format (e.g., +1234567890).
    
    **Note**: For demo purposes, the actual SMS is not sent. 
    Use OTP code "123456" to verify.
    """
    try:
        result = await auth_service.send_phone_otp(request.phone_number)
        return OTPResponse(
            success=result["success"],
            message=result["message"]
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to send OTP: {str(e)}"
        )

@router.post("/phone/verify-otp", response_model=AuthResponse)
async def verify_phone_otp(
    request: PhoneVerifyOTPRequest,
    db: Session = Depends(get_db)
):
    """
    Verify phone OTP and authenticate user
    
    Verifies the OTP code sent to the phone number and returns authentication tokens.
    If this is a new user, they will need to complete their profile.
    
    **Demo OTP**: Use "123456" as the OTP code for testing.
    """
    try:
        auth_response = await auth_service.verify_phone_otp(
            db, request.phone_number, request.otp_code
        )
        return auth_response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Authentication failed: {str(e)}"
        )

@router.post("/google/login", response_model=AuthResponse)
async def google_login(
    request: GoogleLoginRequest,
    db: Session = Depends(get_db)
):
    """
    Authenticate user with Google ID token
    
    Verifies the Google ID token and returns authentication tokens.
    The ID token should be obtained from Google Sign-In on the frontend.
    """
    try:
        auth_response = await auth_service.google_login(db, request.id_token)
        return auth_response
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Google authentication failed: {str(e)}"
        )

@router.post("/complete-profile", response_model=UserResponse)
async def complete_profile(
    request: CompleteProfileRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Complete user profile
    
    Updates the user's profile with their personal information.
    This endpoint is typically called after initial authentication
    for new users who haven't completed their profile yet.
    """
    if current_user.profile_completed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile is already completed"
        )
    
    try:
        profile_data = {
            "first_name": request.first_name,
            "last_name": request.last_name,
            "age": request.age,
            "gender": request.gender,
            "country": request.country,
            "privacy_policy_accepted": request.privacy_policy_accepted,
            "terms_accepted": request.terms_accepted,
            "privacy_policy_version": "1.0",
            "terms_version": "1.0"
        }
        
        updated_user = user_service.complete_profile(db, current_user.id, profile_data)
        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        return updated_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to complete profile: {str(e)}"
        )

@router.post("/refresh")
async def refresh_token(request: RefreshTokenRequest):
    """
    Refresh access token
    
    Uses a refresh token to generate a new access token.
    Refresh tokens have a longer expiration time than access tokens.
    """
    try:
        result = auth_service.refresh_access_token(request.refresh_token)
        return result
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Token refresh failed: {str(e)}"
        )

@router.post("/logout")
async def logout(current_user: User = Depends(get_current_user)):
    """
    Logout user
    
    Logs out the current user. In a production environment,
    you might want to blacklist the token or clear server-side sessions.
    """
    return {"message": "Successfully logged out"}

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """
    Get current user information
    
    Returns the profile information of the currently authenticated user.
    """
    return current_user
