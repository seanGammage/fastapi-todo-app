# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from .models.base import Base
from .models.user import User

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://user:password@db/todo_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save(db: Session, instance):
    """
    Generic save method to add an instance to the DB and commit.
    Args:
    - db (Session): The SQLAlchemy session
    - instance (SQLAlchemy model instance): The model instance to save
    """
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance

