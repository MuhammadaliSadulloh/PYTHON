import telebot
import googletrans
import requests
from googletrans import Translator
from python.translate_data import to_cyrillic, to_latin
from telebot import types

# Bot token
TOKEN = "7114983403:AAG9G8uk9zM1ANVNaQy1y-Z7S1ExMTlN-sw"
bot = telebot.TeleBot(TOKEN)

# Translator obyektini yaratamiz
tarjimon = Translator()

# Foydalanuvchi holatini saqlash uchun lug'at va foydalanuvchilar ro'yxati
user_states = {}
user_list = set()  # Foydalanuvchilarni saqlash uchun to'plam


# Start buyrug'i
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_list.add(message.chat.id)  # Foydalanuvchini ro'yxatga qo'shamiz
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("Lotindan Kirillga")
    btn2 = types.KeyboardButton("Tarjima (Ingliz tiliga)")
    btn3 = types.KeyboardButton("(Advice)maslahat")
    btn4 = types.KeyboardButton("Help")
    btn5 = types.KeyboardButton("Stop")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Tanlang:", reply_markup=markup)


# Stop funksiyasi - holatni tozalash
def stop(message):
    chat_id = message.chat.id
    if chat_id in user_states:
        del user_states[chat_id]  # Foydalanuvchining holatini o'chiramiz
        bot.send_message(chat_id, "To'xtatildi. Holat tozalandi.")


# Foydalanuvchi xabarlarini qayta ishlash
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text

    # Tugmalarni qayta ishlash va avval "Stop" funksiyasini chaqirish
    if text in ["Lotindan Kirillga", "Tarjima (Ingliz tiliga)", "(Advice)maslahat", "Help"]:
        stop(message)  # Avval "Stop" funksiyasini ishga tushiramiz

    # Yangi tugmalar uchun shartlar
    if text == "Lotindan Kirillga":
        user_states[chat_id] = "lotin_kirill"
        bot.send_message(chat_id, "Matnni kiriting:")

    elif text == "Tarjima (Ingliz tiliga)":
        user_states[chat_id] = "tarjima"
        bot.send_message(chat_id, "Tarjima qilish uchun so'z kiriting:")

    elif text == "(Advice)maslahat":
        user_states[chat_id] = "maslahat"

    elif text == "Help":
        bot.send_message(chat_id,
                         "Bot ishlashi haqida:\n1. 'Lotindan Kirillga' tugmasi - matnni kirillga aylantiradi.\n2. 'Tarjima' tugmasi - matnni ingliz tiliga tarjima qiladi.\n3. 'Stop' tugmasi - jarayonni to'xtatadi va bot holatini tozalaydi.")

    elif text == "Stop":
        stop(message)

    # Holatga ko'ra funksiyalarni chaqiramiz
    if chat_id in user_states:
        state = user_states[chat_id]

        if state == "lotin_kirill":
            lotin_kirill(message)
        elif state == "tarjima":
            tarjima(message)
        elif state == "maslahat":
            maslahat(message)


# Lotindan Kirillga o'girish
def lotin_kirill(message):
    chat_id = message.chat.id
    matn = message.text
    javob = to_cyrillic(matn) if matn.isascii() else to_latin(matn)
    bot.send_message(chat_id, javob)


# Ingliz tiliga tarjima qilish
def tarjima(message):
    chat_id = message.chat.id
    matn = message.text
    tarjima_qilingan = tarjimon.translate(matn, src='uz', dest='en')
    bot.send_message(chat_id, tarjima_qilingan.text)


# Maslahat olish
def maslahat(message):
    chat_id = message.chat.id
    url = 'https://api.adviceslip.com/advice'
    r = requests.get(url)
    advice = r.json()['slip']['advice']
    tarjima1 = tarjimon.translate(advice, dest='uz')
    bot.send_message(chat_id, advice)
    bot.send_message(chat_id, tarjima1.text)


# Foydalanuvchilarni ko'rish
@bot.message_handler(commands=['users'])
def show_users(message):
    if message.chat.id == 5982685783:  # Faqat admin ko'rishi mumkin
        bot.send_message(message.chat.id, f"Foydalanuvchilar: {list(user_list)}")
    else:
        bot.send_message(message.chat.id, "Sizda bu komanda mavjud emas.")


# Foydalanuvchilarga xabar yuborish
@bot.message_handler(commands=['send_message'])
def broadcast_message(message):
    if message.chat.id == 5982685783:  # Faqat admin yuborishi mumkin
        msg = bot.send_message(message.chat.id, "Yuboriladigan xabarni kiriting:")
        bot.register_next_step_handler(msg, send_to_all)
    else:
        bot.send_message(message.chat.id, "Sizda bu komanda mavjud emas.")


def send_to_all(message):
    for user in user_list:
        try:
            bot.send_message(user, message.text)
        except Exception as e:
            print(f"Xatolik: {e}")


# Foydalanuvchi chat ID'sini olish
@bot.message_handler(commands=['my_id'])
def get_my_id(message):
    bot.send_message(message.chat.id, f"Sizning chat ID: {message.chat.id}")


bot.infinity_polling()
