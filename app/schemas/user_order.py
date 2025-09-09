from pydantic import BaseModel, conint, root_validator
from datetime import datetime
from typing import List, Optional


class UserOrderItemBase(BaseModel):
    item_id: int
    quantity: conint(gt=0)


class UserOrderItemCreate(UserOrderItemBase):
    pass


class UserOrderItemRead(UserOrderItemBase):
    id: int

    class Config:
        orm_mode = True


class UserOrderBase(BaseModel):
    # you could add common fields here later (e.g. notes, shipping_address)
    pass


class UserOrderCreate(UserOrderBase):
    items: List[UserOrderItemCreate]

    @root_validator
    def ensure_items_not_empty(cls, values):
        items = values.get("items") or []
        if not items:
            raise ValueError("An order must contain at least one item")
        return values


class UserOrderRead(UserOrderBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    items: List[UserOrderItemRead]

    class Config:
        orm_mode = True
