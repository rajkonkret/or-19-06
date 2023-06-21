import pickle

lista = [1, 2, 3, 4, 5]

with open('test_lista.txt', 'w') as f:
    f.write(str(lista))

with open('test_lista.txt', 'r') as f:
    lines = f.read()

print(lines)
print(type(lines))  # <class 'str'>
print(lines[0])  # [

with open('lista_pickle.log', 'wb') as file:
    pickle.dump(lista, file)

with open('lista_pickle.log', 'rb') as file:
    loaded_list = pickle.load(file)

print(loaded_list)
print(type(loaded_list))  # <class 'list'>
print(loaded_list[0])  # 1
