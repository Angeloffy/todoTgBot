from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from database.orm.user_query import orm_get_user, orm_create_user
from keyboards import reply

router = Router()


@router.message(CommandStart())
async def start(message: Message, session: AsyncSession):
    user_id = message.from_user.id
    username = message.from_user.username
    if username is None:
        first_name = message.from_user.first_name
        username = first_name
        if first_name is None:
            username = None

    exist_user = await orm_get_user(session, user_id)
    if exist_user is None:
        await orm_create_user(session, user_id, username)
        welcome_text = "Добро пожаловать!"
    else:
        welcome_text = "Вы вернулись!"

    welcome_text += '\n'
    welcome_text += f"\nДля добавления задачи используйте: /add"
    welcome_text += f"\nПросмотр задач: /tsk"

    await message.answer(text=welcome_text, reply_markup=reply.main_kb)
