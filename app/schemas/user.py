from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True