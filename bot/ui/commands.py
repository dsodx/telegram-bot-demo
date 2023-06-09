from typing import List

from aiogram import Bot
from aiogram.types import BotCommand


def get_default_commands() -> List[BotCommand]:
    return [
        BotCommand(command="start", description="Restart the bot"),
        BotCommand(command="help", description="Show help"),
        BotCommand(command="is_owner", description="Check: is you owner"),
        BotCommand(command="add_me", description="Add me in db"),
        BotCommand(command="del_me", description="Delete me from db"),
        BotCommand(command="reg", description="Run register process"),
        BotCommand(command="my_reg", description="View your reg")
    ]


async def setup_default_commands(bot: Bot) -> None:
    await bot.set_my_commands(commands=get_default_commands())
