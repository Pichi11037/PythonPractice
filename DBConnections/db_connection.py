import psycopg2

connection = psycopg2.connect(
    user ='pichi',
    password = '11037',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_db'
    )
# # Database Connection (postgreSQL)
try:
    with connection:
        with connection.cursor() as cursor:
            query = "SELECT * FROM \"Person\""
            cursor.execute(query)
            logs = cursor.fetchall()
            print(logs)
except Exception as e:
    print(f'Error in 1: {e}')

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
    print(f'Error in 2 : {e}')

# fetchall function
try:
    with connection:
        with connection.cursor() as cursor:
            query = f'SELECT * FROM \"Person\" WHERE id_persona IN %s'
            inp = input('Provide the id\'s to search (separated by commas): ')
            pk = (tuple(inp.split(',')), )
            cursor.execute(query, pk)
            logs = cursor.fetchall()
            for log in logs:
                print(log)
except Exception as e:
    print(f'Error in 3: {e}')

# Insert  value
try: 
    with connection:
        with connection.cursor() as cursor:
            query = 'INSERT INTO "Person"(nombre, apellido, email) VALUES(%s, %s, %s)'
            value = ('Carlos', 'Lara', 'clara@email.com')
            cursor.execute(query, value)
            # connection.commit() Working with the 'with' codeblock, you dont have to use the commit() function
            log_inserted = cursor.rowcount
            print(f'Logs inserted: {log_inserted}')
except Exception as e:
    print(f'Error in 4: {e}')

# Insert multiple  value
try: 
    with connection:
        with connection.cursor() as cursor:
            query = 'INSERT INTO "Person"(nombre, apellido, email) VALUES(%s, %s, %s)'
            values = (
                ('Miguel', 'Mendoza', 'mmendoza@email.com'),
                ('Joaquin', 'Paul', 'jpaul@email.com'),
                ('Daniel', 'Rodriguez', 'drodriguez@email.com'),
            )
            cursor.executemany(query, values)
            # connection.commit() Working with the 'with' codeblock, you dont have to use the commit() function
            log_inserted = cursor.rowcount
            print(f'Logs inserted: {log_inserted}')
except Exception as e:
    print(f'Error in 5: {e}')

# Update a value
try: 
    with connection:
        with connection.cursor() as cursor:
            query = 'UPDATE "Person" SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            pk = input('Provide the id where you want to update: ')
            values = ('Marco', 'Mendoza', 'mmendoza@email.com', pk)
            cursor.execute(query, values)
            # connection.commit() Working with the 'with' codeblock, you dont have to use the commit() function
            log_inserted = cursor.rowcount
            print(f'Logs updated: {log_inserted}')
except Exception as e:
    print(f'Error in 6: {e}')

#  Update multiple values
try: 
    with connection:
        with connection.cursor() as cursor:
            query = 'UPDATE "Person" SET nombre = %s WHERE id_persona = %s'
            pks = input('Provide the ids where you want to update (separated by commas): ').split(',')
            names = input("Provide then new name for all the rows(separated by commas): ").split(',')
            arr = []
            for n in range(len(pks)):
                t = tuple([names[n], pks[n]])
                arr.append(t)
            tup = tuple(arr)
            cursor.executemany(query, tup)
            # connection.commit() Working with the 'with' codeblock, you dont have to use the commit() function
            log_inserted = cursor.rowcount
            print(f'Logs updated: {log_inserted}')
except Exception as e:
    print(f'Error in 7: {e}')

#  Delete a value
try: 
    with connection:
        with connection.cursor() as cursor:
            query = 'DELETE FROM "Person" WHERE id_persona = %s'
            pks = input('Provide the id where you want to delete: ')
            value = (pks, )
            cursor.execute(query, value)
            # connection.commit() Working with the 'with' codeblock, you dont have to use the commit() function
            log_deleted = cursor.rowcount
            print(f'Log deleted: {log_deleted}')
except Exception as e:
    print(f'Error in 8: {e}')

#  Delete multiple values
try: 
    with connection:
        with connection.cursor() as cursor:
            query = 'DELETE FROM "Person" WHERE id_persona IN %s'
            pks = input('Provide the ids where you want to delete (separated by commas): ').split(',')
            tup = (tuple(pks), )
            cursor.execute(query, tup)
            # connection.commit() Working with the 'with' codeblock, you dont have to use the commit() function
            logs_deleted = cursor.rowcount
            print(f'Logs deleted: {logs_deleted}')
except Exception as e:
    print(f'Error in 9: {e}')

finally:
    cursor.close()
    connection.close()
