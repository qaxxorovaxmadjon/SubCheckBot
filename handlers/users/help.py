from aiogram import types
from loader import dp

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(f"Qanday yordam kerak?")