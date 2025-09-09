# app/main.py

from fastapi import FastAPI

from .config import settings
from .db import init_db
from .routers import (
    auth,
    users,
    providers,
    items,
    user_orders,
    admin_orders,
)

app = FastAPI(
    title="Inventory Management API",
    description="An advanced inventory system with JWT auth, user & admin orders.",
    version="1.0.0",
)


@app.on_event("startup")
def on_startup():
    # ensure all tables are created
    init_db()


# Authentication routes (signup, login)
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"],
)

# User management (protected by JWT + role checks)
app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
)

# CRUD for providers
app.include_router(
    providers.router,
    prefix="/providers",
    tags=["Providers"],
)

# CRUD for items + inventory checks
app.include_router(
    items.router,
    prefix="/items",
    tags=["Items"],
)

# Endpoints for customer orders
app.include_router(
    user_orders.router,
    prefix="/user-orders",
    tags=["User Orders"],
)

# Endpoints for admin (purchase) orders
app.include_router(
    admin_orders.router,
    prefix="/admin-orders",
    tags=["Admin Orders"],
)
 