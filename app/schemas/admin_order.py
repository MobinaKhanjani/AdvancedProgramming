from enum import Enum
from pydantic import BaseModel, conint, root_validator
from datetime import datetime
from typing import List, Optional


class AdminOrderStatus(str, Enum):
    DRAFT = "Draft"
    SENT = "Sent"
    RECEIVED = "Received"
    CLOSED = "Closed"


class AdminOrderItemBase(BaseModel):
    item_id: int
    quantity: conint(gt=0)

    @root_validator
    def check_quantity_positive(cls, values):
        qty = values.get("quantity")
        if qty is None or qty <= 0:
            raise ValueError("quantity must be greater than zero")
        return values


class AdminOrderItemCreate(AdminOrderItemBase):
    pass


class AdminOrderItemRead(AdminOrderItemBase):
    id: int

    class Config:
        orm_mode = True


class AdminOrderBase(BaseModel):
    provider_id: int
    status: Optional[AdminOrderStatus] = AdminOrderStatus.DRAFT


class AdminOrderCreate(AdminOrderBase):
    items: List[AdminOrderItemCreate]

    @root_validator
    def ensure_items_not_empty(cls, values):
        items = values.get("items") or []
        if not items:
            raise ValueError("An order must contain at least one item")
        return values


class AdminOrderUpdate(BaseModel):
    status: Optional[AdminOrderStatus]


class AdminOrderRead(AdminOrderBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    items: List[AdminOrderItemRead]

    class Config:
        orm_mode = True
