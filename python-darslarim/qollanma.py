#
#
#

APPEND
cars.append('audi')
# append bu lug`atning oxiriga o`zgaruvchi qo`shadi

INSERT
cars.insert(5, 'ferrari')
# insert bu kiritilgan index o`rnida yangi o`zgaruvchi qo`shadi

TITLE
print(cars.title())
# title o`zgaruvchining bosh harfini katta harflar bilan yozib beradi

REMOVE
cars.remove('mersedez benz')
# remove bu aytilgan o`zgaruvchini lug`atdan chiqarib tashlaydi

SORT
cars.sort()
# sort bu o`zgaruvchilarni alifbo tartibida tartiblayi

LEN
len(davlatlar)
# len>>>elementlar sonini

REVERSE
davlatlar.reverse()
# reverse ro'yxat elemntlarini teskari tartiblaydi
print(sorted(sonlar, reverse=True))

FOR
for daraja in sonlar:
# for takrorlash operatori

LIST
RANGE
sonlar = list(range(11, 101, 2))
# list funksiyasi ro'yxatni yaratish uchun ishlatiladi.
# range funksiyasi esa berilgan oraliqdagi sonlar ketma-ketligini
# yaratish uchun ishlatiladi.

TUPLE
nonushta = tuple(nonushta)
# tuple ro'yxatni o'zgarmas royxatga aylantiradi

UPPER
avto.upper()
# ro'yxat ichidagi elementni barcha harflarini katta haflar billan yozadi

LOWER
ism.lower()
# so'zdagi barcha harflarni kichik harflar bilan yozadi

GET
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.get("model")
print(x)
# get model elementining qiymatini olish

ITEMS
lugat = {'yaxshi': 'good', 'kitob': 'book', 'dastur': 'program'}
for key, value in lugat.items():
    print(key, ':', value)
# items() metodining yordamida Python lug'atining har bir
# elementini (kalit va qiymatni) o'z ichiga olgan iterator
# (yordamchi) qaytariladi. Bu metod lug'atni kalit-qiymat juftliklarining
# barchasini o'z ichiga oladi.

CAPITALIZE
satr = "salom dunyo"
print(satr.capitalize())  # Chiqarish: Salom dunyo
# capitalize() metodining vazifasi, bir satrning birinchi harfini
# bosh harf qilib qaytarishdir. Bu metod faqatgina birinchi harfni o'zgartiradi,
# boshqa harflarni o'zgartirmaydi.

POP
ismlar = ["Ali", "Vali", "Hasan", "Husan"]
uchrashuv = ismlar.pop()
print(uchrashuv)  # Chiqarish: Husan
print(ismlar)  # Chiqarish: ["Ali", "Vali", "Hasan"]
# pop() metodining vazifasi, ro'yxatning eng oxirgi elementini olib
# tashlashdir va o'chirilgan elementni qaytaradi. Agar ro'yxat bo'sh
# bo'lsa yoki indeks kiritilmasa, xato (IndexError) bo'ladi.


ROUND
print(round(4.6))  # 5
print(round(4.678, 2))  # 4.68
print(round(23, -1))  # 20
# round yaxlitlashda yordam beradi


ABS
print(abs(-3.14))  # 3.14
print(abs(3.14))  # 3.14
# abs() funksiyasi sonning absolyut qiymatini hisoblash uchun ishlatiladi


10 // 3  # 3
10 % 3  # 1
# a // b operatori a ni b ga bolganda nechta toliq qism chiqishini hisoblaydi.
# a % b operatori a ni b ga bolganda nechta qoldiq qolishini hisoblaydi.


PASS
OPERATORI


class User:
    def __int__(self, name, username, email):
        self.name = name
        self.uname = username
        self.mail = email

    def describe():
        pass

    def get_email():
        pass


