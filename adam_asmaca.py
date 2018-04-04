import random

sekiller = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +----+
  |    |
 [O    |
 /|\   |
 / \   |
       |
==========''', '''
  +----+
  |    |
 [O]   |
 /|\   |
 / \   |
       |
==========''']

kelimeler = {"futbol": "beşiktaş fenerbahçe galatasaray barcelona porto".split(),
             "renkler": "siyah mavi kırmızı turuncu sarı yeşil mavi mor".split(),
             "dersler": "matematik fizik kimya biyoloji edebiyat".split(),
             "hayvanlar": "kedi köpek balina güvercin aslan kaplan çita".split()
             }


def rastgele_kelime(kelimeler_sozluk):
    anahtar = random.choice(list(kelimeler_sozluk.keys()))

    no = random.randint(0, len(kelimeler_sozluk[anahtar]) - 1)
    return [kelimeler_sozluk[anahtar][no], anahtar]


def oyun_ici(sekiller, yanlisharfler, dogruharfler):
    print(sekiller[len(yanlisharfler)])
    print()

    print("Kullanilan Harfler = ", end=" ")
    for harf in yanlisharfler:
        print(harf, end=" ")
    print()

    bosluklar = "_" * len(gercek_kelime)

    for i in range(len(gercek_kelime)):
        if gercek_kelime[i] in dogruharfler:
            bosluklar = bosluklar[:i] + gercek_kelime[i] + bosluklar[i + 1:]

    for bosluk in bosluklar:
        print(bosluk, end=" ")
    print()


def harf_iste(tahmin_harfler):
    while True:
        tahmin = input("Bir harf giriniz = ")

        if len(tahmin) != 1:
            print("Lütfen sadece bir harf giriniz")
        elif tahmin in tahmin_harfler:
            print("Bu harfi daha önceden kullanmıştınız. Başka bir harf deneyin")
        elif tahmin not in "abcçdefgğhıijklmnoöprsştuüvyz":
            print("Lütfen sadece harf giriniz")
        else:
            return tahmin


print("-" * 50, "ADAM ASMACA", "-" * 50)

yanlis_harfler = ""
dogru_harfler = ""
gercek_kelime = rastgele_kelime(kelimeler)
gercek_anahtar = gercek_kelime[1]
gercek_kelime = gercek_kelime[0]
# oyunBitti=False
while True:
    oyun_ici(sekiller, yanlis_harfler, dogru_harfler)
    tahmin = harf_iste(yanlis_harfler + dogru_harfler)

    if tahmin in gercek_kelime:
        dogru_harfler += tahmin
        tum_harfleri_bildi = True
        for i in range(len(gercek_kelime)):
            if gercek_kelime[i] not in dogru_harfler:
                tum_harfleri_bildi = False
                break

        if tum_harfleri_bildi == True:
            print("TEBRİKLER KELİME =", gercek_kelime + ".OYUNU KAZANDINIZ")
            break

    else:
        yanlis_harfler += tahmin

        if len(yanlis_harfler) == len(sekiller) - 1:
            oyun_ici(sekiller, yanlis_harfler, dogru_harfler)
            print("OYUNU KAYBETTİNİZ")
            print(str(len(dogru_harfler)) + " harf bildiniz, " + str(len(yanlis_harfler)), end=" ")
            print("harfi bilemediniz. Kelime " + gercek_kelime + " idi")
            break
            # oyunBitti=True
