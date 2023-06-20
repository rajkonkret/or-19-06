# funkcję, która oblicza średnią
def liczby(i=0, *cyfry):
    suma = 0
    print(cyfry)
    print(type(cyfry))  # <class 'tuple'>
    try:
        for cy in cyfry:
            print(cy)
            suma += cy
        print(suma)
        count = len(cyfry)

        print(f"Nr ucznia: {i}, Średnia wynosi: {suma / count}")  # Nr ucznia: 4,Srednia wynosi: 4.714285714285714

    except Exception as e:
        print("Bład", e)


liczby()
liczby(1, 2, 3, 4, 5, 6, 7, 8, 9)
liczby(4, 5, 6, 2, 3, 4, 5, 6, 5, 4, 3, 2, 6, 7, 8)
liczby("a", 2, 3)
liczby("a", 2, "a")
liczby(1, "2", "3")
