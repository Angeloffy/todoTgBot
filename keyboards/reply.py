from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton, ReplyKeyboardRemove,
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Создать задачу"),
            KeyboardButton(text="Все задачи")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Input me",
    selective=True
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отмена", callback_data="cancel")
        ]
    ],
    resize_keyboard=True
)

rmk = ReplyKeyboardRemove()