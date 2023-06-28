from fastapi import FastAPI
from app.routes.user_routes import userRouter

app = FastAPI()

app.include_router(userRouter)

@app.get("/")
async def home():
    return {"message": "Hello World"}