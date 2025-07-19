from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserProfile, UserUpdate, UserResponse
from app.services.user_service import user_service
from app.dependencies import get_current_user, require_completed_profile
from app.models.user import User

router = APIRouter()

@router.get("/profile", response_model=UserProfile)
async def get_user_profile(
    current_user: User = Depends(get_current_user)
):
    """
    Get user profile
    
    Returns the current user's profile information.
    """
    return current_user

@router.put("/profile", response_model=UserResponse)
async def update_user_profile(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Update user profile
    
    Updates the current user's profile information.
    Only provided fields will be updated.
    """
    try:
        updated_user = user_service.update_user(db, current_user.id, user_update)
        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return updated_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update profile: {str(e)}"
        )

@router.delete("/account")
async def delete_user_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Delete user account
    
    Permanently deletes the current user's account and all associated data.
    This action cannot be undone.
    """
    try:
        success = user_service.delete_user(db, current_user.id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return {"message": "Account successfully deleted"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete account: {str(e)}"
        )

@router.post("/deactivate")
async def deactivate_user_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Deactivate user account
    
    Deactivates the current user's account. The account can be reactivated later.
    """
    try:
        deactivated_user = user_service.deactivate_user(db, current_user.id)
        if not deactivated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return {"message": "Account successfully deactivated"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to deactivate account: {str(e)}"
        )
