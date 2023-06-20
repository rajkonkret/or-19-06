# funkcje zwracające wynik

def dodaj(a, b):
    return a + b  # return - zwraca wynik


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))
print(dodaj(6, 9) + dodaj(4, 3))  # 22
print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 7))  # 1070.0

zm = oblicz_vat(1000)  # 1230.0
print(zm)

if zm == 1230:
    print("Prawidłowowo")
# 15:00
