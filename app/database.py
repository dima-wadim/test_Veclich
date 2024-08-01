from motor.motor_asyncio import AsyncIOMotorClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from redis.asyncio import Redis

DATABASE_URL = "postgresql+asyncpg://user:password@postgres/testdb"
MONGO_URL = "mongodb://mongo:27017"
REDIS_URL = "redis://redis:6379"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongo_db = mongo_client.testdb

redis = Redis.from_url(REDIS_URL, decode_responses=True)
