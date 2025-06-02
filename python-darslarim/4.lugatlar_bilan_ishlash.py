# 14-dars(luf'at bilan tanishuv)
dadam = {'ismi': 'isomiddin', 'shahri': 'navoiy', 'manzili': 'hazora', 't_yil': 1979}
print(f"Otamning ismi {dadam['ismi'].title()} , {dadam['t_yil']}-yilda {dadam['shahri'].title()} viloyatida tug`ilgan")
taomlar = {'ali': 'osh',
           'vali': 'sho`rva',
           'muhammadali': 'manti',
           'aziz': 'xonim',
           'behruz': 'baliq'}
taom1 = taomlar['ali']
taom2 = taomlar['muhammadali']
taom3 = taomlar['behruz']
print(f'Alining sevimli taomi {taom1}')
print(f'Muhammadalining sevimli taomi {taom2}')
print(f'Behruznung sevimli taomi {taom3}')
python_lugat = {'integer': 'butun son',
                'float': 'o`nli kasr son',
                'string': 'matn',
                'list': 'ro`yxat',
                'tuple': 'o`zgarmas ro`yxat'}
kalit = input('kalit so`zni kriting:').lower()
tarjima = python_lugat.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
l = input('So`zni kiriting!:').lower()
k = {'apple': 'olma',
     'pen': 'ruchka',
     'pensil': 'qalam',
     'hello': 'salom',
     'good': 'yaxshi',
     'key': 'kalit'}
tarjima = k.get(l)
# get model elementining qiymatini olish
if tarjima == None:
    print('Bunday so`z mavjud emas!')
else:
    print(f'{l.title()} so`zining ma`nosi {tarjima}')

# 15 LUG'AT ELEMENTLARI BILAN ISHLASH
python_lugat = {'integer': 'butun son',
                'float': 'o`nli kasr son',
                'string': 'matn',
                'list': 'ro`yxat',
                'append': 'qo`shish',
                'tuple': 'o`zgarmas ro`yxat',
                'input': 'kiritish'}
for keys, value in sorted(python_lugat.items()):
    print(f'{keys}-{value}')

davlatlar = {
    "o'zbekiston": 'toshkent',
    'aqsh': 'washington d.c.',
    'rossiya': 'moskva',
    'tojikiston': 'dushanbe',
    "qirg'iziston": 'bishkek',
    'qozog\'iston': 'nursulton',
    'malayziya': 'kuala-lumpur',
    'singapur': 'sungapur',
    'italiya': 'rim'}
for a, b in sorted(davlatlar.items()):
    print(a)
    print(b)
a = input('davlat nomi:')
davlat = davlatlar.get(a)
if davlat == None:
    print('bizda bu davlat haqida ma\'lumot yo\'q')
else:
    print(f'{a.lower()}ning poyaxti {b}')

restoran = {'osh': 20000,
            'shashlik': 17000,
            'sho`rva': 30000,
            'asarti': 150000,
            'jiz': 50000,
            'choy': 10000,
            'koffee': 10000,
            'tandir': 120000,
            'tovuq': 50000,
            'non': 5000}
print('3ta taom buyurtma bering')
taom_nom = ()
taom = restoran.get(taom_nom)
buyurtmalar = []  # buyurtmalar ro'yxatini yaratish
for i in range(3):
    buyurtma = input(f"{i + 1}-taom buyurtma: ")
    buyurtmalar.append(buyurtma)
for buyurtma in buyurtmalar:
    taom = restoran.get(buyurtma)
    if taom == None:
        print(f"Bizda {buyurtma} yo'q.")
    else:
        print(f"{buyurtma.capitalize()}: {taom} so'm")

# 16- dars
steve = {'ism': 'Steve Jobs',
         't_yil': 1955,
         'v_yil': 2011,
         't_joy': 'Amerika',
         'yozgan_kitobi': ['kitob yozmagan', 'kitob yozmagan', ]}

gitler = {'ism': 'Adolf Hitler',
          't_yil': 1889,
          'v_yil': 1945,
          't_joy': 'Avstriya',
          'yozgan_kitobi': ['kitob yozmagan', 'kitob yozmagan']}

karimov = {'ism': 'Islom Karimov',
           't_yil': 1938,
           'v_yil': 2016,
           't_joy': 'O\'zbekiston',
           'yozgan_kitobi': 'yuksak ma\'naviyat yengmas kuch'}
insonlar = [steve, gitler, karimov]
for inson in insonlar:
    ism = inson['ism']
    tyil = inson['t_yil']
    vyil = inson['v_yil']
    tjoy = inson['t_joy']
    kitobi = inson['yozgan_kitobi']
    print(f'{ism} {tyil}-yilda {tjoy}da tug\'ilgan')
    print(f'{ism} {kitobi} nomli kitob yozgan')
    print(f'{ism} {vyil}da vafot etgan')
print('Bular mashxur insonlar hisoblanishadi')

kinolar = {'suhrob': ['Tenet', 'Inception', 'Interstellar'],
           'adiz': ['shaytanat', 'abdullajon', 'mahallada duv-duv gap'],
           'bekzod': ['godzilla', 'king kong', 'qasoskorlar']}
for ism, kinolar in kinolar.items():
    print(f'{ism}ning sevimli filmlari {kinolar}')
    for kino in kinolar:
        print(kino)

davlatlar = {'o\'zbekiston': {'aholisi': 3700000,
                              'maydoni': 447400,
                              'puli': 'soʻm',
                              'din': 'islom'},
             'amerika': {'aholisi': 331449284,
                         'maydoni': 9830000,
                         'puli': 'USD',
                         'din': 'xristianlik'}}

for davlat, malumot in davlatlar.items():
    aholisi = malumot['aholisi']
    maydoni = malumot['maydoni']
    puli = malumot['puli']
    din = malumot['din']
    print(f'\n{davlat.capitalize()}ning'
          f'\naholisi {aholisi} kishi'
          f'\nmaydoni {maydoni} kv.km'
          f'\npul birligi {puli}'
          f'\nasosiy tarqalgan dini {din} dini')
