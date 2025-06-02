# 39-DARS. PIP VA TASHQI KUTUBXONALAR

# 1
import wikipedia

print(wikipedia.summary("Wikipedia"))

# 2
# pip install googletrans==3.1.0a0
from googletrans import Translator

tarjimon = Translator()  # Translator bu maxsus klass (tarjimon esa obyekt)
while True:
    a = input('so\'z kiriting')
    tarjima1 = tarjimon.translate(a)
    print(tarjima1.text)
    if a == '':
        break

matn_uz = "Tashkent is the capital of Uzbekistan"
tarjima = tarjimon.translate(matn_uz)

print(tarjima.text)

# 3
import requests
from pprint import pprint

manzil = "https://kun.uz/news/main"
r = requests.get(manzil)
pprint(r.text)

# 4
import requests

country = "Uzbekistan"
url = f"https://restcountries.com/v3.1/name/{country}"
a = requests.get(url)
r_json = a.json()[0]
# print(r_json.keys())
print(r_json['capital'][0])  # Capital ma'lumotini olish uchun ro'yxatdagi birinchi elementni olamiz
print(r_json)

# 5
import requests
import googletrans

url = 'https://api.adviceslip.com/advice'
r = requests.get(url)
advice = r.json()['slip']['advice']
print(advice)

translator = googletrans.Translator()
tarjima = translator.translate(advice, dest='uz')

print(tarjima.text)

# 6
import requests

from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="small-cards__default-text")
matn = "salom"
for n in news:
    matn += n.text
print(matn)
# kerakmas so'zlar
stopwords = ["учун", "бўйича", "лекин", "билан", "ва", "бор", "ҳам", "хил", "йил"]
# bulutni yaratamiz
wordcloud = WordCloud(width=1000, height=1000,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=20).generate(matn)

# plot the WordCloud image                        
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

# 7
import json
import googlemaps
from apikey import APIKEY

gmaps = googlemaps.Client(key=APIKEY)

data = gmaps.geocode('Omazor,Tashkent,Uzbekistan')

g = json.dumps(data[0], indent=4, sort_key=True)
print(g)

# ishlamadi


# 8
from fuzzywuzzy import process
from uzwords_data import words

text = "салом"
matches = process.extract(text, words, limit=3)
print(matches)

text = "талба"
match = process.extractOne(text, words)
print(match)

# 9
import wx
from googletrans import Translator

tarjimon = Translator()


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Oʻzbek-Ingliz Lugʻat')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        my_btn = wx.Button(panel, label='TARJIMA')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

        self.text_out = wx.TextCtrl(panel, style=wx.TE_READONLY)
        my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        value = self.text_ctrl.GetValue()
        if not value:
            self.text_out.SetValue("Soʻz kiritmadingiz")
        else:
            tarjima = tarjimon.translate(value, src='uz', dest='en')
            self.text_out.SetValue(tarjima.text.capitalize())


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

# 10
import cv2

# Kamera orqali video oqimini olish
cap = cv2.VideoCapture(0)

# Haar Cascade klassifikatorlarini yuklash (yuz va ko'zlarni aniqlash uchun)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    # Kameradan olingan kadrlarni o'qish
    ret, frame = cap.read()

    # Kadrni kulrang tasvirga aylantirish
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yuzlarni aniqlash
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Har bir aniqlangan yuz uchun
    for (x, y, w, h) in faces:
        # Yuzning atrofida to'rtburchak chizish
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        # Yuz hududidagi ko'zlarni aniqlash
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

        # Har bir aniqlangan ko'z uchun to'rtburchak chizish
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    # Olingan kadrni ekranga chiqarish
    cv2.imshow('Video', frame)

    # 'q' tugmasi bosilganda dasturdan chiqish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamerani to'xtatish va barcha oynalarni yopish
cap.release()
cv2.destroyAllWindows()

# 11
import cv2

# Haar kaskadlarni yuklaymiz
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')  # Ko'zlarni ham tekshirish uchun

# Yuz ifodalarini aniqlash uchun joy tayyorlaymiz
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Tabassumni aniqlaymiz
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        if len(smiles) > 0:
            cv2.putText(frame, 'Tabassum', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        else:
            cv2.putText(frame, 'Xafalik', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    cv2.imshow('Emotion Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# 12
# 27-mavzudan yangilik
import telebot
import googletrans
import requests
from googletrans import Translator
from translate_data import to_cyrillic, to_latin
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
