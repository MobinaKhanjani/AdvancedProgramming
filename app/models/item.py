from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship

from ..db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    sku = Column(String, unique=True, nullable=False, index=True)
    price = Column(Float, nullable=False)
    min_threshold = Column(Integer, default=0, nullable=False)
    category = Column(String, nullable=False, index=True)
    image_url = Column(String, nullable=True)
    quantity = Column(Integer, default=0, nullable=False)
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # link to user order line items
    user_order_items = relationship(
        "UserOrderItem",
        back_populates="item",
        cascade="all, delete-orphan",
    )

    # link to admin (purchase) order line items
    admin_order_items = relationship(
        "AdminOrderItem",
        back_populates="item",
        cascade="all, delete-orphan",
    )
