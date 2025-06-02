# 31-DARS. INKAPSULYATSIA, KLASSNING XUSUSIYAT VA METODLARI

# 1.Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq
# xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi va o'zgarti-
# ruvchi metodlar yozing.

# 2.Yuqoridagi klasslarga talabalar_soni va odamlar_soni degan klassga 
# oid xususiyatlar qo'shing.

# 3.Klassga oid xususiyatlar bilan ishlash uchun maxsus @classmethod lar yozing

class Shaxs:
    __odamlar_soni = 0

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.__tyil = tyil
        Shaxs.__odamlar_soni += 1

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.__tyil}-yilda tug`ilgan"
        return info

    def get_age(self):
        """Shaxsning tug'ulgan yilini qaytaruvchi metod"""
        return self.__tyil

    @classmethod
    def get_odamlar_soni(cls):
        return cls.__odamlar_soni


class Talaba(Shaxs):
    __talabalar_soni = 0

    def __init__(self, ism, familiya, passport, tyil, idraqam):
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = idraqam
        self.bosqich = 1
        Talaba.__talabalar_soni += 1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

    @classmethod
    def get_talabalar_soni(cls):
        return cls.__talabalar_soni


shaxs1 = Shaxs('muhammadali', 'sadulloh', 'AD1234567', 2005)
talaba1 = Talaba('muhammadali', 'sadulloh', 'AD1234567', 2005, 436232675867976543)

from uuid import uuid4


class Avto:
    num_avto = 0
    """Avtomobil klassi"""

    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.num_avto += 1

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")


avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000, 100000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", 'Carolla', "Silver", 2018, 45000)
print(Avto.num_avto)
print(avto1.num_avto)
avto1.add_km(1500)
print(f"ID: {avto1.get_id()}")
print(avto1.get_km())
