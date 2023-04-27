import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6196363236:AAE8pjL3j0EuNcOs9QfzfsdvZZwGWCL0IU0')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который узнает информацию о веб-сайте. Просто отправь мне ссылку на сайт.")

@bot.message_handler(func=lambda message: True)
def get_website_info(message):
    try:
        url = message.text
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').text
        description = soup.find('meta', attrs={'name': 'description'})['content']
        keywords = soup.find('meta', attrs={'name': 'keywords'})['content']
        bot.reply_to(message, f"Название сайта: {title}\nОписание: {description}\nКлючевые слова: {keywords}")
    except:
        bot.reply_to(message, "Произошла ошибка. Проверьте правильность ссылки и попробуйте еще раз.")

bot.polling()
