print()  # wydrukuj/wypisz
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Jacek")  # Nazywam się Jacek
# ctrl d - powielanie kodu
# type - odczytanie typu jaki jest przekazywany
print(type("Radek"))  # <class 'str'> - stringi - teksty
# ctrl alt l - formtowanie kodu

print(39)  # 39
print(type(39))  # <class 'int'> - liczby całkowite

print("39" + "15")  # konkatenacja tekstow 3915
print(39 + 15)  # 54
print(5 * "4")  # 44444

imie = "Radek"
print(imie)  # Radek - zawartość zmiennej imie
print(type(imie))  # <class 'str'>

wiek = 48
print(wiek)
print(type(wiek))  # <class 'int'>
print(type(type(wiek)))  # <class 'type'>
print(imie + str(type(imie)))  # Radek<class 'str'>
# str() - rzutowanie (zamiana) na typ str
# print(imie + wiek)  # TypeError: can only concatenate str (not "int") to str
print(imie + str(wiek))  # Radek48

wiek = "Radek"
print(wiek)
print(type(wiek))
# 11:30
# PS C:\Users\CSComarch\PycharmProjects\or-19-06> python.exe .\pierwszy.py