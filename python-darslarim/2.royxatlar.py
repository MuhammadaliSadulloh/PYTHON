# 7-dars(ro'yxatlar)  (umumiy)
cars = ['bmw E39 M5', 'malibu', 'captiva', 'nexia', 'gentra', 'cobalt']
cars.append('audi')
# append bu lug`atning oxiriga o`zgaruvchi qo`shadi
cars[-4] = 'bmw F90 M5'
print(cars)
cars.insert(2, 'mersedez benz')
cars.insert(5, 'ferrari')
# insert bu kiritilgan index o`rnida yangi o`zgaruvchi qo`shadi
print(cars)
print(cars[6].title())
# title o`zgaruvchining bosh harfini katta harflar bilan yozib beradi
cars.remove('mersedez benz')
# remove bu aytilgan o`zgaruvchini lug`atdan chiqarib tashlaydi
print(cars[7].title())
cars[1] = 'bmw e30 M5'
# sort bu o`zgaruvchilarni alifbo tartibida tartiblayi
cars.sort()
print(cars)

# 8-dars(ro'yxatlar bilan ishlash)
davlatlar = ['uzb', 'aqsh', 'vetnam', 'yaponiya', 'koreya', 'germaniya']
print(davlatlar)
print('davlatlar soni:', len(davlatlar))
# len>>>elementlar sonini
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
# reverse ro'yxat elemntlarini teskari tartiblaydi
print(davlatlar)
sonlar = [10, 15, 76, 9843, 27, 13, 766, 3, 422, 86359, 299, 37, 32920, 5, 9, 7, 3, 2, 1]
print(sonlar)
sonlar.sort()
print(sonlar)
print(sorted(sonlar, reverse=True))
print('120<1200gacha juft sonlar', list(range(120, 1201, 2)))
print('sonlar yig`indisi:', sum(sonlar))
print('eng kattasidan eng kichigini ayirmasi:', (max(sonlar) - min(sonlar)))
print('ro`yxat elementlar soni:', len(sonlar))
print(sonlar[0:5])
taomlar = ['osh', 'sho`rvo', 'kavob', 'tuxum', 'sut']
nonushta = taomlar[3:5]
nonushta.append('shirinliklar')
nonushta.append('choy')
print('taomlar:', taomlar)
print('nonushtaga:', nonushta)
nonushta[0] = 'qaymoq va non'
nonushta = tuple(nonushta)
# tuple ro'yxatni o'zgarmas royxatga aylantiradi
print(nonushta)
