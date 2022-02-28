import telebot
import requests
from config import open_weather
# обращение к телепорту
from telebot import types

TOKEN = 'xxx'
bot = telebot.TeleBot(TOKEN)
import requests
from pprint import pprint
from config import open_weather
import requests
from pprint import pprint


def get_weather():
    r = requests.get(
        f"https://api.themoviedb.org/3/movie/top_rated?api_key=d10554b639e8af1d820f7ec858bc7a02"
    )
    data = r.json()
    #  pprint(data)
    text = ""
    for status in data["results"]:
       print(status["title"].encode("utf-8"))



# обработчик на команду start
@bot.message_handler(commands=['start'])
def start(message):
    # обращение к клавиатуре(меню) + чтобы кнопки были по размеру
    markup = types.ReplyKeyboardMarkup(row_width=2)

    # 1 кнопка
    item_new = types.KeyboardButton('🔥 Новинки кино')
    item_popular = types.KeyboardButton('🎬 Популярное кино')
    item_dock = types.KeyboardButton('🔎 Информация')
    item_filter = types.KeyboardButton('🙃 Жанры кино')
    markup.add(item_new, item_popular, item_dock, item_filter)

    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    # личное сообщение
    if message.chat.type == 'private':
        if message.text == '🔥 Новинки кино':
            markup = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton('1')
            item2 = types.KeyboardButton('2')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, "здесь пока пусто", reply_markup=markup)

        elif message.text == '🎬 Популярное кино':
            markup = types.ReplyKeyboardMarkup(row_width=2)
            item1 = types.KeyboardButton('1')
            item2 = types.KeyboardButton('2')
            back = types.KeyboardButton('⬅ Назад')
            markup.add(item1, item2, back)
            bot.send_message(message.chat.id, "здесь пока пусто", reply_markup=markup)
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
            item_filter = types.KeyboardButton('🙃 Жанры кино')
            markup.add(item_new, item_popular, item_dock, item_filter)
            bot.send_message(message.chat.id, "⬅ Назад", reply_markup=markup)
        elif message.text == "Разработчик":
            bot.send_message(message.chat.id, "Антон Московский")
        elif message.text == "О боте":
            markup = types.ReplyKeyboardMarkup(row_width=2)
            bot.send_message(message.chat.id, f"{get_weather()}", reply_markup=markup)
        elif message.text == "🙃 Жанры кино":
            markup_inline = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Аниме', callback_data='question1')
            item2 = types.InlineKeyboardButton('Детектив', callback_data='question2')
            item3 = types.InlineKeyboardButton('Военный', callback_data='question3')
            item4 = types.InlineKeyboardButton('Комедия', callback_data='question4')
            item5 = types.InlineKeyboardButton('Мультфильм', callback_data='question5')
            item6 = types.InlineKeyboardButton('Ужасы', callback_data='question6')

            markup_inline.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, "Выбери жанр кино", reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'question1':
            bot.send_message(call.message.chat.id, get_weather())

    # не отключался


bot.polling(none_stop=True)
