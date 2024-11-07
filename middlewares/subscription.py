from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from keyboards.inline.mychannel import channels

from data.config import CHANNEL_ID
from utils.helpful_functions import check_subscription


class CheckSubscriptionMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        user_id = message.from_user.id
        
        for channel_id in CHANNEL_ID:
            if not await check_subscription(user_id, channel_id):
                try:
                    chat = await message.bot.get_chat(channel_id) 
                    
                    response_text = (
                        "<b>Botdan foydalanish uchun kanalga a'zo bo'ling 👇</b>\n\n"
                    )
                    
                    await message.answer(response_text, reply_markup=channels)
                except Exception as e:
                    print(f"Error fetching chat: {e}")

                raise CancelHandler()
