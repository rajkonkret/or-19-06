import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    select = '''
    SELECT * FROM software;
    '''

    update = '''
    UPDATE software SET price = 2000 WHERE id =1;
    '''

    delete = '''
    DELETE FROM software WHERE id = 1;
    '''

    cursor = sql_connection.cursor()
    print("Baza danych została podłączona...")

    for row in cursor.execute(select):
        print(row)

    # cursor.execute(update)
    # sql_connection.commit()

    cursor.execute(delete)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")

# Baza danych została podłączona...
# Baza została zamknięta
# (1, 'Python', 200.0)
# (1, 'Python', 2000.0)
# Baza danych została podłączona...
# (2, 'Python', 200.0)
# Baza została zamknięta
