# schemas user helps to validate API Data

from pydantic import BaseModel

class UserCreate(BaseModel):
    """
    Data required to create a user.
    """

    name: str
    email: str

class UserResponse(BaseModel):
    """
    Data returned from the API
    """
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
        