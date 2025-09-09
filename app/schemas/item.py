from pydantic import BaseModel, Field, HttpUrl, PositiveFloat, conint
from datetime import datetime
from typing import Optional


class ItemBase(BaseModel):
    name: str = Field(..., example="Wireless Mouse")
    sku: str = Field(..., example="WM-12345")
    price: PositiveFloat = Field(..., description="Unit price of the item")
    min_threshold: conint(ge=0) = Field(
        0,
        description="Reorder point at which low-stock alerts are triggered"
    )
    category: str = Field(..., example="Electronics")
    image_url: Optional[HttpUrl] = Field(
        None,
        description="Optional URL to an image of the product"
    )


class ItemCreate(ItemBase):
    quantity: conint(ge=0) = Field(
        0,
        description="Initial stock quantity for the new item"
    )


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, example="Gaming Keyboard")
    sku: Optional[str] = Field(None, example="GK-67890")
    price: Optional[PositiveFloat] = Field(None)
    min_threshold: Optional[conint(ge=0)] = Field(None)
    category: Optional[str] = Field(None, example="Peripherals")
    image_url: Optional[HttpUrl] = Field(None)
    quantity: Optional[conint(ge=0)] = Field(None)


class ItemRead(ItemBase):
    id: int
    quantity: int
    created_at: datetime
    is_below_threshold: bool = Field(
        False,
        description="Computed: True if quantity <= min_threshold"
    )

    class Config:
        orm_mode = True
