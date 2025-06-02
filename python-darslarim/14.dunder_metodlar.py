# 32-DARS. DUNDER METODLAR

# 1.Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) 
# turli dunder metodlarni qo'shishni mashq qiling.
#     1.Obyekt haqida ma'lumot (__repr__)
#     2.Talabalarni bosqichi bo'yicha solishtirish (__lt__, __eq__ va hokazo)

# 2.Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga 
# yozilgan talabalarning ro'yxati saqlansin. Buning uchun Fanga add_student(), 
# __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.

# 3.Fanga qo'shish + operatori yordamida talaba qo'shish metodini yozing

# 4.Minus (-) operatori yordamida fandan talaba olib tashlash metodini yozing 
# (bunda talabaning passport raqami yoki ID raqami bo'yicha topib, olib tashlash mumkin)

# 5.Fan obyektlarini chaqiriladigan qiling (masalan, fizika(), yoki 
# fizika(talaba1)). Bu metodlarni o'zingiz istagandek talqin qiling.


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

    def __repr__(self):
        return f'{self.ism} {self.familiya} {self.__tyil} yilda tug\'ulgan'

    def __lt__(self, y):
        """Ikki obyektni solishtirish (<)"""
        return self.__tyil < y.__tyil

    def __eq__(self, y):
        """Ikki obyektni solishtirish (==)"""
        return self.__tyil == self.__tyil

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
        return self.__idraqam

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


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar = []

    def add_student(self, *qiymat):
        for talaba in qiymat:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)

    def __getitem__(self, index):
        return self.talabalar[index]

    def __setitem__(self, index, qiymat):
        self.talabalar[index] = qiymat

    def __len__(self):
        return len(self.talabalar)

    def __add__(self, y):
        if isinstance(y, Fan):
            yangi_fan = Fan(f"{self.nomi} {y.nomi}")
            yangi_fan.talabalar = self.talabalar + y.talabalar
            return yangi_fan
        elif isinstance(y, Talaba):
            self.add_student(y)
        else:
            print(f"Fan ga {type(y)} qo`shib bo`lmaydi")

    def __sub__(self, talaba_id):
        for talaba in self.talabalar:
            if talaba.get_id() == talaba_id:
                self.talabalar.remove(talaba)
                break

    def __call__(self, *qiymat):
        if qiymat:
            for talaba in qiymat:
                self.add_student(talaba)
        else:
            return [talaba.get_info() for talaba in self.talabalar]


fan1 = Fan('qwertyu')
fan2 = Fan('oiuytre')

shaxs1 = Shaxs('muhammadali', 'sadulloh', 'AD1234567', 2005)

talaba1 = Talaba('muhammadali', 'sadulloh', 'AD1234567', 2005, 436232675867976543)
talaba3 = Talaba('Alijon', 'Valiyev', 'AD9876543', 2002, 12345)
talaba2 = Talaba('Ali', 'Aliyev', 'AD9876544', 2003, 12346)

talaba4 = Talaba('muh', 'ssw', 'ad3342', 4322, 7735662)
talaba5 = Talaba('dsd555sd', 'ssdsddsdfdsdaafadadd', 'aasd66ds', 4300, 93726576)
talaba6 = Talaba('sksjjss', 'shshs', 'jsiw829', 5533, 552667266)

fan1.add_student(talaba1, talaba2, talaba3)
fan2(talaba4, talaba5, talaba6)

yangifan = fan1 + fan2
