from sqlalchemy import Column, String, Integer, Boolean, DateTime, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from app.models.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    firebase_uid = Column(String(128), unique=True, nullable=False, index=True)
    auth_method = Column(String(20), nullable=False)
    
    # Profile data
    phone_number = Column(String(20), unique=True, nullable=True)
    email = Column(String(255), nullable=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(20), nullable=True)
    country = Column(String(3), nullable=False)
    
    # Status
    is_active = Column(Boolean, default=True)
    is_phone_verified = Column(Boolean, default=False)
    is_email_verified = Column(Boolean, default=False)
    profile_completed = Column(Boolean, default=False)
    
    # Privacy
    privacy_policy_accepted = Column(Boolean, default=False)
    terms_accepted = Column(Boolean, default=False)
    privacy_policy_version = Column(String(10))
    terms_version = Column(String(10))
    
    # Security
    last_login_at = Column(DateTime(timezone=True))
    failed_login_attempts = Column(Integer, default=0)
    account_locked_until = Column(DateTime(timezone=True))
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Constraints
    __table_args__ = (
        CheckConstraint("auth_method IN ('phone', 'google')", name="valid_auth_method"),
        CheckConstraint("age >= 13 AND age <= 120", name="valid_age"),
        CheckConstraint("gender IN ('male', 'female', 'other', 'prefer_not_to_say')", name="valid_gender"),
        CheckConstraint(
            "(auth_method = 'phone' AND phone_number IS NOT NULL) OR (auth_method = 'google')",
            name="phone_required_for_phone_auth"
        ),
        CheckConstraint(
            "(auth_method = 'google' AND email IS NOT NULL) OR (auth_method = 'phone')",
            name="email_required_for_google_auth"
        ),
    )
