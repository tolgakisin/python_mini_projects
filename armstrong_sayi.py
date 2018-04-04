sayi = int(input("Bir sayi giriniz = "))
numberstr = str(sayi)
toplam = 0

for i in numberstr:
    a = int(i) ** len(numberstr)
    toplam += a
print("toplam = ", toplam)

if toplam == sayi:
    print(sayi, "sayisi bir armstrong sayidir")
else:
    print("armstrong değildir")
