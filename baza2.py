import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    query = '''
    CREATE TABLE SqliteDb_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);'''

    with open('tables.sql', 'r') as file:
        sql_sript = file.read()

    cursor = sql_connection.cursor()
    print("Baza danych została podłączona...")

    # cursor.execute(query)
    # sql_connection.commit()

    cursor.executescript(sql_sript)

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")

# Baza danych została podłączona...
# Baza została zamknięta
