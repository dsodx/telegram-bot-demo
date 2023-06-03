import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from .config import config
from .handlers import setup_routers
from .ui import setup_default_commands

logger = logging.getLogger(name=__name__)


async def on_startup(bot: Bot, dp: Dispatcher, session_pool: async_sessionmaker) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_default_commands(bot=bot)
    setup_routers(dp=dp, session_pool=session_pool)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    engine = create_async_engine(url=config.postgres.dsn)
    session_pool = async_sessionmaker(bind=engine, expire_on_commit=False)

    bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp["config"] = config

    await on_startup(bot=bot, dp=dp, session_pool=session_pool)

    logger.warning(msg="Starting bot...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning(msg="Bot stopped")
