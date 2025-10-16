import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from tortoise import Tortoise
from config import TORTOISE_ORM, TOEKN
from handlers import router


async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    logging.info("Ma'lumotlar bazasi ulangan va sxemalar yaratilgan.")


async def close_db():
    await Tortoise.close_connections()
    logging.info("Ma'lumotlar bazasi ulanishlari yopildi.")


async def startup(bot: Bot):
    await bot.send_message(chat_id=6357730441, text="<b>Bot ishga tushdi✅</b>")


async def shutdown(bot: Bot):
    await bot.send_message(chat_id=6357730441, text="<b>Bot ishdan toxtadi🛑</b>")


async def main():
    await init_db()
    bot = Bot(token=TOEKN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    finally:
        await close_db()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
