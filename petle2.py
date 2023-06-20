dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(dictionary)
print(type(dictionary))  # <class 'dict'>

# wyswietla klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

print(dictionary.keys())

# wypisze wartości
for v in dictionary.values():
    print(v)

print(dictionary.items())  # dict_items([('imie', 'Radek'), ('nazwisko', 'Kowalski')])

for i in dictionary.items():
    print(i)  # ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => Kowalski

dictionary2 = {'name': 'imie', 'company': 'Orange'}
print(dictionary2)
# {'name': 'imie', 'company': 'Orange'}
print({value: key for key, value in dictionary2.items()})
# {'imie': 'name', 'Orange': 'company'}

d2 = {}
for k, v in dictionary2.items():
    d2[v] = k  # zamiana miejscami klucza z wartoscią
print(d2)
# {'imie': 'name', 'Orange': 'company'}
# 11:20
