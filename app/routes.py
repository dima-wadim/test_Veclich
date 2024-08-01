from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import mongo_db, redis, SessionLocal
from app.models import Message

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/api/v1/messages/")
async def get_messages():
    cached_messages = await redis.get("messages")
    if cached_messages:
        return cached_messages

    messages = await mongo_db.messages.find().to_list(None)
    await redis.set("messages", messages)
    return messages

@router.post("/api/v1/message/")
async def create_message(message: Message, db: AsyncSession = Depends(get_db)):
    await mongo_db.messages.insert_one(message.dict())
    await redis.delete("messages")
    return {"status": "Message created"}
