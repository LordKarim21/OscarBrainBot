from aiogram.types import Message
from keyboards.reply.start_reply import client
from loader import bot, dp


@dp.message_handler(commands=['start'])
async def bot_start(message: Message):
    try:
        await bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!", reply_markup=client)
        await message.delete()
    except:
        await message.reply("Напишите боту в ЛС:\nhttps://t.me/OscarBrainBot")
