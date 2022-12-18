from config import TOKEN
from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

executor.start_polling(dp, skip_updates=True)