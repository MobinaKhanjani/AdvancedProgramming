from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..db import get_session
from ..schemas.provider import ProviderCreate, ProviderRead
from ..models.provider import Provider
from ..services.auth import get_current_user
from ..services.auth import get_current_user

router = APIRouter(
    prefix="/providers",
    tags=["Providers"]
)

# تعریف dependency برای ادمین
def get_admin_user(current_user = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin role required"
        )
    return current_user

@router.post(
    "/",
    response_model=ProviderRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(get_admin_user)]
)
def create_provider(
    provider_in: ProviderCreate,
    db: Session = Depends(get_session)
):
    # اینجا فقط ادمین اجازه‌ی اضافه کردن پروایدر دارد
    provider = Provider(**provider_in.dict())
    db.add(provider)
    db.commit()
    db.refresh(provider)
    return provider
