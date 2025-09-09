from pydantic import BaseModel, EmailStr, Field, constr, root_validator
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: constr(min_length=8) = Field(
        ...,
        description="Password must be at least 8 characters long and include letters and numbers"
    )


class UserRead(UserBase):
    id: int
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: str

    @root_validator
    def require_username_or_email(cls, values):
        if not (values.get("username") or values.get("email")):
            raise ValueError("Either username or email must be provided")
        return values
