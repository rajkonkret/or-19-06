# listy składane - listy budowane w jedej linijce

numbers = [1, 2, 3, 4, 5]

# tworzenie nowej listy
squared = [num ** 2 for num in numbers]
print(f"Squared: {squared}")  # Squared: [1, 4, 9, 16, 25]
# for num in numbers:
#     jakaslista.append(x ** 2)

# lista liczb parzystych z danej listy - filtrowanie
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even: {even_numbers}")  # Even: [2, 4]

# modyfikacja w zależnosci od warunku
modified_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(f"Zmodyfikowane: {modified_numbers}")  # Zmodyfikowane: [1, 4, 3, 8, 5]

# parzysta - nieparzysta
even_odd = ['parzysta' if x % 2 == 0 else 'nieparzysta' for x in numbers]
print(f"Parzyste - Nieparzyste {even_odd}")
# Parzyste - Nieparzyste ['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta', 'nieparzysta']

squared_numbers = [x ** 2 for x in range(1, 6)]  # 1..5
print(f"Kwadrat liczb z zakresu {squared_numbers}")
# Kwadrat liczb z zakresu [1, 4, 9, 16, 25]

# abs() - wartośc absolutna
numbers2 = [-1, -2, 3, -4, 5]
absolute = [abs(x) for x in numbers2]
print(f"Wartości absolutne {absolute}")  # Wartości absolutne [1, 2, 3, 4, 5]

word = "Pyton"
letters = [letter for letter in word]
print(f"Literki: {letters}")
Literki: ['P', 'y', 't', 'o', 'n']

lista1 = [word]
print(type(lista1))
print(lista1)  # ['Pyton']

print(list(word))  # ['P', 'y', 't', 'o', 'n']
