# wyjątki

# print(2 / 0)  # ZeroDivisionError: division by zero
# print("Dalsza część programu")
# kalkulator
# menu z operacjami
# pobranie liczb
# wykonanie działąnia
# prezentacja wyniku

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie 
    5. Koniec
    """)

    odp = input("Podaj działąnie jakie chcesz wykonać")
    if odp == '5':
        break
    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))
        # dodac mnozenie i dzielenie
        # wynik dodawania 2 + 4  = 6
        if odp == '1':
            print(f"Wynik działania {a} + {b} = {a + b}")
        elif odp == '2':
            print(f"Wynik działania {a} - {b} = {a - b}")
        elif odp == '3':
            print(f"Wynik działania {a} * {b} = {a * b}")
        elif odp == '4':
            print(f"Wynik działania {a} / {b} = {a / b}")
        else:
            print("Nie znam takiego działania")

    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Bląd wartości")
    except TypeError:
        print("Bład typu")
    except Exception as e:
        print("Wystąpił bład", e)
    else:
        print("Gdy nie będzie błedu")
    finally:  # to wykona sie zawsze
        print("Zawsze")
# ValueError: invalid literal for int() with base 10: 'a'
