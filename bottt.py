import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message
from data_users import load_data, save_data

token = '6562798394:AAGf0PZVUM_lha_MNuo0LHiWyTdR_2a8DHs'
bot = telebot.TeleBot(token)

data = "users.json"
user_data = load_data(data)

location_data = load_data("locations.json")


def make_keyboard(options):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in options.keys():
        keyboard.add(KeyboardButton(i))

    return keyboard


@bot.message_handler(content_types=['text'], commands=['start'])
def start_message(message):
    global user_data
    user_id = message.chat.id
    bot.send_message(user_id, "Рекомендую включить эту песню для особой атмосферы)")

    try:
        audio = open(r'Bernth_-_Farewell.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)
        audio.close()
    except:
        bot.send_message(user_id, "Извините, не получилось отправить песню(")

    if user_id in user_data:
        user_data[user_id]["location"] = "start"
    else:
        user_data[user_id] = {"location": "start"}

    location = user_data[user_id]["location"]
    save_data(user_data, data)
    send_location(message.chat.id, location)


def send_location(chat_id, location):
    cur_location = location_data[location]
    options = cur_location["options"]
    picture_patch = cur_location["picture"]
    description = cur_location["description"]

    if "final" in cur_location:
        with open(picture_patch, "rb") as photo:
            bot.send_photo(chat_id, photo, caption=description, reply_markup=None)
        bot.send_message(chat_id, cur_location["final"], reply_markup=make_keyboard({"/start": {}}))
    else:
        with open(picture_patch, "rb") as photo:
            bot.send_photo(chat_id, photo, caption=description, reply_markup=make_keyboard(options))


@bot.message_handler(func=lambda m: True, content_types=['text'])
def handle_text_answer(message: Message):
    user_id = message.chat.id
    handle_answer(user_id, message.text)


def handle_answer(user_id, user_input):
    global user_data

    current_location = user_data[user_id]["location"]
    options = location_data[current_location]["options"]

    if user_input in options:
        next_location = options[user_input]
        user_data[user_id]["location"] = next_location
        save_data(user_data, data)
        send_location(user_id, next_location)


@bot.message_handler(content_types=['text'], commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Команды: \n"
                                      "/start - запуск бота\n"
                                      "/help - список команд\n")


bot.polling(none_stop=True)
