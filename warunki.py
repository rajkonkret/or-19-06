# warunki - instrukcja sterowania przepływem programu

odp = False

if odp:
    print("Brawo")  # wciecie obowiązkowe
else:
    print("Musisz się uczyć dalej")

print("Program działa nadal")

# podatek = 0.0
# zarobki = int(input('Podaj dochód'))  # zamiana na int, bo input zwraca stringa
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
# # ponizej 30000, powyzej 10000 podatek ma byc 20%(0.2)
# print(f"Zapłacisz {zarobki * podatek} zł")

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

lista_bledow = []
alert_system = 'console'
error = 'medium'
error_message = "Stało się coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append('inny')

print(lista_bledow)

# test z historii
# wyswietlic pytanie
# pobrac odpowiedz
# zweryfikowac odpowiedz
# wyswietlic wynik

odp = input("Podaj datę Chrztu Polski")  # str
if odp == '966':
    print("Brawo")
else:
    print("Masz to na stronie 23 podręcznika")
