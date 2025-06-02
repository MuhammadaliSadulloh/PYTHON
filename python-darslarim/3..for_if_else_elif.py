# 9-dars(for takrorlash operatori)
dustlar = ['Behruz', 'Adiz', 'Bekzod', 'Suxrob', 'Shoxjahon']
for a in dustlar:
    print(f"Assalomu aleykum {a}")
print(f'kod {len(dustlar)} marta takrorlandi')
sonlar = list(range(11, 101, 2))
# range harakatni ma'lum bir necha marta takrorlaydi
print(sonlar)
for daraja in sonlar:
    # for takrorlash operatori
    print(f"{daraja} ning kubi {daraja ** 3} ga teng")
print('')
print(' ')
kinolar = []
a = int(input('yoqtirgan kinolaringiz nechta?:'))
for kino in range(a):
    kinolar.append(input(f"yoqtirgan {kino + 1}-kinoyingizni kiriting:"))
print(kinolar)
odamlar = []
a = int(input('bugun nechta odam bilan ko`rishdiz?:'))
for odam in range(a):
    odamlar.append(input(f" {odam + 1}-sining ismi:"))
print(odamlar)

# 10-dars (if-else)
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'bmw']
for a in cars:
    if a == "gm" or a == 'bmw':
        print(a.upper())
    else:
        print(a.title())
a = input('ismingiz nima?:')
if a.lower() == 'behruz':
    print('assalomaleykuum bratimm qandayssiiz')
else:
    print('hormang aka')
b = int(input(f'{a} aka xoxlamagan sonizni kiriting:'))
if b <= 0:
    c = int(input('ex musbat son kiritishingiz kerak edi. Musbat son kiriting akam:'))
    if c <= 0:
        print("укщшйнцдгнцулрва!")
    else:
        print(f'{c}ning ildizi', (c ** (1 / 2)), 'ga teng aka')
else:
    print(f'{b}ning ildizi', (b ** (1 / 2)), 'ga teng aka')

# 11-dars(if-elif-else ketma-ketligi)
a = int(input('juft son kiriting'))
if a % 2 == 0:
    print('rahamat aka!')
else:
    print('bu juft son emas aka! ')
b = int(input('yoshiz nechchida'))
if b <= 4 or b >= 60:
    narx = 'tekin 0'
elif b <= 18:
    narx = 10000
else:
    narx = 20000
print(f"sizga chipta {narx} so'm")
print('ikkita son o`ylang!')
a = int(input('birinchi a sonni kiriting!:'))
b = int(input('ikkinchi b sonni kiriting!:'))
if a == b:
    print("a=b")
elif a > b:
    print("a>b")
else:
    print("a<b")

mahsulot = ['qalam', 'ruchka', 'daftar', 'sir', 'non', 'ketchup', 'olma', 'nok', 'apelsin', 'saqich']
savat = []
for m in range(5):
    savat.append(input('mahsulotlarni kiriting!:'))
print(savat)
for narsa in savat:
    if narsa in mahsulot:
        print(f'bizda {narsa} bor')
    else:
        print(f'kechirasiz bizda {narsa} yo`q')

foydalanuvchilar = ['muhammadali', 'abror', 'sarvar', 'dilshod', 'bekzod']
login = input('yangi login kiriting!:')
if login in foydalanuvchilar:
    print('login band yangi login kiriting!')
else:
    print(f'xush kelibsiz {login}')

b = int(input('biror butun son kiriting!:'))
for a in range(2, 11):
    if not b % a:
        print(f'{b} {a}ga bo`linadi!')
