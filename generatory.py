def kwadrat(n):
    for x in range(n):
        print(x ** 2)


# generator
def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonuje operacje, zwraca wynik, zapamietuje sobie


kwadrat(5)
kwa = kwadrat2(5)
print(type(kwa))  # <class 'generator'>

print(next(kwa))
print(next(kwa))

print("wypisz cokolwiek")
print("Zrobić cokolwiek")
lista = []
lista.append("1234566")
print(lista)

print(next(kwa))
print(next(kwa))
print(next(kwa))


# print(next(kwa))  # StopIteration


def counter(start=0):
    n = start
    while True:
        yield n
        n += 1


def counter_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


c = counter()
print(next(c))
print(next(c))
print(next(c))

c2 = counter_down(10)
print(next(c2))
print(next(c2))
print(next(c2))
print(next(c2))


def counter_2(start=0):
    n = start
    while True:
        result = yield n
        print(result)
        if result == 'q':
            break
        n += 1


c3 = counter_2(10)
print(next(c3))

print(c3.send('OK'))
print(next(c3))
# c3.send('q')  # StopIteration
# print(next(c3))
