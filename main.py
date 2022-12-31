import os

import requests
import telebot
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

TG_TOKEN = os.getenv("TG_TOKEN")

bot = telebot.TeleBot(TG_TOKEN, parse_mode='MARKDOWN')

standard_message = "Hi, I'll will send an artifical generated face if you send me a /generate command"

@bot.message_handler(commands=['generate'])
def send_random_face(message):
    random_photo = Image.open(requests.get('https://thispersondoesnotexist.com/image', stream=True).raw)
    bot.send_photo(message.chat.id, random_photo)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, standard_message)


bot.infinity_polling()
