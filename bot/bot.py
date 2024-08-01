from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_command(message: Message):
    await message.answer("Привет! Я ваш бот.")

@dp.message(commands=["messages"])
async def list_messages(message: Message):
    await message.answer("Здесь будут ваши сообщения.")

async def on_startup(dispatcher):
    # Логика инициализации бота
    pass

if __name__ == "__main__":
    dp.start_polling(bot, on_startup=on_startup)
