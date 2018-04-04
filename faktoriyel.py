def fakt(sayi):
    if sayi == 0: return 1
    return sayi * fakt(sayi - 1)


print("CIKIS YAPMAK ICIN ""-1"" yazınız")
while True:
    sayi = int(input("Faktoriyelini almak istediğiniz sayiyi giriniz = "))
    if sayi < -1:
        print("Lutfen faktoriyelini almak istediginiz sayi icin 0'dan buyuk bir deger giriniz!")
        continue
    if sayi == -1: break
    print(fakt(sayi))
