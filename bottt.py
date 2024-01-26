import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from data_users import load_data, save_data

token = 'нет'
bot = telebot.TeleBot(token)

data_path = "users.json"
user_data = load_data(data_path)


def make_keyboard(buttons):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for ell in buttons:
        keyboard.add(KeyboardButton(ell))

    return keyboard


@bot.message_handler(content_types=['text'], commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(content_types=['text'], commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Команды: \n"
                                      "/start - запуск бота\n"
                                      "/help - список команд\n")


bot.polling(none_stop=True)