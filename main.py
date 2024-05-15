from os import environ
import os
import subprocess
import sys
import asyncio
from tempfile import NamedTemporaryFile
from subprocess import Popen
from pathlib import Path

from telebot.async_telebot import AsyncTeleBot, types as T

from transformers import pipeline

TOKEN = environ["KEY"]

bot = AsyncTeleBot(TOKEN)



pipe = pipeline(model="Yehoward/whisper-small-ro")

def transcribe(audio: bytes | str) -> str:
    return pipe(audio)["text"]

def is_voice(msg: T.Message) -> bool:
    return msg.voice is not None 

    

@bot.message_handler( content_types=["voice", "audio"])
async def transcribe_voice(msg: T.Message):

    print("am primit mesaj vocal")

    match msg.content_type:
        case "voice":
            msg_content = msg.voice
        case "audio":
            msg_content = msg.audio
        case _:
            print("transcribe_voice: wrogn content type", file=sys.stderr)
            return

    if msg_content is None:
        print("transcribe_voice: Telebot bug", file=sys.stderr)
        return 

    raspuns = await bot.reply_to(msg, "descarcăm audioul")
    try:
        file: T.File = await bot.get_file(msg_content.file_id)
        data = await bot.download_file(file.file_path)
    except Exception as e:
        print(f"{type(e)} : {e}")
        await bot.send_message(msg.chat.id,"Fișierul este mai mare de 20mb")
        return

    text = transcribe(data)

    await bot.edit_message_text(text, msg.chat.id, raspuns.id)


@bot.message_handler( content_types=["video", "video_note"])
async def transcribe_video(msg: T.Message):

    print("am primit mesaj video")

    match msg.content_type:
        case "video":
            msg_content = msg.video
        case "video_note":
            msg_content = msg.video_note
        case _:
            print("transcribe_video: wrogn content type", file=sys.stderr)
            return
    
    if msg_content is None:
        print("transcribe_video: Telebot bug", file=sys.stderr)
        return 


    raspuns = await bot.reply_to(msg, "descarcăm videoul")
    try:
        file: T.File = await bot.get_file(msg_content.file_id)
        data = await bot.download_file(file.file_path)
    except Exception as e:
        print(f"{type(e)} : {e}")
        await bot.send_message(msg.chat.id,"Fișierul este mai mare de 20mb")
        return

    tvideo_path = f"/tmp/{file.file_path.split("/")[-1]}"


    with open(tvideo_path, "wb+") as fi:
        fi.write(data)


    f = NamedTemporaryFile("wb+", suffix=".wav")
    f.close()

    ffmpeg_cmd: list =  f"ffmpeg -i {tvideo_path} {f.name}".split()
    try:
        print(ffmpeg_cmd)
        with Popen(ffmpeg_cmd, stdin=subprocess.PIPE) as proc:
            proc.communicate(input=data)
        text = transcribe(f.name)
    except Exception as e:
        print(f"{type(e)} : {e}")
        await bot.send_message(msg.chat.id,"Error :(")
        return

    finally:
        os.remove(f.name)
        os.remove(tvideo_path)

    await bot.edit_message_text(text, msg.chat.id, raspuns.id)

@bot.message_handler(commands=["ajutor","start", "help"])
async def ajutor(msg: T.Message):
    H_MESSAGE = """
Sunt un robot pentru transcrierea vocii. 
Transmite-mi un mesaj vocal, un fișier audio sau un video și eu îl voi transcrie.
"""
    
    await bot.send_message(msg.chat.id, H_MESSAGE)



async def main():
    await bot.infinity_polling(allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    asyncio.run(main())

