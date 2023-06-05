from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import UserProfile, get_user_profile, update_user_profile
from ..ui import get_check_kb

router = Router()


class Register(StatesGroup):
    name = State()
    last_name = State()
    age = State()
    check = State()


@router.message(Command(commands="reg"))
async def cmd_start(message: Message, state: FSMContext) -> None:
    await message.answer(text="OK. Input your name")
    await state.set_state(state=Register.name)


@router.message(Register.name, F.text.isalpha())
async def name_correct(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.answer(text="OK. Input your last name")
    await state.set_state(state=Register.last_name)


@router.message(Register.name)
async def name_correct(message: Message) -> None:
    await message.answer(text="Incorrect name")


@router.message(Register.last_name, F.text.isalpha())
async def name_correct(message: Message, state: FSMContext) -> None:
    await state.update_data(last_name=message.text)
    await message.answer(text="OK. Input your age")
    await state.set_state(state=Register.age)


@router.message(Register.last_name)
async def name_correct(message: Message) -> None:
    await message.answer(text="Incorrect last name")


@router.message(Register.age, F.text.isdigit())
async def name_correct(message: Message, state: FSMContext) -> None:
    await state.update_data(age=int(message.text))
    data = await state.get_data()
    await message.answer(text=f"OK. Check your input:\n"
                              f"Name: {data.get('name')}\n"
                              f"Last name: {data.get('last_name')}\n"
                              f"Age: {data.get('age')}", reply_markup=get_check_kb())
    await state.set_state(state=Register.check)


@router.message(Register.age)
async def name_correct(message: Message) -> None:
    await message.answer(text="Incorrect age")


@router.message(Register.check, F.text.lower().in_(("correct", "incorrect")))
async def name_correct(message: Message, state: FSMContext, session: AsyncSession) -> None:
    if message.text.lower() == "incorrect":
        await message.answer(text="OK. Input your name again", reply_markup=ReplyKeyboardRemove())
        await state.set_state(state=Register.name)
        return
    data = await state.get_data()
    user = await get_user_profile(session=session, user_id=message.from_user.id)
    if user is None:
        user = UserProfile(id=message.from_user.id, **data)
        session.add(user)
    else:
        await update_user_profile(session=session, user_id=message.from_user.id, data=data)
    await session.commit()
    await state.clear()
    await message.answer(text="OK.", reply_markup=ReplyKeyboardRemove())


@router.message(Command(commands="my_reg"))
async def my_reg_cmd(message: Message, session: AsyncSession) -> None:
    user = await get_user_profile(session=session, user_id=message.from_user.id)
    if user is None:
        await message.answer(text="You haven't reg")
        return
    await message.answer(text=f"Your reg:\n"
                              f"Name: {user.name}\n"
                              f"Last Name: {user.last_name}\n"
                              f"Age: {user.age}")
