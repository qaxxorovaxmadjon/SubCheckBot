from .subscription import CheckSubscriptionMiddleware
from keyboards.inline.mychannel import channels
from loader import dp


if __name__ == 'middlewares':
    dp.middleware.setup(CheckSubscriptionMiddleware())