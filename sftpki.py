import ftplib

ftp = ftplib.FTP('test.rebex.net')
logowanie = ftp.login('demo', 'password')
print(logowanie)
# tabnine

# katalog = ftp.nlst()
katalog = ftp.nlst('pub/example')
print(katalog)
# plik = ftp.retrbinary('RETR readme.txt', open('README.log', 'wb').write)
plik = ftp.retrbinary('RETR pub/example/KeyGenerator.png', open('obraz.png', 'wb').write)