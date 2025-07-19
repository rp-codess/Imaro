from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from typing import Optional
import uuid

class UserService:
    
    def get_user_by_id(self, db: Session, user_id: uuid.UUID) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_firebase_uid(self, db: Session, firebase_uid: str) -> Optional[User]:
        return db.query(User).filter(User.firebase_uid == firebase_uid).first()
    
    def get_user_by_phone(self, db: Session, phone_number: str) -> Optional[User]:
        return db.query(User).filter(User.phone_number == phone_number).first()
    
    def get_user_by_email(self, db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()
    
    def create_user(self, db: Session, user: UserCreate) -> User:
        db_user = User(
            firebase_uid=user.firebase_uid,
            auth_method=user.auth_method,
            phone_number=user.phone_number,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            age=user.age,
            gender=user.gender,
            country=user.country,
            is_phone_verified=user.auth_method == "phone",
            is_email_verified=user.auth_method == "google"
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def update_user(self, db: Session, user_id: uuid.UUID, user_update: UserUpdate) -> Optional[User]:
        db_user = self.get_user_by_id(db, user_id)
        if not db_user:
            return None
        
        update_data = user_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)
        
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def complete_profile(self, db: Session, user_id: uuid.UUID, profile_data: dict) -> Optional[User]:
        db_user = self.get_user_by_id(db, user_id)
        if not db_user:
            return None
        
        # Update profile fields
        for field, value in profile_data.items():
            if hasattr(db_user, field):
                setattr(db_user, field, value)
        
        # Mark profile as completed
        db_user.profile_completed = True
        
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def delete_user(self, db: Session, user_id: uuid.UUID) -> bool:
        db_user = self.get_user_by_id(db, user_id)
        if not db_user:
            return False
        
        db.delete(db_user)
        db.commit()
        return True
    
    def deactivate_user(self, db: Session, user_id: uuid.UUID) -> Optional[User]:
        db_user = self.get_user_by_id(db, user_id)
        if not db_user:
            return None
        
        db_user.is_active = False
        db.commit()
        db.refresh(db_user)
        return db_user

user_service = UserService()
