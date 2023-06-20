# funkcje
a = 4
b = 8


# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)


def dodaj2(a, b):  # funkcja z argumentami
    print(a + b)


def odejmij(a, b, c=0):  # z argumentem domyslnym
    print(a - b - c)


# użycie funkcji
dodaj()  # 12
dodaj2(6, 7)  # 13
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
odejmij(6, 7, 8)
odejmij(7, 8)
odejmij(c=8, a=9, b=4)  # argumenty po nazwie
print(dodaj())  # None
# print(dodaj() + dodaj2(5, 6))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
