from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship

from ..db import Base


class UserOrder(Base):
    __tablename__ = "user_orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    user = relationship("User", back_populates="user_orders")
    items = relationship(
        "UserOrderItem",
        back_populates="user_order",
        cascade="all, delete-orphan",
    )


class UserOrderItem(Base):
    __tablename__ = "user_order_items"

    id = Column(Integer, primary_key=True, index=True)
    user_order_id = Column(
        Integer,
        ForeignKey("user_orders.id"),
        nullable=False,
        index=True,
    )
    item_id = Column(
        Integer,
        ForeignKey("items.id"),
        nullable=False,
        index=True,
    )
    quantity = Column(Integer, nullable=False)

    user_order = relationship("UserOrder", back_populates="items")
    item = relationship("Item", back_populates="user_order_items")
