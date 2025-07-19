import random
import string
from datetime import datetime, timedelta
from typing import Dict, Optional
from twilio.rest import Client
from app.core.config import settings
import redis
import json

class TwilioService:
    def __init__(self):
        """Initialize Twilio client"""
        self.client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        self.messaging_service_sid = settings.TWILIO_MESSAGING_SERVICE_SID
        
        # In production, use Redis for OTP storage
        # For development, use in-memory storage
        self.otp_storage = {}  # Will be replaced with Redis in production
    
    def generate_otp(self, length: int = 6) -> str:
        """Generate a random OTP code"""
        return ''.join(random.choices(string.digits, k=length))
    
    def store_otp(self, phone_number: str, otp: str, expires_in_minutes: int = 5) -> None:
        """Store OTP with expiration time"""
        expiry_time = datetime.utcnow() + timedelta(minutes=expires_in_minutes)
        self.otp_storage[phone_number] = {
            'otp': otp,
            'expires_at': expiry_time,
            'attempts': 0
        }
    
    def verify_otp(self, phone_number: str, provided_otp: str) -> Dict[str, any]:
        """Verify OTP code"""
        stored_data = self.otp_storage.get(phone_number)
        
        if not stored_data:
            return {
                'success': False,
                'message': 'No OTP found for this phone number'
            }
        
        # Check if OTP has expired
        if datetime.utcnow() > stored_data['expires_at']:
            del self.otp_storage[phone_number]
            return {
                'success': False,
                'message': 'OTP has expired. Please request a new one.'
            }
        
        # Check attempt limit
        if stored_data['attempts'] >= 3:
            del self.otp_storage[phone_number]
            return {
                'success': False,
                'message': 'Too many failed attempts. Please request a new OTP.'
            }
        
        # Verify OTP
        if stored_data['otp'] == provided_otp:
            # OTP is correct, remove from storage
            del self.otp_storage[phone_number]
            return {
                'success': True,
                'message': 'OTP verified successfully'
            }
        else:
            # Increment attempt counter
            stored_data['attempts'] += 1
            return {
                'success': False,
                'message': f'Invalid OTP. {3 - stored_data["attempts"]} attempts remaining.'
            }
    
    async def send_sms(self, phone_number: str, message: str) -> Dict[str, any]:
        """Send SMS using Twilio"""
        try:
            message = self.client.messages.create(
                messaging_service_sid=self.messaging_service_sid,
                body=message,
                to=phone_number
            )
            
            return {
                'success': True,
                'message': 'SMS sent successfully',
                'sid': message.sid
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Failed to send SMS: {str(e)}'
            }
    
    async def send_otp_sms(self, phone_number: str) -> Dict[str, any]:
        """Send OTP via SMS"""
        try:
            # Generate OTP
            otp = self.generate_otp()
            
            # Create message
            message = f"Your Imaro verification code is: {otp}. This code will expire in 5 minutes. Do not share this code with anyone."
            
            # Send SMS
            sms_result = await self.send_sms(phone_number, message)
            
            if sms_result['success']:
                # Store OTP for verification
                self.store_otp(phone_number, otp)
                
                return {
                    'success': True,
                    'message': f'OTP sent to {phone_number}',
                    'sid': sms_result['sid']
                }
            else:
                return sms_result
                
        except Exception as e:
            return {
                'success': False,
                'message': f'Failed to send OTP: {str(e)}'
            }
    
    def cleanup_expired_otps(self) -> None:
        """Clean up expired OTPs from storage"""
        current_time = datetime.utcnow()
        expired_numbers = [
            phone for phone, data in self.otp_storage.items()
            if current_time > data['expires_at']
        ]
        
        for phone in expired_numbers:
            del self.otp_storage[phone]

# For development/demo purposes
class MockTwilioService(TwilioService):
    """Mock Twilio service for development when Twilio credentials are not available"""
    
    def __init__(self):
        # Don't initialize Twilio client in mock mode
        self.otp_storage = {}
        self.demo_otp = "123456"  # Fixed OTP for demo
    
    async def send_sms(self, phone_number: str, message: str) -> Dict[str, any]:
        """Mock SMS sending"""
        print(f"📱 MOCK SMS to {phone_number}: {message}")
        return {
            'success': True,
            'message': 'SMS sent successfully (MOCK MODE)',
            'sid': 'mock_sid_12345'
        }
    
    async def send_otp_sms(self, phone_number: str) -> Dict[str, any]:
        """Send mock OTP"""
        try:
            # Use demo OTP
            otp = self.demo_otp
            
            # Create message
            message = f"Your Imaro verification code is: {otp}. This code will expire in 5 minutes. (DEMO MODE)"
            
            # Mock send SMS
            sms_result = await self.send_sms(phone_number, message)
            
            # Store OTP for verification
            self.store_otp(phone_number, otp)
            
            return {
                'success': True,
                'message': f'Demo OTP sent to {phone_number}. Use code: {otp}',
                'demo_otp': otp,  # Include in response for demo
                'sid': sms_result['sid']
            }
                
        except Exception as e:
            return {
                'success': False,
                'message': f'Failed to send demo OTP: {str(e)}'
            }

# Create service instance
def get_twilio_service() -> TwilioService:
    """Get Twilio service instance (real or mock based on configuration)"""
    try:
        # Try to create real Twilio service
        if (hasattr(settings, 'TWILIO_ACCOUNT_SID') and 
            settings.TWILIO_ACCOUNT_SID and 
            settings.TWILIO_ACCOUNT_SID != 'your-twilio-account-sid'):
            return TwilioService()
        else:
            # Use mock service for development
            print("⚠️  Using Mock Twilio Service (Demo Mode)")
            return MockTwilioService()
    except Exception as e:
        print(f"⚠️  Twilio setup failed, using Mock Service: {e}")
        return MockTwilioService()

# Global service instance
twilio_service = get_twilio_service()
