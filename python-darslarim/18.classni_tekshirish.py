# # 37-DARS. KLASSNI TEKSHIRISH
# !!!!modul nomi classnitekshirish

# 1.30-darsimizda Shaxs va Talaba klasslarini yaratgan edik. 
# Shu ikki klassning xususiyatlari va metodlarini tekshiruvchi 
# test dasturlar yozing.

# 2.Ikki klass uchun yagona test yoza olasizmi? (isInstance() funksiyasini eslang)


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

        x = 5
        y = 7

        print(x)
        print(y)

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Fan:
    def __init__(self, nomi, muddati):
        self.nomi = nomi
        self.muddati = muddati

    def get_fan(self):
        return f"{self.nomi} ({self.muddati} )"


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []

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

    def fanga_yozil(self, fan):
        if fan not in self.nomi:
            self.fanlar.append(fan)
            print(f'{self.fan} muvaffaqiyatli qo\'shildi')
        else:
            print('fan allaqachon mavjud')

    def remove_fan(self, fan):
        if fan not in self.fanlar:
            self.fanlar.remove(fan)
            print(f'{self.fan} muvaffaqiyatli o\'chirildi')
        else:
            print('siz bu fanga yzilmagansiz')


class Professor(Shaxs):
    def __init__(self, ism, familiya, tyil, institut):
        super().__init__(ism, familiya, None, tyil)
        self.institut = institut

    def get_info(self):
        return f'{self.ism} {self.familiya} {self.institut} ning professori'


class Foydalanuvchi(Shaxs):
    def __init__(self, ism, familiya, tyil, foydalanuvchi_id, email_adres):
        super().__init__(ism, familiya, None, tyil)
        self.email = email_adres
        self.foydalanuvchi_id = foydalanuvchi_id

    def get_info(self):
        info = f'foydalanuvchi {self.ism} {self.familiya}'
        info += f' tug\'ulgan yili {self.tyil} email adresi {self.email} \nfoydalanuvchinng id raqami:{self.foydalanuvchi_id}'
        return info


class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, dukon_raqami):
        super().__init__(ism, familiya, None, None)
        self.dukon_raqami = dukon_raqami

    def get_info(self):
        return f'{self.ism} {self.familiya}  {self.dukon_raqami}-do\'kon egasi'


class Mijoz(Shaxs):
    def __init__(self, ism, passport, mijoz_id, tel):
        super().__init__(ism, None, passport, None)
        self.mijoz_id = mijoz_id
        self.tel = tel

    def get_info(self):
        return f'Mijozning ismi {self.ism} \npasport raqami:{self.passport} \nid raqami:{self.mijoz_id} \ntelefon raqami:{self.tel}'


class Admin(Foydalanuvchi):
    def __init__(self, ism, familiya, passport, tyil, foydalanuvchi_id, email_adres):
        super().__init__(ism, familiya, tyil, foydalanuvchi_id, email_adres)
        self.passport = passport

    def ban_user(self):
        print('foydalanuvchi bloklandi')


talaba1 = Talaba('Muhammadali', 'Sa\'dulloh', 'Ad1234567', 2005, 1234567890)
fan1 = Fan('algebra', '6oy')
professor1 = Professor('alijon', 'Valiyev', 1111, 'Texnika')
sotuvchi1 = Sotuvchi('akram', 'qassob', 101)
mijoz1 = Mijoz('hasan', 'AS098765', 78901234567, +9989995671234)
admin1 = Admin('asdfg', 'qwetrtygf', 'AD24537497734', 2000, 341547005879404567997545, 'assalom124556@gmail.com')
foydalanuvchi1 = Foydalanuvchi('qahramon', 'turayev', 1943, 33455667894335300, 'qaxr25422@gmail.com')
shaxs1 = Shaxs('Suxrob', 'To\'yboyev', 'AD5637156', 2005)

# print(shaxs1.get_info())
# print(talaba1.get_info())
# print(professor1.get_info())
# print(sotuvchi1.get_info())
# print(mijoz1.get_info())
# print(admin1.ban_user())
# print(foydalanuvchi1.get_info())
# print(fan1.get_fan())


# 2-qism boshqa moduldan yoziladi

import unittest


# from classnitekshirish(degan fayl bolgan) import Shaxs,Talaba


class TestShaxsTalaba(unittest.TestCase):
    def setUp(self):
        ism = 'Muhammadali'
        familiya = 'sa\'dulloh'
        passport = 'AD1234567'
        self.yunalish = 's'
        tyil = 2005
        idraqam = 987654321
        self.shaxs1 = Shaxs(ism, familiya, passport, tyil)
        self.talaba2 = Talaba(ism, familiya, passport, tyil, idraqam)

    def test_get__info(self):
        self.assertEqual(self.shaxs1.get_info(), 'Muhammadali sa\'dulloh. Passport:AD1234567, 2005-yilda tug`ilgan')
        self.assertEqual(self.talaba2.get_info(), 'Muhammadali sa\'dulloh. 1-bosqich. ID raqami: 987654321')

    def test_is_instance(self):
        self.assertIsInstance(self.shaxs1, Shaxs)
        self.assertIsInstance(self.talaba2, Talaba)


unittest.main()
