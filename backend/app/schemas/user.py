from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
import uuid

class UserBase(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int] = None
    gender: Optional[str] = None
    country: str
    
    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        if not v or len(v.strip()) < 1 or len(v.strip()) > 50:
            raise ValueError('Name must be between 1 and 50 characters')
        return v.strip()
    
    @validator('age')
    def validate_age(cls, v):
        if v is not None and (v < 13 or v > 120):
            raise ValueError('Age must be between 13 and 120')
        return v
    
    @validator('gender')
    def validate_gender(cls, v):
        if v is not None and v not in ['male', 'female', 'other', 'prefer_not_to_say']:
            raise ValueError('Invalid gender')
        return v

class UserCreate(UserBase):
    firebase_uid: str
    auth_method: str
    phone_number: Optional[str] = None
    email: Optional[str] = None

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    country: Optional[str] = None
    
    @validator('first_name', 'last_name')
    def validate_names(cls, v):
        if v is not None and (not v or len(v.strip()) < 1 or len(v.strip()) > 50):
            raise ValueError('Name must be between 1 and 50 characters')
        return v.strip() if v else v
    
    @validator('age')
    def validate_age(cls, v):
        if v is not None and (v < 13 or v > 120):
            raise ValueError('Age must be between 13 and 120')
        return v
    
    @validator('gender')
    def validate_gender(cls, v):
        if v is not None and v not in ['male', 'female', 'other', 'prefer_not_to_say']:
            raise ValueError('Invalid gender')
        return v

class UserResponse(UserBase):
    id: uuid.UUID
    firebase_uid: str
    auth_method: str
    phone_number: Optional[str] = None
    email: Optional[str] = None
    is_active: bool
    is_phone_verified: bool
    is_email_verified: bool
    profile_completed: bool
    privacy_policy_accepted: bool
    terms_accepted: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class UserProfile(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    age: Optional[int] = None
    gender: Optional[str] = None
    country: str
    phone_number: Optional[str] = None
    email: Optional[str] = None
    auth_method: str
    profile_completed: bool
    created_at: datetime
    
    class Config:
        from_attributes = True
