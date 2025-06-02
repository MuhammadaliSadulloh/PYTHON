
# 17-dars(while sikli)
kitoblar = []
kitob = ''
while kitob != 'stop':
    kitob = input('yoqtirgan kitoblaringizni kiriting')
    if kitob != 'stop':
        kitoblar.append(kitob.capitalize())
    else:
        print(kitoblar)

print('muzeyga chipta narxi foydalanuvchining yoshiga bog\'liq')
while True:
    b = input('yoshingizni kiriting:')
    if b == '':
        break
    yosh = int(b)
    if yosh < 7:
        a = 2000
    elif 7 <= yosh < 18:
        a = 3000
    elif 18 <= yosh < 65:
        a = 10000
    else:
        a = 0
    print(f'sizga chipta {a}so\'m')

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = float(input(savol))
    if qiymat < 0:
        continue
    elif qiymat == 'Exit':
        break
    else:
        ildiz = float(qiymat) ** (0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")

# 18-DARS. WHILE, RO'YXATLAR VA LUG'ATLAR
buyurtmalar = []
while True:
    buyurtma = input('mahsulot nomini kiriting:')
    buyurtmalar.append(buyurtma)
    if buyurtma == 'exit':
        break
print(buyurtmalar)

mahsulot = {}
while True:
    a = input('mahsulot nomi:')
    b = int(input('mahsulot narxi:'))
    mahsulot[a] = b
    c = input('yana mahsulot kiritasizmi?')
    if c != '':
        break
print(mahsulot)

bozorlik = ['olma', 'anor', 'anjir', 'uzum']
while bozorlik:
    buyurtma = bozorlik.pop()
    if buyurtma in mahsulot.keys():
        b = mahsulot[a]
        print(f'{buyurtma}-{b} so\'m')
    else:
        print(f'bizda {buyurtma} yo\'q')

