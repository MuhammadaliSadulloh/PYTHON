import telebot

# Bot tokeningiz
TOKEN = "7114983403:AAG9G8uk9zM1ANVNaQy1y-Z7S1ExMTlN-sw"
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# Foydalanuvchilar ro'yxati
user_list = []


# Foydalanuvchini ro'yxatga qo'shish funksiyasi
def add_user(user_id):
    if user_id not in user_list:
        user_list.append(user_id)


# /start komandasi orqali foydalanuvchini ro'yxatga olish
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.chat.id
    add_user(user_id)
    bot.reply_to(message, "Assalomu alaykum! Botga xush kelibsiz!")


# # Oddiy xabarlar uchun handler
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     user_id = message.chat.id
#     add_user(user_id)
#     bot.reply_to(message, f"Xabaringiz qabul qilindi: {message.text}")


# Admin uchun barcha foydalanuvchilarning ro'yxatini ko'rish
@bot.message_handler(commands=['users'])
def show_users(message):
    if message.chat.id == 5982685783:  # Admin ID sini qo'shing
        users = '\n'.join([str(user) for user in user_list])
        bot.reply_to(message, f"Foydalanuvchilar ro'yxati:\n{users}")
    else:
        bot.reply_to(message, "Sizda bu komanda uchun ruxsat yo'q!")


# Bot orqali xabar yuborish funksiyasi
def send_broadcast(message_text):
    for user_id in user_list:
        bot.send_message(user_id, message_text)


# Admin uchun xabar yuborish komandasi
@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    if message.chat.id == 5982685783:
        msg = message.text.replace('/broadcast ', '')
        send_broadcast(msg)
        bot.reply_to(message, "Xabar barcha foydalanuvchilarga yuborildi!")
    else:
        bot.reply_to(message, "Sizda bu komanda uchun ruxsat yo'q!")


# Botni doimiy ishlash uchun
bot.infinity_polling()
