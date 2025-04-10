# database.py
from typing import List, Type, TypeVar

from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import Session, sessionmaker

from .models.base import Base
from .models.user import User

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://user:password@db/todo_db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)

T = TypeVar('T')


async def create_tables():
    # This manually creates the tables in the asyncpg database
    async with engine.begin() as conn:
        # Create tables asynchronously
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Function to get an object by ID
async def get_by_id(db: AsyncSession, model: Type[T], object_id: int) -> T:
    result = await db.execute(select(model).filter(model.id == object_id))
    instance = result.scalar_one_or_none()
    if instance is None:
        raise NoResultFound(f"{model.__name__} not found with ID {object_id}")
    return instance

# Function to get all objects of a model
async def get_all(db: AsyncSession, model: Type[T]) -> List[T]:
    result = await db.execute(select(model))
    return result.scalars().all()

# Function to delete an object by ID
async def delete(db: AsyncSession, model: Type[T], object_id: int) -> None:
    instance = await get_by_id(db, model, object_id)
    await db.delete(instance)
    await db.commit()

# Function to create or save an object
async def save(db: AsyncSession, instance: T) -> T:
    db.add(instance)
    await db.commit()
    await db.refresh(instance)
    return instance


