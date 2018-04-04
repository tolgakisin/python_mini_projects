"""

GEOMETRİK ŞEKİLLERİN HESAPLANMASI

"""

pi = 3.14


def kare(kenar):
    return print(kenar * kenar)


def dikdortgen(kisa_k, uzun_k):
    return print((kisa_k * uzun_k))


def yamuk(alt_t, ust_t, y):
    return print(((alt_t + ust_t) * y) / 2)


def paralel_kenar(alt_t, y):
    return print(alt_t * y)


def cember(r):
    return print(pi * (r ** 2))


if __name__ == "__main__":

    print("""
        1-Kare
        2-Dikdortgen
        3-Yamuk
        4-Paralel Kenar
        5-Çember
    """)

    secim = int(input("Alanini bulmak istediginiz geometrik şekil = "))

    if secim == 1:
        print("Kare icin : ")
        kenar = float(input("Kenar uzunlugunu giriniz = "))
        kare(kenar)

    elif secim == 2:
        print("Dikdortgen icin : ")
        kisa_k = float(input("Kisa kenar uzunlugunu giriniz = "))
        uzun_k = float(input("Uzun kenar uzunlugunu giriniz = "))
        dikdortgen(kisa_k, uzun_k)

    elif secim == 3:
        print("Yamuk icin: ")
        alt_t = float(input("Alt taban uzunlugunu giriniz = "))
        ust_t = float(input("Ust taban uzunlugunu giriniz = "))
        y = float(input("Yuksekligi giriniz = "))
        yamuk(alt_t, ust_t, y)

    elif secim == 4:
        print("Paralel Kenar icin : ")
        alt_t = float(input("Alt taban uzunlugunu giriniz = "))
        y = float(input("Yuksekligi giriniz = "))
        paralel_kenar(alt_t, y)

    elif secim == 5:
        print("Cember icin : ")
        r = float(input("Yaricap uzunlugunu giriniz = "))
        cember(r)

    else:
        print("Lutfen belirtilen degerlerin disinda bir deger girmeyiniz!")
