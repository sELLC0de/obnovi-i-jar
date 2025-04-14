from aiogram import Bot, Dispatcher
from aiogram.utils.executor import start_polling
from handlers import register_handlers
import os
from aiohttp import web
import threading

API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

async def on_startup(_):
    print("Бот запущен")

# 🌐 Запускаем фейковый веб-сервер в отдельном потоке
def run_web_server():
    async def handle(request):
        return web.Response(text="Bot is running!")

    app = web.Application()
    app.router.add_get("/", handle)

    runner = web.AppRunner(app)

    async def start():
        await runner.setup()
        site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 10000)))
        await site.start()

    import asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start())
    loop.run_forever()

# 🧵 Запускаем веб-сервер в отдельном потоке
threading.Thread(target=run_web_server).start()

# ▶️ Запуск aiogram бота
if __name__ == '__main__':
    start_polling(dp, on_startup=on_startup)
