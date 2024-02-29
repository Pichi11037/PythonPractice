import psycopg2

connection = psycopg2.connect(
    user ='pichi',
    password = '11037',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
    )
# Database Connection (postgreSQL)
try:
    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM \"Person\""
            cursor.execute(query)
            logs = cursor.fetchall()
            print(logs)
except Exception as e:
    print(f'no value inserted:{e}')

# Search for a user with a query
try:
    with connection:
        with connection.cursor() as cursor:
            id = str(input('Ingrese el id a buscar: '))
            query = f'SELECT * FROM \"Person\" WHERE id_persona = %s'
            cursor.execute(query, (id,))
            log = cursor.fetchone()
            print(log)
except Exception as e:
    print(f'Ocurrio un error: {e}')

# fetchall function
try:
    with connection:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM \"Person\" WHERE id_persona IN (1,2,3)'
            cursor.execute(query)
            logs = cursor.fetchall()
            for log in logs:
                print(log)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    cursor.close()
    connection.close()
