from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config_data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
