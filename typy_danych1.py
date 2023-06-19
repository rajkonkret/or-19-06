wiek = 47
rok = 2023
temp = 36.6
wiek2 = 37.5

print(wiek2)
print(type(wiek2))  # <class 'float'>

print(5 * "Radek")  # RadekRadekRadekRadekRadek

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # 0.023232822540781017 - wynik float
print(wiek // rok)  # częśc całkowita z dzielenia, tutaj 0 - wynik int
print(wiek % rok)  # reszta z dzielenia, tutaj 47 (modulo)
print(wiek ** rok)  # potęgowanie

print(5 % 2)  # 1 bo 5 / 2 = 2 r 1, 2 * 2 + 1 = 5
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0 - float
print(0.2 + 0.7)  # 0.8999999999999999
# liczby float sa zapamietywane w komputerza jak mantysta i wykładnik
#  mantysta, wykładnik maja swoja dokładnosc
# przy operacjach na float wystepuje bład zaokrąglenia
wynik = 0.2 + 0.7
print(f"{wynik:.1f}")  # 0.9, zaokragliło tylko do wyswietlenia

print(f"Sprawdzanie zmiennej temp {wiek} {temp}")  # Sprawdzanie zmiennej temp 47 36.6
print(f"""
    {wiek}
    {temp}
""")

print(type(4 / 2))  # <class 'float'>
print(type(4 // 2))  # <class 'int'>

# typ logiczny
# True, False - prawda, fałsz
czy_znasz_Python = True
print(czy_znasz_Python)  # True
print(type(czy_znasz_Python))  # <class 'bool'>
print(int(czy_znasz_Python))  # rzutowanie bool na int 1 - True
czy_znasz_Python = False
print(int(czy_znasz_Python))  # False - 0

x = 1
print(bool(x))  # rzutowanie inta na bool - True
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = 0
print(bool(x))  # False

x = "radek"
print(bool(x))  # True
x = ''
print(bool(x))  # False
# wszystko rózne od 0, None i od pustego ciągu znaków bedzie True
x = None
print(bool(x))  # False

a = 14
b = 3
print(f"Wynik porównania {a} > {b}", a > b)
print(f"Wynik porównania {a} < {b}", a < b)
print(f"Wynik porównania {a} == {b}", a == b)  # == porównanie czy równe
print(f"Wynik porównania {a} != {b}", a != b)  # != czy różne
# Wynik porównania 14 > 3 True
# Wynik porównania 14 < 3 False
# Wynik porównania 14 == 3 False
# Wynik porównania 14 != 3 True
