# GİRİLEN SAYIYA KADAR OLAN ASAL SAYILARI YAZDIRAN PROGRAM

def asal(sayi):
    asal_list = []
    for i in range(2, sayi):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
                break
        if flag == False:
            asal_list.append(i)
    for a in asal_list:
        print(a)


sayi = int(input("Sayi giriniz = "))
asal(sayi)
