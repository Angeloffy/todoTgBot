from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from database.orm.task_query import orm_get_task, orm_delete_task

router = Router()


@router.message(F.text.startswith('/del_'))
async def del_task(message: Message, session: AsyncSession):
    task_id = message.text.split("/del_")[1]
    if task_id == '':
        await message.answer("Вы не указали ID задачи.")
    elif not task_id.isdigit():
        await message.answer("ID не число.")
    else:
        task_id = int(task_id)
        task = await orm_get_task(session, task_id)
        if task is None:
            await message.answer(text='Задачи не существует')
        else:
            if int(task.user_id) != int(message.from_user.id):
                await message.answer(text='Вы не можете удалить эту задачу.')
            else:
                await orm_delete_task(session, task_id)
                await message.answer(text='Задача удалена успешно')
