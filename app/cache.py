from app.database import redis

async def cache_get(key):
    return await redis.get(key)

async def cache_set(key, value):
    await redis.set(key, value)

async def cache_delete(key):
    await redis.delete(key)
