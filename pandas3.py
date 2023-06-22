import pandas as pd

miasta = pd.read_csv('worldcities.csv')
# print(miasta)

# print(miasta[10:20])
# print(miasta.head())  # 5 pierwszych wierszy
# print(miasta.tail())  # 5 ostatnich wierszy
# print(miasta[5:500:15])  # wyswietla co 15
# 5        Shanghai      Shanghai  31.1667  ...    admin  22120000.0  1156073548
# 20       Istanbul      Istanbul  41.0100  ...    admin  15154000.0  1792756324

# print(miasta[5:500:15][['city', 'iso2', 'capital']])
# miasta[5:500:15][['city', 'iso2', 'capital']].to_excel('test3.xlsx')
# print(miasta.info())
# print(miasta.describe())
# miasta.id.describe().to_csv('tt.csv')

# print(miasta.isnull().sum())
# print(miasta.notnull().sum())
print(miasta.duplicated().sum())
# print(miasta.duplicated())
miasta.drop_duplicates()
