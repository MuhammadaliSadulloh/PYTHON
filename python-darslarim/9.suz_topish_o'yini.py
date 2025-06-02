
# 26-dars.so'z topish o'yini
from algoritm_darslar.uzwords_a import words_a
import random


def get_word(word):
    return random.choice(word)


b = get_word(words_a)
print(b)


def uzunlik(c):
    uzunligi = ['-' for e in c]
    return uzunligi


print(uzunlik(b))


def display(soz, uzunlii, harf):
    for a in range(len(soz)):
        if soz[a] in harf:
            uzunligi[a] = soz[a]
    return ''.join(uzunligi)


uzunligi = uzunlik(b)
print(''.join(uzunligi))

while True:
    if '-' in uzunligi:
        harf = input('Harf kiriting: ')
        s = display(b, uzunligi, harf.lower())
        print(s)
        if '-' not in s:
            print("Siz so'zni topdingiz!")
            break
    else:
        break
