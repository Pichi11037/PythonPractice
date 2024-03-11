from poolCursor import PoolCursor
from person import Person
import logging as log

log.basicConfig(level=log.DEBUG)

'''
DAO (DATA ACCESS OBJECT)
CRUD (CREATE READ UPDATE DELETE)
'''

class PersonDAO:

    _SELECT = 'SELECT * FROM "Person" ORDER BY id_persona'
    _SELECTONE = 'SELECT * FROM "Person" WHERE id_persona=%s ORDER BY id_persona'
    _INSERT = 'INSERT INTO "Person"(nombre, apellido, email) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE "Person" SET nombre = %s, apellido=%s, email=%s WHERE id_persona=%s'
    _DELETE = 'DELETE FROM "Person" WHERE id_persona=%s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            log.debug(cursor.closed)
            cursor.execute(cls._SELECT)
            records = cursor.fetchall()
            personas = []
            for record in records:
                persona = Person(record[0], record[1], record[2], record[3])
                personas.append(persona)
            return personas
            
    @classmethod
    def selectOne(cls, persona):
        with PoolCursor() as cursor:
            try:
                value = (str(persona.id), )
                cursor.execute(cls._SELECTONE, value)
                record = cursor.fetchone()
                persona = Person(int(record[0]), record[1], record[2], record[3])
                return persona
            except Exception as e:
                log.error(f'Error occured: {e}')
    
    @classmethod
    def insert(cls, persona):
        with PoolCursor() as cursor:
            log.debug(f'Persona a insertar: {persona}')
            name = persona.name
            lastName = persona.lastName
            email = persona.email
            values = (name, lastName, email)
            cursor.execute(cls._INSERT, values)
            log_inserted = cursor.rowcount
            return log_inserted
    
    @classmethod
    def update(cls, persona):
        with PoolCursor() as cursor:
            values = (persona.name, persona.lastName, persona.email, persona.id)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'Person updated: {persona}')
            return cursor.rowcount

    
    @classmethod
    def delete(cls, persona):
        with PoolCursor() as cursor:
            value = (persona.id, )
            cursor.execute(cls._DELETE, value)
            return cursor.rowcount, persona

    

if __name__ == '__main__':

    # Select all
    personas = PersonDAO().select()
    for n in personas:
        log.debug(n)

    # Insert
    nPersona = Person(64, 'newperson', 'newperson', 'newperson@email.com')
    personsInserted = PersonDAO().insert(nPersona)
    log.debug(f'Persons inserted: {personsInserted}')
    
    # Select one
    personSelected = PersonDAO().selectOne(nPersona)
    log.debug(f'Person selected: {personSelected}')
    

    # # Update
    nPersona.name = "pepito"
    nPersona.lastName = "perez"
    nPersona.email = "pppppp@email.com"
    personUpdated = PersonDAO().update(nPersona)

    # Select one
    personSelected = PersonDAO().selectOne(nPersona)

    # Delete
    n, personDeleted = PersonDAO().delete(nPersona)
    log.debug(f'Persons deleted: {n}; {personDeleted}')
    
    # Select one
    personSelected = PersonDAO().selectOne(nPersona)