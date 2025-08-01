import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

# Устанавливаем логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    await message.answer("Привет! Это Контент-бот. Зарабатывай на файлах 📁")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
