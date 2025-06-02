

# 19-dars. FUNKSIYA
def yoshni_hisoblash(ism, joriy_yil, yosh=19):
    print(f'{ism}  {joriy_yil - yosh} yilda tug\'ulgan')


yoshni_hisoblash('Muhammadali', 2024)


def darajaga_oshirish(son):
    print(f'{son} ning kvadrati {son ** 2}ga teng!')
    print(f'{son} ning kubi {son ** 3}ga teng!')


darajaga_oshirish(5)


def juft_toq(son):
    if son % 2:
        print(f'{son} toq son!')
    else:
        print(f'{son} juft son!')


juft_toq(4525134235125)


# son1=int(input('1-sonni kiriting:'))
# son2=int(input('2-sonni kiriting:'))
def taqqoslash(son1, son2):
    if son1 > son2:
        print(son1)
        if son1 == son2:
            print('sonlar teng')
    else:
        print(son2)


taqqoslash(3, 4)
x = int(input('x='))
y = int(input('y='))


def darajaga_oshirish(x, y):
    print(x ** y)


darajaga_oshirish(x, 2)
darajaga_oshirish(5, 42)
darajaga_oshirish(354, 46)


def qoldiqsiz_bolish(son):
    for a in range(2, 11):
        if not son % a:
            print(f'{son} {a}ga bolinadi')


qoldiqsiz_bolish(3)
qoldiqsiz_bolish(12158989876)


# 20-DARS. QIYMAT QAYTARUVCHI FUNKSIYA
def malumot_berish(ism, familiya, tyil, tjoy, email, tel):
    malumotnoma = {'ism': ism,
                   'familiya': familiya,
                   'tyil': tyil,
                   'tjoy': tjoy,
                   'email': email,
                   'tel': tel}
    return malumotnoma


insonlar = []
while True:
    ism = input('ism:')
    familiya = input('familya:')
    tyil = int(input('tyil:'))
    tjoy = input('tjoy:')
    email = input('email manzili(malburiy emas!):')
    tel = input('telefon raqamini(malburiy emas!):')
    if tel == '':
        tel = '------'
    if email == '':
        email = '------------'
    insonlar.append(malumot_berish(ism.title(), familiya.title(), tyil, tjoy.title(), email, tel))
    yana = input('yana malumot kiritasizmi?(ha/yo\'q):')
    if yana == 'yo\'q':
        break
print(insonlar)


def kattasini_aniqlash(x, y, z):
    max = x
    if y >= x:
        max = y
    if z >= y:
        max = z
    return max
    print(max)


kattasini_aniqlash(4, 545, 45)

PI = 3.14


def aylana_malumotlari(radius):
    d = 2 * radius
    p = 2 * PI * radius
    s = 4 * PI * radius ** 2
    aylana = {'radiusi': radius,
              'diametr': d,
              'perimetr': p,
              'yuza': s}
    print(aylana)
    return radius


aylana_malumotlari(56544.54)
