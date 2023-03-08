from loader import bot, dp
import handlers
from aiogram.utils import executor
from utils.set_bot_commands import set_default_commands


async def on_start(_):
    await set_default_commands(dp)
    print("Bot start")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_start)
