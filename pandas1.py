import pandas as pd

lista = [[2, 5, 8, 9], [9, 8, 5, 4]]
slownik = {'Imie': ['Ania', 'Michał', 'Przemek'], 'wiek': [18, 22, 34]}
zbior = pd.DataFrame(lista)

zbior.columns = ['jeden', 'dwa', 'trzy', 'cztery']
sl = pd.DataFrame(slownik)
print(sl)
# print(zbior)
# zbior.to_csv('test1.csv')

sl.to_csv('test2.csv')