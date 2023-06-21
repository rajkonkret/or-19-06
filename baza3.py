import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    insert = '''
    INSERT INTO software (id,name,price) VALUES(2,'Python', 200);
    '''
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona...")

    cursor.execute(insert)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")

# Baza danych została podłączona...
# Baza została zamknięta
