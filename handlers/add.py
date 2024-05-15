from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from database.orm.task_query import orm_create_task
from keyboards import reply

router = Router()


class AddingTask(StatesGroup):
    adding_task = State()


@router.message(Command(commands=["add"]))
@router.message(F.text.lower() == "создать задачу")
async def add(message: Message, state: FSMContext):
    await state.set_state(AddingTask.adding_task)
    await message.answer("Введите описание задачи:", reply_markup=reply.cancel_kb)


@router.message(AddingTask.adding_task)
async def process_task_description(message: Message, state: FSMContext, session: AsyncSession):
    user_id = message.from_user.id
    task_description = message.text
    await state.clear()
    await orm_create_task(session, task_description, user_id)
    await message.answer(f"Задача '{task_description}' добавлена!", reply_markup=reply.main_kb)
