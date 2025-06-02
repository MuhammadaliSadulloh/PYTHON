
# 33-DARS. FAYLLAR BILAN ISHLASH

# 1.Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching

# 2.Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π soni nuqtadan 
# so'ng million xona aniqlik bilan yozilgan).

# 3.Sizning tug'ilgan kuningiz π soni tarkibida uchraydimi yoki yo'q 
# ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz 
# 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda 
# uchraydimi yo'q toping.

# 4.Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle 
# yordamida yangi faylga saqlang.

# 5.Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan 
# ma'lumotni yangi qatordan faylga yozib boruvchi dastur tuzing. 
# Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan qo'shilib 
# borsin (yangi faylga emas).


with open('pi.txt') as file:
    pi = file.read()

pi = pi.rstrip()
pi = pi.replace('\n', '')
pi = pi.replace(' ', '')

bdate = '01122005'

print(bdate in pi)

import pickle

with open('pi_float.dat', 'wb') as file:
    pickle.dump(pi, file)

with open('pi_float.dat', 'rb') as file:
    a = pickle.load(file)

print(a)

while True:
    dustlar = input('yaxshi ko\'rgan insonlaringizni kiriting,\nagar qolmagan bo\'lsa (enter) tugmasini bosing')
    with open('malumotlar.py', 'a') as fayl:
        a = fayl.write(dustlar + '\n')
    if not dustlar:
        break

with open('malumotlar.py', 'rb') as fayl:
    a = fayl.read()

# # 34-DARS. JSON

# # 1.Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini
# # konsolga chiqaring: data = {"Model" : "Malibu", "Rang" : 
# # "Qora", "Yil":2020, "Narh":40000}

# # 2.Ushbu JSON matnni ko'chirib oling, va talabaning ismi va 
# # familiyasini konsolga chiqaring: talaba_json = """{"ism":"Hasan",
# # "familiya":"Husanov","tyil":2000}"""

# # 3.Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.

# # 4.Ushbu JSON faylni yuklab oling. Faylda 3 ta talabaning ism va 
# # familiyasi saqlangan. Ularning har birini alohida qatordan 
# # "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida konsolga chiqaring.

# # 5.Quyidagi bog'lamaga kirsangiz, Wikipediadagi Python dasturlash 
# # tili haqidagi maqolani JSON ko'rinishida ko'rishingiz mumkin. 
# # Brauzerda chiqqan ma'lumotni JSON ko'rinishida saqlang (brauzerda 
# # Ctrl+S tugmasini bosib). Faylni Pythonda oching va konsolga maqolaning 
# # sarlavhasi (title) va qisqa matnini (extract) chiqaring: 
# # https://uz.wikipedia.org/w/api.php?format=json&action=
# # query&prop=extracts&exintro&explaintext&redirects=1&titles=Python


import json

data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
data_json = json.dumps(data)

print(data_json)

talaba = {"ism": "Hasan", "familiya": "Husanov", "kurs": '1-kurs'}
talaba_json = json.dumps(talaba)

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    a = f.read()

talabalar = {"student": [{"id": "01", "name": "Tom", "lastname": "Price", "year": 4, "faculty": "Engineering"},
                         {"id": "02", "name": "Nick", "lastname": "Thameson", "year": 3, "faculty": "Computer Science"},
                         {"id": "03", "name": "John", "lastname": "Doe", "year": 2, "faculty": "ICT"}]}

with open('student.json', 'w') as f:
    json.dump(talabalar, f)

with open("student.json") as f:
    data = json.load(f)

for item in data["student"]:
    print(f"{item['name']} {item['lastname']}." f" Faculty of {item['faculty']} ")

with open('api_result.json') as f:
    a = json.load(f)

print(a['query']['pages']['13801']['title'])
print('\n\n\n')
print(a['query']['pages']['13801']['extract'])
