# argumenty słownikowe
def connect(**opcje):
    print(opcje)  # {'name': 'radek'}
    print(type(opcje))  # <class 'dict'>
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)  # {'host': '127.0.0.7', 'port': '8080'}
    connect_param['pwd'] = opcje
    print(connect_param)
    # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'name': 'radek'}}
    connect_param.update({'pwd2': opcje})
    print(connect_param)
    # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'name': 'radek'}, 'pwd2': {'name': 'radek'}}


# connect(1,2,3,4,5)
# TypeError: connect() takes 0 positional arguments but 5 were given
connect(name="radek")
connect(a=9, b=8)
connect(user="Radek", host="/", parametr="abc")
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'user': 'Radek', 'host': '/', 'parametr': 'abc'},
#  'pwd2': {'user': 'Radek', 'host': '/', 'parametr': 'abc'}}
