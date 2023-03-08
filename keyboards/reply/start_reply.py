from aiogram import types


client = types.ReplyKeyboardMarkup()
for i in ["/start", "/help", "/download_youtube"]:
    b = types.KeyboardButton(i)
    client.add(b)
