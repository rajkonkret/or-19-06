# for - petla iterujaca
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rob

for _ in range(10):
    pass

for i in range(10):
    print(i * 2)

lista2 = list(range(1, 46))  # 1..45
print(lista2)

for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)

for i in range(10):
    if i % 2 == 0:
        print(i, "jest parzysta")

# 0 jest parzysta
# 2 jest parzysta
# 4 jest parzysta
# 6 jest parzysta
# 8 jest parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)
lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8]

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)
# <module 'random' from 'C:\\Users\\CSComarch\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\random.py'>

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']

for p in imiona:
    print(p)

# wyswietlic imiona z tej listaw taki sposób:
# 0 Radek
# 1 Asia

for i in range(len(imiona)):  # range(4) 0..3 indeksy
    print(i, imiona[i])

# enumerate
for p in enumerate(imiona):
    print(p)  # (0, 'Radek')

for p, w in enumerate(imiona):
    print(p, w)  # 0 Radek

for p, w in enumerate(imiona):
    print(p, w, sep=":", end="")  # 3:Marcin
# 0:Radek1:Asia2:Zbyszek3:Marcin
# sep = separator elementó wypisywanych w print po przecinku
# end - znak jaki ma byc na koncu lini, domyslnie \n - new line

ludzie = ['Radek', 'Zenek', 'Asia', 'Marcin', 'Zbyszek', "Franek"]
wiek = [47, 67, 34, 32, 45]
jezyk = ['java', 'python']
print()  # przejscie do nowej lini
# 0 Radek 47
# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])  # 0 Radek 47

# zip
for o, w in zip(ludzie, wiek):
    print(o, w)

for o, w, j in zip(ludzie, wiek, jezyk):
    print(o, w, j)

for i, o in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o)  # 0 ('Radek', 47, 'java')

for i, (o, w, j) in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o, w, j)  # 1 Zenek 67 python

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan')
print(zipped)

for item in zipped:
    print(item)
    # ('Radek', 47, 'java')
    # ('Zenek', 67, 'python')
    # ('Asia', 34, 'Nan')
    # ('Marcin', 32, 'Nan')
    # ('Zbyszek', 45, 'Nan')
    # ('Franek', 'Nan', 'Nan')

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # pętla z ujemnym krokiem, idzie wstecz
    print(i)
