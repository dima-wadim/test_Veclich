from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token="YOUR_TELEGRAM_BOT_TOKEN")
dp = Dispatcher(storage=MemoryStorage())

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Welcome to test_Veclich bot!")

@dp.message_handler(commands=["messages"])
async def get_messages(message: types.Message):
    # Логика получения сообщений из MongoDB
    messages = [...]  # Пример данных
    await message.answer(f"Messages: {messages}")

@dp.message_handler(commands=["add_message"])
async def add_message(message: types.Message):
    # Логика добавления сообщения
    await message.answer("Message added!")
