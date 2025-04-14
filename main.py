from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from handlers import register_handlers

API_TOKEN = 'YOUR_BOT_TOKEN'  # <-- вставь сюда токен от BotFather

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
