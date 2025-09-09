# app/db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

# SQLite needs check_same_thread=False for multiple threads
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def init_db():
    """
    Import all models here so that their 
    metadata gets registered on Base before table creation.
    """
    from .models import user, provider, item, user_order, admin_order  # noqa
    Base.metadata.create_all(bind=engine)


def get_session():
    """
    FastAPI dependency to get a database session.
    Remember to close it after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
