from aiogram import Router, F
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.types import Message

from ..filters import IsOwnerFilter

router = Router()
router.message.filter(F.chat.type == ChatType.PRIVATE)


@router.message(Command(commands="is_owner"), IsOwnerFilter(is_owner=True))
async def cmd_start(message: Message) -> None:
    await message.answer(text="You <b>is</b> owner!")


@router.message(Command(commands="is_owner"), IsOwnerFilter(is_owner=False))
async def cmd_help(message: Message) -> None:
    await message.answer(text="You <b>is not</b> owner!")
