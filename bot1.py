import telebot
import requests

bot = telebot.TeleBot('6113365018:AAE68FI33fhI8HDHT-uLwBdlPMN9ucO5DAc')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, напиши вот такую команду:\n/check <своя ссылка>")
@bot.message_handler(commands=['check'])
def check_host(message):
    try:
        url = message.text.split()[1]
        response = requests.get(url)
        if response.status_code == 200:
            bot.reply_to(message, f"{url} is up and running!")
        else:
            bot.reply_to(message, f"{url} is down!")
    except:
        bot.reply_to(message, "Invalid URL or something went wrong.")

bot.polling()
