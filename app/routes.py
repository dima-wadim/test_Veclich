from fastapi import APIRouter
from .models import Message

router = APIRouter()

@router.get("/api/v1/messages/")
async def get_messages():
    return []

@router.post("/api/v1/message/")
async def create_message(message: Message):
    return {"status": "success"}
