import psycopg2

connection = psycopg2.connect(
    user ='pichi',
    password = '11037',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
    )

# try:
#     connection.autocommit = False
#     cursor = connection.cursor()
#     query1 = "INSERT INTO \"Person\"(nombre, apellido, email) VALUES(%s, %s, %s)"
#     values1 = ('Pedro', 'Casa', 'pcasa@mail.com')
#     cursor.execute(query1, values1)

#     query2 = "INSERT INTO \"Person\"(nombre, apellido, email) VALUES(%s, %s, %s)"
#     values2 = ('Jose', 'Jojote', 'jjojotea@mail.com')
#     cursor.execute(query2, values2)
    
#     connection.commit()
#     print('Transaction finished, commit done!')
# except Exception as e:
#     connection.rollback()
#     print(f'Error in 1: {e}')
# finally:
#     connection.close()


try:
    with connection:
        with connection.cursor() as cursor:
            connection.autocommit = False
            query1 = "INSERT INTO \"Person\"(nombre, apellido, email) VALUES(%s, %s, %s)"
            values1 = ('Pedro', 'Casa', 'pcasa@mail.com')
            cursor.execute(query1, values1)

            query2 = "INSERT INTO \"Person\"(nombre, apellido, email) VALUES(%s, %s, %s)"
            values2 = ('Jose', 'Jojote', 'jjojotea@mail.com')
            cursor.execute(query2, values2)

            # connection.commit()
            # print('Transaction finished, commit done!')
except Exception as e:
    print(f'Error, rollback done: {e}')
finally:
    connection.close()

