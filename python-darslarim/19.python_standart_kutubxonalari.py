# 38-DARS. PYTHON STANDART KUTUBXONASI


# 1.Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

# 2.Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring

# 3.Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini 
# qaytaruvchi funksiya yozing

# 4.Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni 
# andoza yordamida tekshiring

# 5.Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. 
# Quyidagi matndan namuna sifatida foydalanishingiz mumkin:

#     Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi:
# https://youtu.be/vsxJPRLXpgI
# Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va 
# metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: 
# https://python.sariq.dev/testing/37-klass-test

# 1
import datetime as dt

hozir = dt.datetime.now()
kun = hozir.date()


def sanalar():
    for i in range(10):
        sana = kun + (i + 1) * dt.timedelta(days=14)
        print(sana)


# 2
print(dt.date.today() + dt.timedelta(days=14))


def ramadan():
    ramazon = dt.date(2025, 3, 10)
    qurbon_hayit = dt.date(2025, 6, 10)
    return f'ramazongacha {ramazon - dt.date.today()},qurbon hayitigacha {qurbon_hayit - dt.date.today()}'


# 3  
def my_birthday(tugulgan_sana):
    bugun = dt.date.today()
    farq = bugun - tugulgan_sana
    yillar = farq.days // 365
    oylar = (farq.days % 365) // 30
    kunlar = (farq.days % 365) % 30
    return f'{yillar} yil {oylar} oy {kunlar} kun'


print(my_birthday(dt.date(2005, 12, 1)))

# 4
import re

tel = '+998990381952'
andoza = r"\+998\d{9}$"
print(re.match(andoza, tel))


# 5
def find_urls(text):
    andozah = r"https?://[^\s]+"
    urls = re.findall(andozah, text)
    return urls


matn = """Assalom alaykum hurmatli do\'stlar. Navbatdagi darsimiz YouTubega yuklandi:
https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va 
metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: 
https://python.sariq.dev/testing/37-klass-test"""

print(find_urls(matn))
