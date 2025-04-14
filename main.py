from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from handlers import register_handlers

API_TOKEN = '7807585583:AAHn3iMpPTjggU0A9OJF0lAEpXeGbwnPQek' 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
