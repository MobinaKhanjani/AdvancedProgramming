from enum import Enum

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime,
    func,
    Enum as SqlEnum,
)
from sqlalchemy.orm import relationship

from ..db import Base


class AdminOrderStatus(Enum):
    DRAFT = "Draft"
    SENT = "Sent"
    RECEIVED = "Received"
    CLOSED = "Closed"


class AdminOrder(Base):
    __tablename__ = "admin_orders"

    id = Column(Integer, primary_key=True, index=True)
    provider_id = Column(Integer, ForeignKey("providers.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(
        SqlEnum(AdminOrderStatus),
        default=AdminOrderStatus.DRAFT,
        nullable=False,
    )
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

    provider = relationship("Provider", back_populates="admin_orders")
    user = relationship("User", back_populates="admin_orders")
    items = relationship(
        "AdminOrderItem",
        back_populates="admin_order",
        cascade="all, delete-orphan",
    )


class AdminOrderItem(Base):
    __tablename__ = "admin_order_items"

    id = Column(Integer, primary_key=True, index=True)
    admin_order_id = Column(
        Integer,
        ForeignKey("admin_orders.id"),
        nullable=False,
    )
    item_id = Column(
        Integer,
        ForeignKey("items.id"),
        nullable=False,
    )
    quantity = Column(Integer, nullable=False)

    admin_order = relationship("AdminOrder", back_populates="items")
    item = relationship("Item", back_populates="admin_order_items")