# Pythonda hech qanday vazifani bajarmaydigan pass operatori mavjud.
# Bu operatordan bo'sh metodlar yaratishda foydalanish mumkin. Misol 
# uchun siz klassingiz uchun muhim metodlarni bilasiz, lekin metod 
# badani hali tayyor emas. Agar metod badanini bo'sh qoldirsangiz, 
# Python IndentationError xatosini qaytaradi. Shunday xolatlarda, 
# funksiya badaniga pass operatorini qo'yib ketishimiz mumkin:
# pass operatoridan if-else, for, while 
# operatorlari badanida ham foydalanish mumkin.


DIR
FUNKSIYASINI
ISHLATISH


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]


print(see_methods(Talaba))
['get_age', 'get_fullname', 'get_info', 'get_lastname',
 'get_name', 'set_bosqich', 'update_bosqich']

# Agar dir() funksiyasiga klass emas, obyekt 
# uzatsak metodlardan tashqari xususiyatlar ham chiqib keladi:
print(see_methods(talaba1))
['bosqich', 'familiya', 'get_age', 'get_fullname',
 'get_info', 'get_lastname', 'get_name', 'ism', 'set_bosqich',
 'tyil', 'update_bosqich']

ROYXATLAR
BLAN
ISHLASH
USULLARI
# Shu o'rinda Pythonda ro'yxatlar bilan ishlashning 
# qulayliklaridan birini ham ko'rsatib o'tsak. 
# Yuqoridagi kodimizning oxirgi qatorida e'tibor bersangiz,
# biz yangi ro'yxat shakllantirishda 1 qator koddan foydalandik:

[talaba.get_info() for talaba in self.talabalar]
# Kodimizni tahlil qilsak, self.talabalar ichidagi har bir talaba 
# uchun get_info() metodini bajar degan ma'no kelib chiqadi. Kodni kvadrat 
# qavslar ichiga olganimiz uchun esa, har bir tsikl natijasi avtomat ravishda 
# ro'yxatga qo'shib boriladi.
# ------
# Mana endi metodga murojat qilib, talabalar haqida ma'lumot olishimiz mumkin:
mat_talabalar = matematika.get_students()
print(mat_talabalar)

NUQTA
YOKI
METOD?

# Pythondagi obyketlarning o'ziga xos xususiyatlaridan biri,
# obyektning xususiyatiga nuqta orqali murojat qilish mumkin. 
# Misol uchun avval yaratagn talaba1 obyektining ismini bilish 
# uchun talaba1.ism deb yozish kifoya.

# Bu o'ziga yarasha qulay bo'lsada, bu usuldan foydalanmagan afzal. 
# Sababi, vaqt o'tib klassingiz takomillashishi, uning ba'zi 
# xususiyatlari o'zgarishi, o'chirilishi yoki almashtirilishi mumkin. 
# Shunday holatlarda nuqta orqali murojat qilish siz kutgan natijani 
# bermasligi va dastur xato ishlashiga olib kelishi mumkin. 
# Bunday holatlarning oldini olish uchun esa, obyektning xususiyatlarini 
# metod orqali olishni odat qilish tavsiya qilinadi. Huddi shu kabi, 
# obyektning xususiyatlarini yangilash uchun ham alohida metodlar yozga afzal.

# Dasturchilar orasida obyektning xususiyatlarini 
# o'zgartiradigan metodlarni set (o'zgartir) so'zi bilan, 
# xususiyatlarni qaytaradigan metodlarni esa get (olish) 
# so'zi bilan boshlash qoida qilib olingan. 
# Masalan: set_name() va get_name() kabi.

# Agar yuqoridagi qoidalarga amal qilgan holda, Talaba klassimizni 
# yangilaydigan bo'lsak, u tahminan shunday ko'rinishga ega bo'ladi:

class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich

    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1

    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil


__dict__
METODI
# Yuqorida zikr qilingan dunder metodlardan biri bu __dict__ 
# metodi bo'lib, bu metod obyketning xususiyatlarini lug'at 
# ko'rinishida qaytaradi:

print(talaba1.__dict__)
{'ism': 'Alijon', 'familiya': 'Valiyev', 'tyil': 2000, 'bosqich': 1}
# Natijadan faqatgina kalitlarni ajratib olsak, obyektning xususiyatlari chiqadi:

