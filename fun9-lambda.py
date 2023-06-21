# lambda - skrocony zapis funkcji
odejmij = lambda a, b: a - b  # lambda zwraca wartość

print(odejmij(9, 8))

# def odejmij(a, b):
#     return a - b


oblicz_vat = lambda cena, vat=7: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")

print(wiek(9))
print(wiek(11))
print(wiek(18))

# dziecko
# nastolatek
# dorosły

lista = [1, 2, 3, 8, 10, 23, 50]
print(lista)

l = []
for i in lista:
    l.append(i * 2)

print(l)
print([i * 2 for i in lista])

# map() - mapowanie kolekcji
print(f"Zastosowanie map:  {list(map(lambda x: x * 2, lista))}")  # Zastosowanie map:  [2, 4, 6, 16, 20, 46, 100]

# filter() - filtruje dane i zwraca spełniajace warunek
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter: [1, 2]
print(f"Zastosowanie filter: {list(filter(lambda x: x < 8, lista))}")
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")  # Zastosowanie filter: [8, 10]
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3 or x > 20, lista))}")  # Zastosowanie filter: [1, 2, 23, 50]
print(True and True)  # True
print(not False)  # True
# x > 3 and x < 20 -> 3 < x < 20
