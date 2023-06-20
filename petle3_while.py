# petla while
# sterowana warunkiem
licznik = 0
while True:
    licznik += 1  # licznik = licznik + 1
    print('Komunikat')
    if licznik > 10:
        break  # przrywa działanie pętli

print(licznik)  # 11

licznik = 0
while licznik < 10:
    print("Komunikat")
    licznik += 1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)
print(lista2)
# ['5', '6', '7', '8']
# [5, 6, 7, 8]