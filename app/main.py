from fastapi import FastAPI

app = FastAPI(title='TODO App')


@app.get("/")
async def root():
    return {"message": "Hello World"}