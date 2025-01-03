from aiogram import Bot, Dispatcher
import asyncio
import logging
from aiogram.enums import ParseMode
from data.config import BOT_TOKEN
from handler import setup_message_routers
from data.config import ADMINS


async def on_startup(bot: Bot):
    for admin in ADMINS:
        await bot.send_message(admin, "Bot ishga tushdi!")
    logging.info("Bot ishga tushganligi haqida xabar yuborildi.")


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.startup.register(on_startup)

    handler_routers = setup_message_routers()
    dp.include_router(handler_routers)

    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
