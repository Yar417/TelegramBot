from key.py import bot_key
import telebot
from telebot import types

bot = telebot.TeleBot(bot_key)


@bot.message_handler(commands=['start'])  # отслеживание команд и их выполнение
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html') 


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Vizit site', url='https://google.com'))
    bot.send_message(message.chat.id, 'go to site', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('GitHub')

    start = types.KeyboardButton('Start')

    markup.add(website, start)

    bot.send_message(message.chat.id, 'go to site', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, 'Hello to you!', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Hello to you! {message}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('1.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Don`t understand you!', parse_mode='html')


@bot.message_handler(content_types=['photo'])  # отслеживание отправки
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Good shot!')


bot.polling(none_stop=True)
