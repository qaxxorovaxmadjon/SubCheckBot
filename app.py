from aiogram import executor
from utils import logging
from loader import dp

import middlewares, filters, handlers


if __name__ == '__main__':
    executor.start_polling(
        dp, skip_updates = True
    )