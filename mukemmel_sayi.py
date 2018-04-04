# Mükemmel sayı, kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayıdır.

sayi = int(input("Bir sayi giriniz = "))
toplam = 0

for i in range(1, sayi):
    if sayi % i == 0:
        toplam = toplam + i

print("Toplam = ", toplam)

if toplam == sayi:
    print(sayi, "sayisi Mükemmel Sayidir")
else:
    print("Mükemmel Sayi degildir")
