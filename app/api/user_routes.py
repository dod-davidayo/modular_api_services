# app/api/user_routes.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.service.user_service import create_user, get_users
from app.schemas.user_schema import UserCreate, UserResponse


router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user_route(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    API endpoint to create user.
    """

    return create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def list_users(
    db: Session = Depends(get_db)
):
    """
    API endpoint to list users.
    """

    return get_users(db)