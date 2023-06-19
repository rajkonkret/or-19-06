# set  - przechowuje niepowtarzające się elementy

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
print(lista)
print(type(lista))  # <class 'list'>

zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} - klamerka, nie zapamietał kolejnosci

zb2 = set()  # pusty set
print(zb2)  # set()

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)

print(zbior.pop())  # 33
print(zbior)
print(zbior.pop())
print(zbior.pop())
print(zbior.pop())
print(zbior)  # {44, 18, 22, 55}

zbior.remove(55)
zbior.remove(18)
print(zbior)  # {44, 22}

lista2 = list(zbior)
print(lista2)
print(type(lista2))  # <class 'list'>

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {18, 52, 999, 11, 44, 667, 62}

print(zbior | zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62} - suma zbiorów
print(zbior & zbior2)  # {44} - czesc wspolna
print(zbior - zbior2)  # różnica  {22}
print(zbior.difference(zbior2))  # {22}
print(zbior2.difference(zbior))  # {999, 11, 18, 52, 667, 62}
