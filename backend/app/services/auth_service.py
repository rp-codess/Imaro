from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.core.security import create_access_token, create_refresh_token, verify_token
from app.services.firebase_service import firebase_service
from app.services.user_service import user_service
from app.schemas.user import UserCreate
from app.schemas.auth import AuthResponse
from app.core.config import settings
import uuid

class AuthService:
    
    async def send_phone_otp(self, phone_number: str) -> dict:
        """Send OTP to phone number"""
        return await firebase_service.send_verification_code(phone_number)
    
    async def verify_phone_otp(self, db: Session, phone_number: str, otp_code: str) -> AuthResponse:
        """Verify phone OTP and authenticate user"""
        # Verify OTP with Firebase
        verification_result = await firebase_service.verify_phone_otp(phone_number, otp_code)
        
        if not verification_result["success"]:
            raise ValueError(verification_result["message"])
        
        firebase_uid = verification_result["firebase_uid"]
        
        # Check if user exists
        user = user_service.get_user_by_firebase_uid(db, firebase_uid)
        
        if not user:
            # Create new user with minimal info
            user_data = UserCreate(
                firebase_uid=firebase_uid,
                auth_method="phone",
                phone_number=phone_number,
                first_name="",  # Will be completed later
                last_name="",   # Will be completed later
                country="",     # Will be completed later
            )
            user = user_service.create_user(db, user_data)
        
        # Update last login
        user.last_login_at = datetime.utcnow()
        db.commit()
        
        # Generate tokens
        access_token = create_access_token({"sub": str(user.id), "firebase_uid": firebase_uid})
        refresh_token = create_refresh_token({"sub": str(user.id), "firebase_uid": firebase_uid})
        
        return AuthResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            user_id=str(user.id),
            profile_completed=user.profile_completed,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
    
    async def google_login(self, db: Session, id_token: str) -> AuthResponse:
        """Authenticate user with Google ID token"""
        # Verify Google token with Firebase
        verification_result = await firebase_service.verify_google_token(id_token)
        
        if not verification_result["success"]:
            raise ValueError(verification_result["message"])
        
        firebase_uid = verification_result["firebase_uid"]
        email = verification_result["email"]
        name = verification_result.get("name", "")
        
        # Check if user exists
        user = user_service.get_user_by_firebase_uid(db, firebase_uid)
        
        if not user:
            # Extract first and last name from Google name
            name_parts = name.split() if name else ["", ""]
            first_name = name_parts[0] if len(name_parts) > 0 else ""
            last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
            
            # Create new user
            user_data = UserCreate(
                firebase_uid=firebase_uid,
                auth_method="google",
                email=email,
                first_name=first_name,
                last_name=last_name,
                country="",  # Will be completed later
            )
            user = user_service.create_user(db, user_data)
        
        # Update last login
        user.last_login_at = datetime.utcnow()
        if verification_result.get("email_verified"):
            user.is_email_verified = True
        db.commit()
        
        # Generate tokens
        access_token = create_access_token({"sub": str(user.id), "firebase_uid": firebase_uid})
        refresh_token = create_refresh_token({"sub": str(user.id), "firebase_uid": firebase_uid})
        
        return AuthResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            user_id=str(user.id),
            profile_completed=user.profile_completed,
            expires_in=settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        )
    
    def refresh_access_token(self, refresh_token: str) -> dict:
        """Refresh access token using refresh token"""
        payload = verify_token(refresh_token, "refresh")
        if not payload:
            raise ValueError("Invalid refresh token")
        
        user_id = payload.get("sub")
        firebase_uid = payload.get("firebase_uid")
        
        # Generate new access token
        access_token = create_access_token({"sub": user_id, "firebase_uid": firebase_uid})
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
        }
    
    def get_current_user_id(self, token: str) -> str:
        """Get current user ID from access token"""
        payload = verify_token(token, "access")
        if not payload:
            raise ValueError("Invalid or expired token")
        
        return payload.get("sub")

auth_service = AuthService()
