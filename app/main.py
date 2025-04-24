from fastapi import FastAPI

from app.database import create_tables
from app.routes import user

app = FastAPI(title="TODO App")

app.include_router(user.router)

@app.on_event("startup")
async def on_startup():
    await create_tables()