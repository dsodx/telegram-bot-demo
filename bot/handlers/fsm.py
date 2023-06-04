from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

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
async def name_correct(message: Message, state: FSMContext) -> None:
    if message.text.lower() == "incorrect":
        await message.answer(text="OK. Input your name again", reply_markup=ReplyKeyboardRemove())
        await state.set_state(state=Register.name)
        return
    await message.answer(text="OK.", reply_markup=ReplyKeyboardRemove())
    await state.clear()
