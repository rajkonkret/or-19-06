import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = re.get(url)
print(response)
# <Response [200]> - ok
# 3xx - problemy
# 4xx - błedy np.: 404 - błedny adres, 400 bad request
# 5xx - błedy wewnetrzne serwera

table = response.json()
print(table)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '117/A/NBP/2023', 'effectiveDate': '2023-06-20', 'mid': 4.4386}]}
print(table['table'])  # A
print(table['currency'])  # euro
print(table['rates'])  # [{'no': '117/A/NBP/2023', 'effectiveDate': '2023-06-20', 'mid': 4.4386}]
print(table['rates'][0])  # {'no': '117/A/NBP/2023', 'effectiveDate': '2023-06-20', 'mid': 4.4386}
print(table['rates'][0]['mid'])  # 4.4386
print(table['rates'][0]['effectiveDate'])  # 2023-06-20
