# pliki csv - dane oddzzielone znakiem podziału
# Radek,Maciek,Zenek

import csv

fileds = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '9']
dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'year': 2, 'name': "Radek"},
]

filename = 'records.csv'

with open(filename, 'w',newline='',encoding='utf-8') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fileds)
    csvwriter.writeheader()
    csvwriter.writerows(dict)
