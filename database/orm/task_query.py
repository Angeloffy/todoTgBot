from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.models import Task, User


async def orm_create_task(session: AsyncSession, description: str, user_id: int):
    task = Task(description=description, user_id=user_id)
    session.add(task)
    await session.commit()


async def orm_get_task(session: AsyncSession, task_id: int):
    result = await session.execute(select(Task).filter(Task.id == task_id))
    return result.scalars().first()


async def orm_update_task(session: AsyncSession, task_id: int, new_description: str):
    task = await orm_get_task(session, task_id)
    if task:
        task.description = new_description
        await session.commit()


async def orm_delete_task(session: AsyncSession, task_id: int):
    task = await orm_get_task(session, task_id)
    if task:
        await session.delete(task)
        await session.commit()


async def orm_get_tasks_by_user_id(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()
    if not user:
        return None

    tasks_result = await session.execute(select(Task).filter(Task.user_id == user_id))
    tasks = tasks_result.scalars().all()
    if not tasks:
        return None

    return tasks
