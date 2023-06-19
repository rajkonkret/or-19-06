user = "Tomek"  # str
wiek = 39  # int - całkowite
wersja = 3.90000001  # float - zmiennoprzecinkowe
liczba = 134567123456  # int

print("Witaj  %s masz teraz %d lat" % (user, wiek))
# Witaj  Tomek masz teraz 39 lat
# print("Witaj  %s masz teraz %d lat" % (wiek, user))
# TypeError: %d format: a real number is required, not str
print('Witaj %(user)s, masz teraz %(wiek)d lat' % {'user': user, 'wiek': wiek})
print('Witaj %(user)s, masz teraz %(age)d lat' % {'user': user, 'age': wiek})  # Witaj Tomek, masz teraz 39 lat
# Witaj Tomek, masz teraz 39 lat

print("Witaj {} masz teraz {} lat".format(user, wiek))  # Witaj Tomek masz teraz 39 lat
print("Witaj {} masz teraz {} lat".format(wiek, user))  # Witaj 39 masz teraz Tomek lat

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.

print("Uzywamy wersji Python %i" % 3)  # Uzywamy wersji Python 3

print("Uzywamy wersji Python %i" % 3)
print("Uzywamy wersji Python %f" % 3.9)  # Uzywamy wersji Python 3.900000
print("Uzywamy wersji Python %.1f" % 3.9)  # Uzywamy wersji Python 3.9
print("Uzywamy wersji Python %.2f" % 3.9)  # Uzywamy wersji Python 3.90
print("Uzywamy wersji Python %.f" % 3.9)  # Uzywamy wersji Python 4
# zero miejsc po przecinku, ale z zaokrąglęniem
print("Używamy wersji Python %.0f" % 3.9)  # Używamy wersji Python 4
print("Uzywamy wersji Python {}".format(wersja))  # Uzywamy wersji Python 3.90000001

print(f"Uzywamy wersji Pythona {wersja}")  # Uzywamy wersji Pythona 3.90000001
print(f"Uzywamy wersji Pythona {wersja:.1f}")
print(f"Uzywamy wersji Pythona {wersja:.2f}")  # Uzywamy wersji Pythona 3.90
print(f"Uzywamy wersji Pythona {wersja:.0f}")  # Uzywamy wersji Pythona 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:>20}")
print(f"{user:<30}")  # "Tomek                         "

print(liczba)
print("Nasza duża liczba {:,}".format(liczba))
# Nasza duża liczba 134,567,123,456
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))
# Nasza duża liczba 134.567.123.456
# Nasza duża liczba 134 567 123 456
