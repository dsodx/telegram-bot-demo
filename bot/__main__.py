import logging
import asyncio

from aiogram import Bot, Dispatcher

from .config import config

logger = logging.getLogger(name=__name__)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=config.bot_token.get_secret_value())
    dp = Dispatcher()

    logger.warning(msg="Starting bot...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.warning(msg="Bot stopped")
