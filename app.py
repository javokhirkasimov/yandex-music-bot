import os
from asyncio import sleep
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from download_music import download_world_tracks, download_russia_tracks, download_uzbek_tracks

TOKEN = '2030399731:AAH5kr6GtOPPd12IFematnEl2Xep6hrtpXA'
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmdstart(message:types.Message):
    await message.answer(f'Hi, {message.from_user.first_name},\n /world\n/russia\n/uzbek ')

@dp.message_handler(commands='world')
async def send_musics(message:types.Message):
    await message.answer('Please wait a minute!')
    download_world_tracks()
    for m in os.listdir('./musics/world'):
        if m.endswith('.mp3'):
            music = types.InputFile(path_or_bytesio=f'musics/world/{m}')
            await message.answer_audio(music)
            sleep(1)
            os.remove(f'musics/world/{m}')


@dp.message_handler(commands='russia')
async def send_musics(message:types.Message):
    await message.answer('Please wait a minute!')
    download_russia_tracks()
    for m in os.listdir('./musics/russia'):
        if m.endswith('.mp3'):
            music = types.InputFile(path_or_bytesio=f'musics/russia/{m}')
            await message.answer_audio(music)
            sleep(1)
            os.remove(f'musics/russia/{m}')

@dp.message_handler(commands='uzbek')
async def send_musics(message:types.Message):
    await message.answer('Please wait a minute!')
    download_uzbek_tracks()
    for m in os.listdir('./musics/uzbek'):
        if m.endswith('.mp3'):
            music = types.InputFile(path_or_bytesio=f'musics/uzbek/{m}')
            await message.answer_audio(music)
            sleep(1)
            os.remove(f'musics/uzbek/{m}')


if  __name__ == '__main__':
    executor.start_polling(dp)