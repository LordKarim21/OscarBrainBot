from aiogram.types import BotCommand
from aiogram import Dispatcher
from config_data.config import DEFAULT_COMMANDS


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [BotCommand(i[0], i[1]) for i in DEFAULT_COMMANDS]
    )
