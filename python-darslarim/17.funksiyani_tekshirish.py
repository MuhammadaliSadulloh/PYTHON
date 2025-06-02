# 36-DARS. FUNKSIYANI TEKSHIRISH
# !!!!!modul nomi funksiyanitekshirish
# Quyidagi funksiyalarni yarating, va ularning har biri uchun 
# test dasturlarini yozing:

# 1.Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya

# 2.Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir 
# matnning birinchi harfini katta harfga o'zgatiruvchi funksiya

# 3.Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya

# 4.Berilgan son Fibonachchi ketma-ketligida uchraydimi (True) yoki 
# yo'q (False) qaytaruvchi funksiya yozing.


def taqqoslash(a, b, c):
    return max(a, b, c)


d = taqqoslash(2, 4, 2122)

texts = [
    "salom dunyo",
    "python dasturlash",
    "chatGPT bilan tanishing",
    "o'zbekiston tarixi",
    "sun'iy intellekt",
    "dasturlash tillari",
    "internet xavfsizligi",
    "yangi texnologiyalar",
    "fizika va matematika",
    "ilmiy izlanishlar",
    "kompyuter fanlari",
    "maqola yozish",
    "kitoblar va o'qish",
    "musical compositions",
    "world history",
    "creative writing",
    "machine learning",
    "data science",
    "software development",
    "web dizayn",
    "mobile ilovalar",
    "san'at va madaniyat",
    "psixologiya",
    "ta'lim va o'qitish",
    "kino va televideniye",
    "sport va salomatlik",
    "siyosat va iqtisod",
    "tabiat va ekologiya",
    "sahna san'ati",
    "tarixiy asarlar",
    "geografiya",
    "yoshlar va o'smirlar",
    "sayohat va sarguzasht",
    "matematika va statistik",
    "software engineering",
    "digital marketing",
    "entrepreneurship",
    "financial literacy",
    "business management"
]


def katta_harf(t):
    return [c.capitalize() for c in t]


def juft_son(asdfgh):
    return [juftlari for juftlari in asdfgh if juftlari % 2 == 0]


ruyxat = list(range(1, 100))


def fibanachu(a):
    sonlar = [0, 1]
    for i in range(2, 1000):
        keyingi_son = sonlar[-1] + sonlar[-2]
        sonlar.append(keyingi_son)
    return a in sonlar


f = fibanachu(5)
son = juft_son(ruyxat)
harf = katta_harf(texts)

# 2-qism boshqa modulda yoziladi
import unittest


# from funksiyanitekshirish(degan fayl bo'lgan) import *

class tubSonTest(unittest.TestCase):
    def test_taqqoslash(self):
        a = taqqoslash(12, 132, 12344)
        self.assertEqual(a, 12344)

    def test_katta_harf(self):
        self.assertEqual(katta_harf(['qwert', 'qwerty', 'trewq']), ['Qwert', 'Qwerty', 'Trewq'])

    def test_juft_son(self):
        a = juft_son([1, 3, 5, 7])
        b = []
        self.assertEqual(a, b)

    def test_fibanachu(self):
        self.assertTrue(fibanachu(13))


unittest.main()
