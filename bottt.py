import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from data_users import load_data, save_data
from locations import location_data

token = '6457885818:AAHVcYEAP10xizU2FAHaVRNcub1ViPwjrq0'
bot = telebot.TeleBot(token)

data = "users.json"
user_data = load_data(data)


def make_keyboard(options):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in options.keys():
        keyboard.add(KeyboardButton(i))

    return keyboard


@bot.message_handler(content_types=['text'], commands=['start'])
def start_message(message):
    global user_data
    user_id = message.chat.id
    bot.send_message(user_id, "Привет!")

    if user_id in user_data:
        user_data[user_id]["location"] = "start"
    else:
        user_data[user_id] = {"location": "start"}

    location = user_data[user_id]["location"]
    send_location(message.chat.id, location)
    save_data(user_data, data)


def send_location(chat_id, location):
    cur_location = location_data[location]
    options = cur_location["options"]
    picture_patch = cur_location["picture"]
    description = cur_location["description"]

    keyboard = make_keyboard(options)

    with open(picture_patch, "rb") as photo:
        bot.send_photo(chat_id, photo, caption=description, reply_markup=keyboard)


@bot.message_handler(content_types=['text'], commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Команды: \n"
                                      "/start - запуск бота\n"
                                      "/help - список команд\n")


bot.polling(none_stop=True)