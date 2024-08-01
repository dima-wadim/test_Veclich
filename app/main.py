from fastapi import FastAPI
from .database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/api/v1/messages/")
async def get_messages():
    # Код для получения списка сообщений
    return []

@app.post("/api/v1/message/")
async def create_message(username: str, content: str):
    # Код для создания нового сообщения
    return {"status": "success"}
