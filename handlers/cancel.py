from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext

from keyboards import reply

router = Router()


@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "отмена")
async def cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Отменено", reply_markup=reply.main_kb)
