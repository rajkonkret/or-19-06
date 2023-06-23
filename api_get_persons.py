import requests

# pobieranie losowych informacji o uzytkowników
response = requests.get('https://randomuser.me/api/')
data = response.json()

print(data)
# {'results': [{'gender': 'female', 'name': {'title': 'Mrs', 'first': 'Alexandra', 'last': 'Meyer'},
#               'location': {'street': {'number': 988, 'name': 'High Street'}, 'city': 'Roscrea', 'state': 'Louth',
#                            'country': 'Ireland', 'postcode': 39887,
#                            'coordinates': {'latitude': '2.6275', 'longitude': '158.8019'},
#                            'timezone': {'offset': '-11:00', 'description': 'Midway Island, Samoa'}},
#               'email': 'alexandra.meyer@example.com',
#               'login': {'uuid': '098015c9-5e60-4806-ade4-70444b0e442b', 'username': 'crazyladybug101',
#                         'password': 'toonarmy', 'salt': '5xaIazQZ', 'md5': '0f81d8525530ff2c89996b2d7df4ab4a',
#                         'sha1': '4f7cc21cf4af3a197b1b3442297685310313ea26',
#                         'sha256': '2c5e9a0ed83f8e169991930aa52eaa940955f2c46b6b2154f4741d3a9602e869'},
#               'dob': {'date': '1959-07-10T21:45:14.282Z', 'age': 63},
#               'registered': {'date': '2008-05-09T19:37:59.259Z', 'age': 15}, 'phone': '061-082-2174',
#               'cell': '081-730-6683', 'id': {'name': 'PPS', 'value': '3513602T'},
#               'picture': {'large': 'https://randomuser.me/api/portraits/women/25.jpg',
#                           'medium': 'https://randomuser.me/api/portraits/med/women/25.jpg',
#                           'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/25.jpg'}, 'nat': 'IE'}],
#  'info': {'seed': 'aac93212ff1461f0', 'results': 1, 'page': 1, 'version': '1.4'}}
user = data['results'][0]
print(user)
print("Imię", user["name"]['first'])
print("Nazwisko", user["name"]['last'])
print("Email", user["email"])
print("Zdjęcie")
photo_url = user['picture']['large']
response_photo = requests.get(photo_url)

with open("user_photo.jpg", "wb") as f:
    f.write(response_photo.content)

print("Zdjęcie zapisane!")
