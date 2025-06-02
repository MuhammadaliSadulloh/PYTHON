
# 28-dars.Klass va obyekt
# 1-qism
class foydalanuvchi:
    def __init__(self, nom, ism, email):
        self.a = nom
        self.b = ism
        self.c = email

    # 2-3-qism
    def nomi(self):
        return self.a

    def email(self):
        return f'Email manzili:{self.c}'

    def get_info(self):
        print(f"Foydalanuvchi:{self.a}, ismi: {self.b}, email:{self.c}")


abdullo = foydalanuvchi('qwer1234', 'abdullo', '@abdullo2005')
abdullo.get_info()
print(abdullo.nomi())
print(abdullo.email())


# 29-DARS. OBYKETLAR BILAN ISHLASH

# 1.Avto degan yangi klass yarating. Unga avtomobillarga 
# doir bo'lgan bir nechta xususiyatlar (model, rang, 
# korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga 
# standart qiymat bering (masalan, kilometer=0)
# 
# 2.Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avto haqida to'liq ma'lumotni 
# matn ko'rinishida qaytarsin
# 
# 3.Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning +
# yurgan kilometrajini yangilab borsin
# 
# 4.Yangi, Avtosalon degan klass yarating va kerakli 
# xususiyatlar bilan to'ldiring (salon nomi, manzili, 
# sotuvdagi avtomobillar va hokazo)
# 
# 5.Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
# 
# 6.Avtosalondagi avtomobillar haqida ma'lumot 
# qaytaruvchi metod yozing
# 
# 7.Yuqoridagi obyektlar va ularga tegishli metodlarni 
# tekshirib ko'ring
# 
# 1-2-3qism
class Avto:
    def __init__(self, rusumi, korobka, narxi, rangi, yili):
        self.nomi = rusumi
        self.rangi = rangi
        self.yili = yili
        self.narxi = narxi
        self.korobka = korobka
        self.kilometr = 0

    def set_kilometr(self, kilometr_yurgan):
        self.kilometr = kilometr_yurgan

    def update_km(self, kilometr_yur):
        self.kilometr += kilometr_yur

    def get_info(self):
        return f'avtomobil rusumi: {self.nomi}, \nrangi: {self.rangi} ,\nishlab chiqarilgan yili: {self.yili}, \nkarobkasi: {self.korobka} \nnarxi={self.narxi}, \nyurgan yo\'li={self.kilometr}'


cobalt = Avto('cobalt', 'avtomat', 15000, 'Oq', 2023)
a = int(input('avttomobilning bugun yurgan masofasi: '))
cobalt.update_km(a)
print(cobalt.get_info())


# 4-5-6-qism
class Avtosalon:
    def __init__(self, salon_nomi, salon_manzili):
        self.nom = salon_nomi
        self.manzil = salon_manzili
        self.mashinalar_ruyxati = []

    def add_car(self, mashina):
        self.mashinalar_ruyxati.append(mashina)

    def get_car(self):
        return [mashina.get_info() for mashina in self.mashinalar_ruyxati]


gm = Avtosalon('General Motors', 'O\'zbekison')
lassetti = Avto('Lasseti', 'mexanika', 9800, 'Kulrang', 2010)
nexia2 = Avto('Nexia', 'mexanika', 7800, 'Oq', 2007)
gm.add_car(cobalt)
gm.add_car(lassetti)
gm.add_car(nexia2)

print(gm.mashinalar_ruyxati)
gm_mashinalar = gm.get_car()
print(gm_mashinalar)

print(dir(Avto))
print('salom')
print(dir(str))
print('qwertyuiopasfghjk')
print(lassetti.__dict__)


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]


print(see_methods(Avtosalon))
print(see_methods(Avto))
