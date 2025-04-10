from databases import Database
from fastapi import FastAPI
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI(title='TODO App')

DATABASE_URL = "postgresql+asyncpg://user:password@db/todo_db"

db = Database(DATABASE_URL)

#SQLAlchemy Setup
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# Create a sessionmaker for SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}