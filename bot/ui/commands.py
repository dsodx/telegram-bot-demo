from typing import List

from aiogram import Bot
from aiogram.types import BotCommand


def get_default_commands() -> List[BotCommand]:
    return [
        BotCommand(command="start", description="Restart the bot"),
        BotCommand(command="help", description="Show help")
    ]


async def setup_default_commands(bot: Bot) -> None:
    await bot.set_my_commands(commands=get_default_commands())
