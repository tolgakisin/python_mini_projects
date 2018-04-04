dosya = open("maas1.txt", "w")

maaslar = {
    "tolga": 23000,
    "ali": 22999,
    "mert": 2000,
    "ahmet": 5098,
    "merve": 19232,
    "ebru": 20000,
    "cemre": 20213,
    "mehmet": 20009
}

for key, value in maaslar.items():
    a = key
    b = str(value)
    dosya.write(a)
    dosya.write(" ")
    dosya.write(b)
    dosya.write("\n")

dosya.close()

dosya = open("maas1.txt", "r")
for i in dosya.readlines():
    print(i)

dosya.close()
