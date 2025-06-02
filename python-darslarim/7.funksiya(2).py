
# 21-dars.FUNKSYA VA RO'YXAT
def katta_harf(soz):
    soz = soz[:]
    for a in range(len(soz)):
        soz[a] = soz[a].title()
    return soz


sozlar = ['asda', 'adasd', 'asddasdd', 'asdadsd', 'saddadd']
katta_harf(sozlar)
print(sozlar)
print(katta_harf(sozlar))

talabalar = ['ali', 'vali', 'hasan', 'husan']


def bahola(ismlar):
    baholar = {}
    for a in ismlar:
        baho = input(f"Talaba {a.title()}ning bahosini kiriting: ")
        baholar[a] = baho
    return baholar


talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)


# 22-dars. MOSLASHUVCHAN FUNKSIYA (*args, **kwargs)
def summa(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x * y * sum(sonlar)


print(summa(12, 213, 1232, 23333, 11331))


def talabalar_royxati(ismi, familiyasi, **talabalar):
    talabalar['ismi'] = ismi
    talabalar['familiyasi'] = familiyasi
    return talabalar


talaba1 = talabalar_royxati('Muhammadali', 'Sadulloh', fakulteti='suniy intelekt')
talaba2 = talabalar_royxati('Suxrob', 'Tuyboyev', yoshi=18)
print(talaba1, talaba2)
