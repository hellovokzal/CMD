import telebot

import threading

import time

# Создаем токен

bot = telebot.TeleBot("6273069974:AAENVAn_UuRaSDg0_SJuiTjGS2E3BJkC5z4")

# При старте команда

@bot.message_handler(commands=['start'])

def start(message):

    bot.send_message(message.chat.id, "Привет, нужна помощь? Введи команду /help")

# Для помощи команды

@bot.message_handler(commands=['help'])

def help(message):

    bot.send_message(message.chat.id, "Список команд:\n/spam <свой номер телефона +7 только РФ, но знайте должно быть 12 цифр, если +79999999999> <секунды от 0 - 500>\n\n/vip - узнать подробнее о vip\n\n/status - информация о купленной vip доступа\n\nЕсть возможные вопросы, то напиши нам: @progress135top, @Jacktr333")

# Узнать об VIP покупке

@bot.message_handler(commands=['vip'])

def vip(message):

    bot.send_message(message.chat.id, "Сумма на вип:\n10 рублей - День\n50 рублей - Неделя\n100 рублей - Месяц\n300 рублей - Год\n\nДля Покупки Писать - @Jacktr333, @progress135top\n\nОплата - Qiwi Кошелек")

# Узнать свой статус

@bot.message_handler(commands=['status'])

def status(message):

    # Открываем файл

    with open('user.txt', 'r') as file:

        # Под каждым строкам будет чекать челов под id

        for line in file:

            users = f"{line}"

            # Если он купил vip

            if f'{message.chat.id}' in line:

                bot.send_message(message.chat.id, f"𝙎𝙩𝙖𝙩𝙪𝙨: ✯ᴠɪᴘ ✯\nᴛɪᴍᴇ: от модератора зависит")

                # Если он участник

            if message.chat.id != users:

                bot.send_message(message.chat.id,"𝙎𝙩𝙖𝙩𝙪𝙨: ✯ ᴍᴇᴍʙᴇʀ ✯\nᴛɪᴍᴇ: ʙʟᴏᴄᴋ")

                # Если он модератор

            if message.chat.id == 1477069902 or message.chat.id == 1454242973:

                bot.send_message(message.chat.id, "𝙎𝙩𝙖𝙩𝙪𝙨: ✯ ᴏᴡɴᴇʀ ✯\nᴛɪᴍᴇ: ∞")

# Пишем команду /getVip, чтобы участнику дать вип доступ

@bot.message_handler(commands=['getVip'])

def getVip(message):

    if message.chat.id == 1477069902 or message.chat.id == 1454242973:

        id = message.text[7:len(message.text)]

        try:

            bot.send_message(id, "💳 Вам выдали подписку 💳")

            bot.send_message(message.chat.id,"Вы выдали подписку!")

            

        except:

            bot.send_message(message.chat.id,"Пользователь не зарегестрирован в боте!")

    else:

        bot.send_message(message.chat.id,"Вы не админ бота!")

bot.polling()
