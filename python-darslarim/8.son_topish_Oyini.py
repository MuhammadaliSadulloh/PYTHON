
# 25-dars.Son topish o'yini
def son_topish(d):
    import random
    inson = 0
    kompyuter = 0
    while True:
        print('son topish o\'yinini o\'ynaymiz avval men son o\'ylayman siz topasiz')
        tahminlar1 = 0
        b_son = random.randint(1, d)
        while True:
            tahminlar1 += 1
            son = int(input(f'1 va {d} orasigagi son kiriting'))

            if son < b_son:
                print('bundan kattaroq')

            elif son > b_son:
                print('bundan kichikroq')

            if son == b_son:
                print('qoyil topdingiz')
                break

        print(f'siz {tahminlar1} urunishda topdingiz')
        print('endi siz son o\'ylang men topaman')
        tahminlar2 = 0
        input(f'agar son o\'ylagan bo\'lsangiz "ENTER" tugmasini bosing')
        pastki_chegara = 1
        yuqori_chegara = d
        while True:
            tahminlar2 += 1
            b_son2 = random.randint(pastki_chegara, yuqori_chegara)
            print(f'siz o\'ylagan son {b_son2} ga teng')
            javob = input('to\'g\'ri bo\'lsa (t),kichik bo\'lsa (+),katta bo\'lsa (-)')
            if javob == '+':
                pastki_chegara = b_son2 + 1

            elif javob == '-':
                yuqori_chegara = b_son2 - 1

            elif javob == 't':
                print(f'men {tahminlar2} urunishda topdim')
                if tahminlar2 < tahminlar1:
                    print(f'Afsuski yutqaazdingiz, men {tahminlar2} marta urunishda topdim va sizni yutdim')
                elif tahminlar2 > tahminlar1:
                    print(f'Tabriklayman siz yutdingiz,siz {tahminlar1} marta urunishda topdingiz va yutdingiz')
                else:
                    print('durrang ikkalamiz bir xil topdik')
                    break
                break
            else:
                print('xatolik yuz berdi tayinlanmagan tugmani bosdingiz')
                break

        if tahminlar1 < tahminlar2:
            inson += 1
        elif tahminlar1 > tahminlar2:
            kompyuter += 1
        print(f'hisob  {inson}:{kompyuter}')
        c = input('O\'ynaymizmi (ha/yo\'q)')
        if c != 'ha':
            print('Men bilan uynaganingiz uchun rahmat')
            break

            return d


son_topish(10)
