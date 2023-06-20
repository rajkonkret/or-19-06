# json - {'name':'Radek"}
# json obiekt typu klucz-wartosc
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(person_dict)
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)
# {"name": "Radek", "age": 40, "czy_pali": null}

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(data['name'])  # Radek
print(data.keys())
print(data.values())
print(data.items())
# dict_keys(['name', 'age', 'czy_pali'])
# dict_values(['Radek', 40, None])
# dict_items([('name', 'Radek'), ('age', 40), ('czy_pali', None)])
