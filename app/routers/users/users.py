from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_session
from ..schemas.user import UserRead
from ..services.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me", response_model=UserRead)
def read_current_user(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    # می‌توانید اینجا داده‌های بیشتری از کاربر واکشی کنید
    return current_user
