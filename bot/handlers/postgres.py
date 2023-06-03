from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import User, get_user

router = Router()


@router.message(Command(commands="add_me"))
async def cmd_start(message: Message, session: AsyncSession) -> None:
    user = await get_user(session=session, user_id=message.from_user.id)
    if user is None:
        user = User(id=message.from_user.id, name=message.from_user.full_name)
    else:
        await message.answer(text="You are already added")
        return
    session.add(user)
    await session.commit()
    await message.answer(text="Success!")


@router.message(Command(commands="del_me"))
async def cmd_start(message: Message, session: AsyncSession) -> None:
    user = await get_user(session=session, user_id=message.from_user.id)
    if user is None:
        await message.answer(text="You are already deleted")
        return
    await session.delete(user)
    await session.commit()
    await message.answer(text="Success!")
