from aiogram.types import Message
from aiogram import Dispatcher

async def handle_message(message: Message):
    await message.answer("Сообщение получено!")

def register_handlers(dp: Dispatcher):
    dp.message.register(handle_message)
