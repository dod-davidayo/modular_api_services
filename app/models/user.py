from sqlalchemy import  Column, String,  Integer
from app.db.base import Base


class User(Base):
    """
    Sqlalchemy database model.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index = True)
