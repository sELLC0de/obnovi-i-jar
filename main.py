from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from handlers import register_handlers
import asyncio
import os

from aiohttp import web  # добавим веб-сервер

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

async def on_startup(_):
    print("Бот запущен")

async def start_web_app():
    async def handle(request):
        return web.Response(text="Bot is running!")

    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 10000)))  # Render использует переменную PORT
    await site.start()

async def main():
    await asyncio.gather(
        start_web_app(),
        executor.start_polling(dp, on_startup=on_startup)
    )

if __name__ == '__main__':
    asyncio.run(main())
