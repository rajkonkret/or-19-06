import pandas as pd

# pip install pandas

data = pd.read_csv('records.csv')
print(data)

#     name branch  year  cgpa
# 0  Radek    COE     2   9.1
print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)  # [['Radek' 'COE' 2 9.1]]

print(data.values[0])  # ['Radek' 'COE' 2 9.1]
print(type(data.values[0]))  # <class 'numpy.ndarray'>
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  Radek    COE     2   9.1>
# 13:30
