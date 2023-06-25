import pysftp

# Utwórz parametry połączenia
host = 'test.rebex.net'
port = 22
username = 'demo'
password = 'password'

# Tworzenie obiektu CnOpts i wyłączenie weryfikacji klucza hosta
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Nawiąż połączenie SFTP
with pysftp.Connection(host=host, port=port, username=username, password=password, cnopts=cnopts) as sftp:
    # Wykonaj operacje SFTP
    file_list = sftp.listdir()  # Pobierz listę plików na serwerze
    print(file_list)  # Wyświetl listę plików
