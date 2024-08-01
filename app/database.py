import motor.motor_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

mongo_client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://mongo:27017')
db = mongo_client.test_database

DATABASE_URL = 'postgresql+asyncpg://user:password@postgres/mydatabase'
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def init_db():
    # Инициализация базы данных
    pass