print(talaba1.__dict__.keys())
dict_keys(['ism', 'familiya', 'tyil', 'bosqich'])

OBYEKTNING
XUSUSIYATLARI
VA
METODLARINI
KORISH
# Obyektlar bilan ishlaganda, o'z-o'zidan shu obyektga tegishli 
# xususiyatlar va metodlarni bilish talab qilinadi. Agar obyekt 
# tegishli bo'lgan klassni o'zimiz yaratgan bo'lsak, istalgan payt 
# klass ichini ko'rib olishimiz mumkin. Lekin boshqalar yaratgan 
# klass haqida ma'lumot olish talab qilinsa, buning bir nechta yo'li bor.

dir()
FUNKSIYASI
# dir() funksiyasi yordamida istalgan obyekt yoki klassning 
# xususiyatlari va metodlarini ko'rib olishimiz mumkin:

dir(Talaba)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'get_age',
 'get_fullname',
 'get_info',
 'get_lastname',
 'get_name',
 'set_bosqich',
 'update_bosqich']


# Lekin bunda har bir klass bilan keluvchi maxsus dunder metodlar
# ham chiqib keldi. Dunder metodlar ikki pastki chiziq (__) bilan 
# boshlanadi va maxsus holatlar uchun saqlab qo'yilgan. Biz hozircha 
# faqat __init__ metodi bilan tanishdik, qolganlari bilan keyingi 
# darslarimizda yana ko'rishamiz. Dunder metodlardan keyin esa biz 
# murojat qilishimiz mumkin bo'lgan metodlar ro'yxati kelgan.

# Dunder — double underscore (ikki pastki chiziq) so'zlarining qisqartmasi.

# Keling dunder metodlarni tashlab, bizga kerak metodlarni qaytaruvchi 
# sodda funksiya yozamiz:

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]


print(see_methods(Talaba))
['get_age', 'get_fullname', 'get_info', 'get_lastname', 'get_name', 'set_bosqich', 'update_bosqich']
# Agar dir() funksiyasiga klass emas, obyekt uzatsak metodlardan tashqari 
# xususiyatlar ham chiqib keladi:

print(see_methods(talaba1))
['bosqich', 'familiya', 'get_age', 'get_fullname', 'get_info', 'get_lastname', 'get_name', 'ism', 'set_bosqich', 'tyil',
 'update_bosqich']

TAQQOSLASH
METODLARI

1. ** `assertEqual(a, b)` ** - `a`
va
`b`
qiymatlari
teng
bo
'lishini tasdiqlaydi (`a == b`).
2. ** `assertNotEqual(a, b)` ** - `a`
va
`b`
qiymatlari
teng
emasligini
tasdiqlaydi(`a != b`).
3. ** `assertTrue(x)` ** - `x`
ning
qiymati
`True`
ekanligini
tasdiqlaydi.
4. ** `assertFalse(x)` ** - `x`
ning
qiymati
`False`
ekanligini
tasdiqlaydi.
5. ** `assertIs(a, b)` ** - `a`
obyekt
`b`
obyekt
bilan
ayni
obyekt
ekanligini
tasdiqlaydi.
6. ** `assertIsNot(a, b)` ** - `a`
obyekt
`b`
obyekt
bilan
bir
xil
emasligini
tasdiqlaydi.
7. ** `assertIsNone(x)` ** - `x`
ning
qiymati
`None`
ekanligini
tasdiqlaydi.
8. ** `assertIsNotNone(x)` ** - `x`
ning
qiymati
`None`
emasligini
tasdiqlaydi.
9. ** `assertIn(a, b)` ** - `a`
qiymati
`b`
ichida
borligini
tasdiqlaydi.
10. ** `assertNotIn(a, b)` ** - `a`
qiymati
`b`
ichida
yo
'qligini tasdiqlaydi.
11. ** `assertIsInstance(a, b)` ** - `a`
qiymati
`b`
klassining
vorisi
ekanligini
tasdiqlaydi.
12. ** `assertNotIsInstance(a, b)` ** - `a`
qiymati
`b`
klassining
vorisi
emasligini
tasdiqlaydi.

