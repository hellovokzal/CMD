import requests as r
import telebot
bot = telebot.TeleBot("6219995606:AAG4jYJoXYOIMJuBoHDTQ9dU8X9IEjIU6xc")
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(messsge.chat.id, "Привет, напиши команду /help, чтобы узнать подробнее команд")
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список команд:\n/check <твоя ссылка> - узнать работает ли интернет или нет")
@bot.message_handler(commands=['check'])
def check(message):
    url = message.text[7:len(message.text)]
    bot.send_message(message.chat.id, f"Проверяем ссылку {url}...")
    try:
        link = r.get(url)
        bot.send_message(message.chat.id, f"Ссылка работает!\nКод: {r.status_code}")
    except:
        bot.send_message(message.chat.id, f"Ссылка не работает!\nКод: {r.status_code}")
