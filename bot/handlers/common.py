from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(text="Hello!")


@router.message(Command(commands="help"))
async def cmd_help(message: Message) -> None:
    await message.answer(text="*Help*")
