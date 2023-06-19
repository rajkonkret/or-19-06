# lista - kolekcja do przechowywania danych
lista = []  # pusta lista
print(type(lista))  # <class 'list'>
print(lista)  # []
lista.append("Radek")
lista.append("Maciek")
lista.append("Dominik")
lista.append("Tadek")
lista.append("Zenek")
print(lista)
# ['Radek', 'Maciek', 'Dominik', 'Tadek', 'Zenek']
# indeksy w liscie sa numerowane od 0
print(lista[0])  # Radek
print(lista[1])
# print(lista[10])  # IndexError: list index out of range
print(lista[-1])  # Zenek  - ostatni element z listy
print(lista[-2])  # Tadek
print(lista[0:3])  # ['Radek', 'Maciek', 'Dominik'] - indeks 3 to czwarty element - nie brany juz wietlany

print(len(lista))  # 5  - dlugosc kolekcji (liczba elementów)
print(lista)  # ['Radek', 'Maciek', 'Dominik', 'Tadek', 'Zenek']

# nadpisanie elementu na danym indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Tadek', 'Zenek']

# wstawianie do listy na indeksie (rozszerzenie listy)
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Tadek', 'Zenek']

# wstawienie na pierwszej pozycji, czyli na indeksie 0
lista.insert(0, "Tomek")  # ['Tomek', 'Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Tadek', 'Zenek']
print(lista)

# usunięcie elementu z listy
lista.remove("Maciek")
print(lista)  # ['Tomek', 'Radek', 'Marcin', 'Mikołaj', 'Tadek', 'Zenek']

indeks = lista.index('Tadek')  # 4
print(indeks)

# to jest tylko kopia adresu gdzie znajduje sie lista - referencja
lc2 = lista
print(lc2)

# prawidłowe kopiowanie elementów listy do drugiej
lc3 = lista.copy()

# usunięcie wszystkich elementów z listy
lista.clear()
print(lista)  # []
print(lc2)  # []
print(lc3)  # ['Tomek', 'Radek', 'Marcin', 'Mikołaj', 'Tadek', 'Zenek']
a = 3
b = a
print(b)
a = 7
print(b)
# 14:00

print("Radek" in lc3)  # True

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)
print(type(liczby))  # <class 'list'>

liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola']
lista_osoby.sort()
print(lista_osoby)  # ['ola', 'radek']

liczby.reverse()
print(liczby)  # [999, 687, 54, 34, 22, 12.34]

# nadpisanie po indeksie
liczby[3] = 6666
print(liczby)

print(liczby[0:3])  # [999, 687, 54]
print(liczby[-2])
print(liczby[0:-2])  # [999, 687, 54, 6666]

indeks = liczby.index(6666)
print(liczby.pop(indeks))  # 6666 - usuniecie po indeksie i zwrocenie nam tego elementu
print(liczby)

# usuniecie po elemencie
print(liczby.remove(54))  # zwraca None
print(liczby)

print(len(liczby))  # długosc kolekcji liczby wynosi 4

krotka = tuple(liczby)
print(krotka)  # (999, 687, 22, 12.34)
print(type(krotka))  # <class 'tuple'>
