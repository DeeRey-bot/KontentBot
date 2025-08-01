import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS", "").split(",")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: Message):
    await message.answer("Привет! Это Контент‑бот. Готов к работе 💼")

@dp.message_handler(commands=["help"])
async def help_cmd(message: Message):
    await message.answer("Здесь ты сможешь зарабатывать на файлах. Загрузи PDF — и получи ссылку для скачивания 💸")

if __name__ == "__main__":
    executor.start_polling(dp)