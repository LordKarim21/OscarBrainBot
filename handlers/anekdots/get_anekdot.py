from loader import bot, dp
from aiogram.types import Message
from utils.parser.parser import parser
from random import shuffle


@dp.message_handler(commands=['anekdot'])
async def get_anekdot(message: Message):
    list_jokes = parser()
    shuffle(list_jokes)
    joke = list_jokes[0]
    await bot.send_message(message.chat.id, joke)
    list_jokes.remove(joke)
