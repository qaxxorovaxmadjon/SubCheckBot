from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

channels = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Channel name", url="https://t.me/Your channel username"),
        ],
        [
            InlineKeyboardButton(text="Channel name", url="https://t.me/Your channel username"),
        ],

    ]
)
