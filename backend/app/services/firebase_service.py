import firebase_admin
from firebase_admin import credentials, auth
from app.core.config import settings
import os

class FirebaseService:
    def __init__(self):
        if not firebase_admin._apps:
            # Initialize Firebase Admin SDK
            if os.path.exists(settings.FIREBASE_CREDENTIALS_PATH):
                cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
                firebase_admin.initialize_app(cred, {
                    'projectId': settings.FIREBASE_PROJECT_ID,
                })
            else:
                # For development/testing - you can also use environment variables
                firebase_admin.initialize_app()
    
    async def send_verification_code(self, phone_number: str) -> dict:
        """
        Send OTP to phone number
        Note: This is a placeholder. In production, you would use Firebase Auth REST API
        or implement your own OTP service with Firebase Admin SDK
        """
        try:
            # In production, you would make a call to Firebase Auth REST API
            # For now, we'll return a success response
            return {
                "success": True,
                "message": f"OTP sent to {phone_number}",
                "session_info": f"session_{phone_number}"  # This would be real session info
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Failed to send OTP: {str(e)}"
            }
    
    async def verify_phone_otp(self, phone_number: str, otp_code: str) -> dict:
        """
        Verify OTP code
        Note: This is a placeholder. In production, you would verify against Firebase
        """
        try:
            # For demo purposes, accept "123456" as valid OTP
            if otp_code == "123456":
                # Create a custom token for this phone number
                custom_token = auth.create_custom_token(phone_number.replace("+", "phone_"))
                return {
                    "success": True,
                    "custom_token": custom_token.decode('utf-8'),
                    "firebase_uid": phone_number.replace("+", "phone_"),
                    "phone_number": phone_number
                }
            else:
                return {
                    "success": False,
                    "message": "Invalid OTP code"
                }
        except Exception as e:
            return {
                "success": False,
                "message": f"OTP verification failed: {str(e)}"
            }
    
    async def verify_google_token(self, id_token: str) -> dict:
        """
        Verify Google ID token
        """
        try:
            # Verify the ID token
            decoded_token = auth.verify_id_token(id_token)
            
            return {
                "success": True,
                "firebase_uid": decoded_token['uid'],
                "email": decoded_token.get('email'),
                "name": decoded_token.get('name'),
                "picture": decoded_token.get('picture'),
                "email_verified": decoded_token.get('email_verified', False)
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Google token verification failed: {str(e)}"
            }
    
    async def verify_firebase_token(self, token: str) -> dict:
        """
        Verify Firebase ID token
        """
        try:
            decoded_token = auth.verify_id_token(token)
            return {
                "success": True,
                "firebase_uid": decoded_token['uid'],
                "email": decoded_token.get('email'),
                "phone_number": decoded_token.get('phone_number')
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Token verification failed: {str(e)}"
            }

firebase_service = FirebaseService()
