from fastapi import FastAPI

from app.routes import user

app = FastAPI(title="TODO App")

app.include_router(user.router)