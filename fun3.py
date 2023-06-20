a = 10
b = 10


def dodaj():
    a = 6
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a
    a = 6
    b = 7
    print(a + b)


print("Zmienna a z góry", a)
dodaj()
print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj2()
print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj3()
print("Zmienna a z góry", a)  # Zmienna a z góry 6
dodaj2()  # 16