# Bu metodlar Pythonning unit testlarini avtomatlashtirishda foydali bo'lib, dastur kodini sinovdan o'tkazishda keng qo'llaniladi.


re
Moduli
Haqida
Chuqurroq
Tushuncha

# re moduli Python'da regular expressions (muntazam ifodalar) bilan ishlash 
# uchun ishlatiladi. Muntazam ifodalar matndan muayyan naqshlar bo'yicha qidirish, 
# almashtirish yoki tekshirish uchun ishlatiladi.

re
Moduli
Funksiyalari:
re.match(pattern, string):

# Bu funksiya string matnining boshidan pattern bilan mos keladigan qismni topadi. 
# Agar mos kelsa, Match obyekti qaytaradi, aks holda None qaytaradi.
re.search(pattern, string):

# Bu funksiya string ichidagi pattern bilan mos keladigan birinchi qismni qidiradi. 
# Agar topilsa, Match obyekti qaytaradi, aks holda None qaytaradi.
re.findall(pattern, string):

# Bu funksiya string ichidagi pattern bilan mos keladigan barcha qismalarni topadi 
# va ularni ro'yxat shaklida qaytaradi.
re.sub(pattern, repl, string):

# Bu funksiya string ichidagi pattern ga mos keladigan barcha qismalarni repl bilan 
# almashtiradi va yangi satrni qaytaradi.
# Muntazam Ifodalar Misollari:

\d: Bitta
raqam(0 - 9).
\w: Bitta
so
'z belgisi (harf, raqam yoki pastki chiziq).
\s: Bitta
bo
'shliq belgisi (bo'
sh
joy, tab
va
h.k.).
[abc]: a, b, yoki
c
ga
mos
keladigan
har
qanday
belgi.
[ ^ abc]: a, b, yoki
c
dan
boshqa
har
qanday
belgi.
# re moduli orqali siz matnlarda juda ko'p turli xil qidiruv va manipulyatsiyalarni 
# amalga oshirishingiz mumkin.

uiid

filter
mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", "tarvuz", "qovun", "banan"]
mevalar_b = list(filter(lambda meva: meva.startswith('b'), mevalar))
mevalar_a_r = list(filter(lambda meva: (meva.startswith('a') and meva.endswith('r')), mevalar))
print(mevalar_b)
print(mevalar_a_r)




DEQUE
from collections import deque

# Yangi deque yaratish
d = deque()

# Oxiriga element qo'shish (append)
d.append('A')
d.append('B')

# Boshiga element qo'shish (appendleft)
d.appendleft('C')

print(d)  # deque(['C', 'A', 'B'])

# Oxiridan element olish (pop)
d.pop()  # 'B' ni oladi va o'chiradi

# Boshidan element olish (popleft)
d.popleft()  # 'C' ni oladi va o'chiradi

print(d)  # deque(['A'])

Deque metodlari:
append(x): x elementini oxiriga qo‘shadi.
appendleft(x): x elementini boshiga qo‘shadi.
pop(): Oxiridan elementni oladi va o‘chiradi.
popleft(): Boshidan elementni oladi va o‘chiradi.
extend(iterable): Oxiriga iterable obyektdan elementlarni qo'shadi.
extendleft(iterable): Boshiga iterable obyektdan elementlarni qo'shadi.
rotate(n): Deque elementlarini n qadamga aylantiradi (manfiy qiymat bo'lsa, teskari aylantiradi).
Deque afzalliklari:
Deque ikki tomonlama navbat bo‘lib, tezkor operatsiyalarni ta’minlaydi. Shuning uchun, kengligi
bo‘yicha qidiruv kabi algoritmlarda, navbatga tez-tez qo('shish va olish operatsiyalari talab '
qilinadigan vaziyatlarda, deque ko')pincha ishlatiladi.