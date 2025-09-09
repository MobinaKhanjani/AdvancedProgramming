from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional


class ProviderBase(BaseModel):
    name: str = Field(..., example="ACME Supplies")
    email: EmailStr = Field(..., example="supplier@example.com")
    contact_name: Optional[str] = Field(None, example="John Doe")
    phone: Optional[str] = Field(None, example="+1234567890")
    lead_time_days: int = Field(
        ..., ge=0, description="Expected delivery lead time in days"
    )


class ProviderCreate(ProviderBase):
    pass


class ProviderUpdate(BaseModel):
    name: Optional[str] = Field(None, example="ACME Supplies")
    email: Optional[EmailStr] = Field(None, example="supplier@example.com")
    contact_name: Optional[str] = Field(None, example="Jane Smith")
    phone: Optional[str] = Field(None, example="+0987654321")
    lead_time_days: Optional[int] = Field(
        None, ge=0, description="Expected delivery lead time in days"
    )
    is_active: Optional[bool] = Field(
        None, description="Toggle provider active status"
    )


class ProviderRead(ProviderBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
