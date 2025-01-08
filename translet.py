import telebot
import os
from googletrans import Translator

API_TOKEN=os.environ.get('API_TOKEN')
bot=telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message,"لطفا متن فارسی را وارد کنید و در انتها اختصار زبان مورد نظر را بنوسید " )

@bot.message_handler(func=lambda message: true)
def translet_command(message):
    text=message.text
    language=text.split()[-1]
    translet=Translator()
    transleted_text=translet.translate(text,dest="language").text
    bot.reply_to(message,transleted_text)






@bot.infinity_polling()