import os
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from download_music import download_world_tracks, search_music
import asyncio
import concurrent.futures


TOKEN = '2030399731:AAH5kr6GtOPPd12IFematnEl2Xep6hrtpXA'
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def cmdstart(message:types.Message):
    await message.answer(f'Hi, {message.from_user.first_name},\nSend me the name of a music I\'ll try to find it (<b>Not Artist Name or Album Name</b>)\n\n<i>To get Top10 musics from Yandex Music chart:</i> /top',parse_mode="HTML")



async def top_musics(CHART_ID,user_id):
    response = await run_blocking_io(download_world_tracks,CHART_ID,user_id)
    return response

async def download_music(music_name):
    response = await run_blocking_io(search_music,music_name)
    return response

async def run_blocking_io(func, *args):
    loop = asyncio.get_running_loop()
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,func,*args
        )
    return result



@dp.message_handler(commands='top')
async def send_top(message:types.Message):
    await message.answer('Please wait a minute!')
    media = types.MediaGroup()
    user_id = message.from_user.id
    await top_musics('world',user_id=user_id)
    for m in os.listdir(f'./musics/world/{user_id}'):
        if m.endswith('.mp3'):
            media.attach_audio(types.InputFile(path_or_bytesio=f'musics/world/{user_id}/{m}', filename=m[:-4]))
            os.remove(f'musics/world/{user_id}/{m}')
    os.rmdir(f'musics/world/{user_id}/')
    await message.answer_media_group(media)

    

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def send_music(message:types.Message):
    await message.answer('Please wait a minute!')
    result = await download_music(message.text)
    if result is None:
        for m in os.listdir('./musics'):
            if m.endswith('.mp3'):
                music = types.InputFile(path_or_bytesio=f'musics/{m}', filename=m[:-4])
                await message.answer_audio(music)
                os.remove(f'musics/{m}')
    elif result == 'Non':
        await message.answer('Couldn\'t find any music' )
    else:
        await message.answer(f"Please send me the name of the music not {list(result)[0]}")
    


    

if  __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)