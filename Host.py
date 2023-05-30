import telebot
import random
import time
randomizator = "off"
bot = telebot.TeleBot("5879556659:AAH4ghYVO0Iq99pJN9ilqD7LbGDl9ddTXwY")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Введи /help, чтобы узнать все")
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список команд:\n/on - Включить рандомизацию для всех пользователей\n/off - Выключить рандомизацию для всех пользователей\n/check_randomizator - Чекает включены или нет рандомизаторы\n/starting <свой пример> - вводите свой любой пример и если включена команда /on, то будет рандомизировать текст либо пример")
@bot.message_handler(commands=['on'])
def on(message):
    global randomizator
    randomizator = "on"
    bot.send_message(message.chat.id, "Для всех пользователей была включена рандомизация")
@bot.message_handler(commands=['off'])
def off(message):
    global randomizator
    randomizator = "off"
    bot.send_message(message.chat.id, "Для всех пользователей была выключена рандомизация")
@bot.message_handler(commands=['check_randomizator'])
def check_randomizator(message):
    global randomizator
    if randomizator == "on":
        bot.send_message(message.chat.id, f"Рандомизатор включен\nКод рандомизатора: {randomizator}")
    else:
        bot.send_message(message.chat.id, f"Рандомизатор выключен\nКод рандомизации: {randomizator}")
@bot.message_handler(commands=['starting'])
def starting(message):
    global randomizator
    num = random.randint(0, 4)
    if randomizator == "on":
        if num == 0 or num == 1:
            bot.send_message(message.chat.id, "Пошел нахуй недоделанное чмо, чтобы твоя мать ебалась с отчимом")
        if num == 2:
            bot.send_message(message.chat.id, "Ты тупой или что? Я сказал тебе иди нахуй, чтобы твоя мать сосалась с отчимом или с тобой")
        if num == 3:
            bot.send_message(message.chat.id, "Ты понимаешь, что твоя мать ебалась с кем-то, чтобы облизала тебя спермой")
        if num == 4:
            bot.send_message(message.chat.id, "Ответ: Хуй тебе))")
            time.sleep(0.5)
            bot.send_message(message.chat.id, "Ахахахахахахахахахаха")
    else:
        try:
            started = message.text[10:len(message.text)]
            started = eval(started)
            bot.send_message(message.chat.id, f"Ответ: {started}")
        except:
            bot.send_message(message.chat.id, "Неправильно ввели!")
bot.polling()
