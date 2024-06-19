import reply
import asyncio
from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from AntiFlood import AntiFloodMiddleware
from handlers import form, help, start, about
from config_reader import config


from database import start_db


bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher()


async def main():
    await start_db()
    dp.message.middleware(AntiFloodMiddleware())
    dp.include_routers(
        start.router,
        help.router,
        about.router,
        form.router,
        reply.router,
        )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


