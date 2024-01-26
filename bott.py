import telebot

token = 'нет'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'], commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(content_types=['text'], commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Команды: \n"
                                      "/start - запуск бота\n"
                                      "/help - список команд\n")


bot.polling(none_stop=True)
