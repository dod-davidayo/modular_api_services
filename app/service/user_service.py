# app/services/user_service.py

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate


def create_user(db: Session, user: UserCreate):
    """
    Business logic for creating a user.
    """

    db_user = User(
        name=user.name,
        email=user.email
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def get_users(db: Session):
    """
    Return all users.
    """

    return db.query(User).all()