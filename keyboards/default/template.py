from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

template = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Test"),
            KeyboardButton(text="Test"),
        ],
    ],
    resize_keyboard=True 
)
