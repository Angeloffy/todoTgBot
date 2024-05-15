from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession
from keyboards import reply

from database.orm.task_query import orm_get_tasks_by_user_id
from src.parse_tasks import format_tasks

router = Router()

@router.message(Command(commands=["tsk"]))
@router.message(F.text.lower() == "все задачи")
async def tsk(message: Message, session: AsyncSession):
    user_id = message.from_user.id
    tasks = await orm_get_tasks_by_user_id(session, user_id)
    formated_tasks = await format_tasks(tasks)
    await message.answer(text=formated_tasks, reply_markup=reply.main_kb)
