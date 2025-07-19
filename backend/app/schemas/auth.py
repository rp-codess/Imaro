from pydantic import BaseModel, validator
from typing import Optional
import re

class PhoneSendOTPRequest(BaseModel):
    phone_number: str
    
    @validator('phone_number')
    def validate_phone(cls, v):
        # Basic phone validation - adjust regex as needed
        if not re.match(r'^\+[1-9]\d{1,14}$', v):
            raise ValueError('Invalid phone number format. Use international format: +1234567890')
        return v

class PhoneVerifyOTPRequest(BaseModel):
    phone_number: str
    otp_code: str
    
    @validator('otp_code')
    def validate_otp(cls, v):
        if not re.match(r'^\d{6}$', v):
            raise ValueError('OTP must be 6 digits')
        return v

class GoogleLoginRequest(BaseModel):
    id_token: str

class CompleteProfileRequest(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    country: str
    privacy_policy_accepted: bool = True
    terms_accepted: bool = True
    
    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        if not v or len(v.strip()) < 1 or len(v.strip()) > 50:
            raise ValueError('Name must be between 1 and 50 characters')
        return v.strip()
    
    @validator('age')
    def validate_age(cls, v):
        if v < 13 or v > 120:
            raise ValueError('Age must be between 13 and 120')
        return v
    
    @validator('gender')
    def validate_gender(cls, v):
        if v not in ['male', 'female', 'other', 'prefer_not_to_say']:
            raise ValueError('Invalid gender. Must be one of: male, female, other, prefer_not_to_say')
        return v
    
    @validator('country')
    def validate_country(cls, v):
        # Basic country code validation - you can expand this
        if len(v) != 3 or not v.isupper():
            raise ValueError('Country must be 3-letter ISO code (e.g., USA, IND, GBR)')
        return v

class AuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user_id: str
    profile_completed: bool
    expires_in: int

class RefreshTokenRequest(BaseModel):
    refresh_token: str

class OTPResponse(BaseModel):
    success: bool
    message: str
