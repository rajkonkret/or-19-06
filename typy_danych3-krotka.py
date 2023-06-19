# krotka - niemutowalna, niemodyfikowalna
tupla = ("Radek",)  # tupla jednoelementowa, nawiasy nieobowiązkowe
print(type(tupla))  # <class 'tuple'>

tupla2 = ("Tomek", "Asia", "Zbyszek", "Marcin")
print(tupla2)
print(type(tupla2))  # <class 'tuple'>

tupla3 = (43, 55, 22.34, 11, 200)
print(tupla3)
print(type(tupla3))  # <class 'tuple'>

print(tupla2.count("Tomek"))
print(tupla2.index("Asia"))

a, b = 1, 2
print(a)
print(b)

a, b = b, a
print(a, b)

tp = 1, 2, 3
print(tp)
print(type(tp))  # <class 'tuple'>

a, *b = tp
print(a, b)  # 1 [2, 3]

# rozpakowanie tupli
imie1, *imie2, imie3 = tupla2  # ('Tomek', 'Asia', 'Zbyszek', 'Marcin')
print(imie1)
print(imie2)
print(imie3)
# Tomek
# ['Asia', 'Zbyszek']
# Marcin

tupla4 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a, *b, c = tupla4
print(b)  # [2, 3, 4, 5, 6, 7, 8]
a, b, *c = tupla4
print(c)  # [3, 4, 5, 6, 7, 8, 9]

lista = list(tupla2)
print(lista)  # ['Tomek', 'Asia', 'Zbyszek', 'Marcin']
print(type(lista))  # <class 'list'>

