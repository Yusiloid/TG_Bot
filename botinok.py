import pprint
import time

import telebot
import pprint
token = ''


bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['test13'])
def send_welcome(message):
    bot.reply_to(message, 'https://forms.gle/wr1NX9AQopyudfYK9')

@bot.message_handler(commands=['test17'])
def send_welcome(message):
    bot.reply_to(message, 'https://forms.gle/9LypYZsMRNqx9wS99')


@bot.message_handler(commands= ['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет, дорогой путник!')

@bot.message_handler(commands= ['help'])
def send_welcome(message):
    bot.reply_to(message, 'Нужна помощь?')
''' 
@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(1000):
        time.sleep(0.5)
        bot.send_message(message.chat.id, i + 1)
'''
@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message,f'***{text.upper()}!***')

@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'Текст содержит слово плохой')
        return
    text = message.text[::-1]
    bot.reply_to(message, text)

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)
    file_ID = 'CAACAgIAAxkBAAIBq2XymcpD4DttegQulrlbX-dL52aDAAIIAANPjZIkhUixFLvqiXM0BA'
    bot.send_sticker(message.chat.id,file_ID)




bot.polling()