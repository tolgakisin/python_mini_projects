import time

zaman = time.localtime()

yil = zaman[0]
ay = zaman[1]
gun = zaman[2]
saat = zaman[3]
dakika = zaman[4]
saniye = zaman[5]
hafta = zaman[6]
yil_gun = zaman[7]


def tarih():
    print("yilin {}. haftasında {}. gunundeyiz".format(hafta, yil_gun))
    print("tarih:{}/{}/{} - saat:{}:{}:{}".format(yil, ay, gun, saat, dakika, saniye))


tarih()
