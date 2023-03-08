from loader import bot, dp
from aiogram.types import Message
from states.states import Download
from aiogram.dispatcher import FSMContext
import os
import uuid
from pytube import YouTube


def download_video(url: str):
    yt = YouTube(url)
    audio_id = uuid.uuid4().fields[-1]
    # for audio
    # yt.streams.filter(only_audio=True).first().download("audio", f"{audio_id}.mp3")
    # return f"{audio_id}.mp3"
    yt.streams.filter(file_extension="mp4")
    stream = yt.streams.get_by_itag(22)
    stream.download("audio", f"{audio_id}.mp3")
    return f"{audio_id}.mp4"


@dp.message_handler(commands='download_youtube')
async def download_youtube(message: Message):
    await bot.send_message(message.from_user.id, "скинь ссылку на видео и я отправлю ее тебе ввиде аудио.")
    await Download.download.set()


@dp.message_handler(state=Download.download)
async def download(message: Message, state: FSMContext):
    title = download_video(message.text)
    audio = open(f'audio/{title}', 'rb')
    await message.answer(text="Все скачалось держи аудио")
    try:
        await bot.send_audio(message.chat.id, audio)
        await bot.send_message(message.chat.id, "")
    except:
        await message.answer("Файл слишком большой")
    os.remove(f"audio/{title}")
    await state.finish()
