import telebot
import requests

import config
from config import top_rated
from config import now_playing
from config import popular_actors
# обращение к телепорту
from telebot import types

TOKEN = '5203866796:AAGCC8E0YlMO-AllwGzNrlsugXUKjtFX5do'
bot = telebot.TeleBot(TOKEN)
from pprint import pprint

# обработчик на команду start
@bot.message_handler(commands=['start'])
def start(message):
    # обращение к клавиатуре(меню) + чтобы кнопки были по размеру
    markup = types.ReplyKeyboardMarkup(row_width=2)

    # 1 кнопка
    item_new = types.KeyboardButton('🔥 Новинки кино')
    item_popular = types.KeyboardButton('🎬 Популярное кино')
    item_dock = types.KeyboardButton('🔎 Информация')
    item_filter = types.KeyboardButton('🙃 Актеры')
    markup.add(item_new, item_popular, item_dock, item_filter)

    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    # личное сообщение
    if message.chat.type == 'private':
        if message.text == '🔥 Новинки кино':
            markup = types.ReplyKeyboardMarkup(row_width=2)

            back = types.KeyboardButton('⬅ Назад')
            markup.add(back)
            bot.send_message(message.chat.id, now_playing(), reply_markup=markup)


        elif message.text == '🎬 Популярное кино':
            markup = types.ReplyKeyboardMarkup(row_width=2)
            back = types.KeyboardButton('⬅ Назад')
            markup.add(back)
            bot.send_message(message.chat.id, top_rated(), reply_markup=markup)
        elif message.text == '🔎 Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_name = types.KeyboardButton('Разработчик')
            item_info = types.KeyboardButton('О боте')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item_name, item_info, back)
            bot.send_message(message.chat.id, "🔎 Информация", reply_markup=markup)
        elif message.text == '⬅ Назад':
            markup = types.ReplyKeyboardMarkup(row_width=2)
            # 1 кнопка
            item_new = types.KeyboardButton('🔥 Новинки кино')
            item_popular = types.KeyboardButton('🎬 Популярное кино')
            item_dock = types.KeyboardButton('🔎 Информация')
            item_filter = types.KeyboardButton('🙃 Актеры')
            markup.add(item_new, item_popular, item_dock, item_filter)
            bot.send_message(message.chat.id, "⬅ Назад", reply_markup=markup)
        elif message.text == "Разработчик":
            bot.send_message(message.chat.id, "Антон Московский")
        elif message.text == "О боте":
            markup = types.ReplyKeyboardMarkup(row_width=2)
            bot.send_message(message.chat.id, "Бот берет данные с сайта The Movie DB.", reply_markup=markup)
        elif message.text == "🙃 Актеры":
            markup = types.ReplyKeyboardMarkup(row_width=2)

            back = types.KeyboardButton('⬅ Назад')
            markup.add(back)
            bot.send_message(message.chat.id, popular_actors(), reply_markup=markup)

    # не отключался


bot.polling(none_stop=True)
