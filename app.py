import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from Config.config_bot import Bot_cfg as cfg
from database.engine import create_tables, session_maker

from handlers import start, add, cancel, tsk, del_task
from middlewares.db import DbSessionMiddleware

bot = Bot(cfg['token'], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp.include_router(cancel.router)
dp.include_router(start.router)
dp.include_router(add.router)
dp.include_router(tsk.router)
dp.include_router(del_task.router)

async def on_startup(bot):
    await create_tables()
    print('BOT STARTED')


async def on_shutdown(bot):
    await bot.session.close()
    print('BOT SHUTDOWN')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DbSessionMiddleware(session_pool=session_maker))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    return bot


if __name__ == "__main__":
    asyncio.run(main())
