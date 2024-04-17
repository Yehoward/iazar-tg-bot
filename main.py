from os import environ
import sys
import asyncio

from telebot import TeleBot, types as T
from telebot.async_telebot import AsyncTeleBot
from telebot.util import quick_markup

from transformers import pipeline

TOKEN = environ["KEY"]

bot = AsyncTeleBot(TOKEN)



pipe = pipeline(model="Yehoward/whisper-small-ro")

def transcribe(audio: bytes ) -> str:
    return pipe(audio)["text"]

def is_voice(msg: T.Message) -> bool:
    return msg.voice is not None 

    

@bot.message_handler( content_types=["voice"])
async def transcribe_voice(msg: T.Message):

    print("am primit mesaj vocal")
    if msg.voice is None:
        print("transcribe_voice: Telebot bug", file=sys.stderr)
        return 

    raspuns = await bot.reply_to(msg, "descarcăm audioul")
    file: T.File = await bot.get_file(msg.voice.file_id)
    data = await bot.download_file(file.file_path)

    text = transcribe(data)

    await bot.edit_message_text(text, msg.chat.id, raspuns.id)

@bot.message_handler(commands=["ajutor","start", "help"])
async def ajutor(msg: T.Message):
    H_MESSAGE = """
Sunt un robot pentru transcrierea vocii. 
Transmite-mi un mesaj vocal și eu îl voi transcrie.
"""
    
    await bot.send_message(msg.chat.id, H_MESSAGE)



async def main():
    await bot.infinity_polling(allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    asyncio.run(main())

