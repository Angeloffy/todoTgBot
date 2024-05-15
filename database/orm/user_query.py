from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User


async def orm_create_user(session: AsyncSession, user_id: int, username: str = None):
    user = User(id=user_id, username=username)
    session.add(user)
    await session.commit()


async def orm_get_user(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()


async def orm_update_user(session: AsyncSession, user_id: int, new_username: str):
    user = await orm_get_user(session, user_id)
    if user:
        user.username = new_username
        await session.commit()
        return user
    return None


async def orm_delete_user(session: AsyncSession, user_id: int):
    user = await orm_get_user(session, user_id)
    if user:
        session.delete(user)
        await session.commit()
        return True
    return False


async def orm_exist_user(session: AsyncSession, user_id: int):
    result = await session.execute(select(User).filter(User.id == user_id))
    return bool(result.scalars().first())
