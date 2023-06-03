import asyncio
import logging

from aiogram import Bot, Dispatcher

from .config import config
from .handlers import setup_routers
from .ui import setup_default_commands

logger = logging.getLogger(name=__name__)


async def on_startup(bot: Bot, dp: Dispatcher) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_default_commands(bot=bot)
    setup_routers(dp=dp)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    await on_startup(bot=bot, dp=dp)

    logger.warning(msg="Starting bot...")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning(msg="Bot stopped")
