import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    csvreader = csv.reader(csv_f)
    print(type(csvreader))  # <class '_csv.reader'>

    fields = next(csvreader)  # przestawia wskaznik na kolejny

    for row in csvreader:
        rows.append(row)

print(fields)  # ['name', 'branch', 'year', 'cgpa']
print(rows)  # [['Radek', 'COE', '2', '9.1']]
print(rows[0])
print(rows[0][0])  # Radek
