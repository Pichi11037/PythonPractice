from service.PoolCursor import PoolCursor
from domain.User import User
from logger_base import log

class UserDAO:
    _SELECT = 'SELECT * FROM "Users" ORDER BY user_id'
    _INSERT = 'INSERT INTO "Users"(username, password) VALUES(%s, %s)'
    _UPDATE = 'UPDATE "Users" SET username=%s, password=%s WHERE user_id=%s'
    _DELETE = 'DELETE FROM "Users" WHERE user_id=%s'

    @classmethod
    def select(cls):
        with PoolCursor() as cursor:
            log.debug(cursor.closed)
            cursor.execute(cls._SELECT)
            records = cursor.fetchall()
            users = []
            for record in records:
                user = User(record[0], record[1], record[2])
                users.append(user)
            return users

    @classmethod
    def insert(cls, user):
        with PoolCursor() as cursor:
            log.debug(cursor.closed)
            username = user.username
            password = user.password
            values = (username, password)
            cursor.execute(cls._INSERT, values)
            return cursor.rowcount

    @classmethod
    def update(cls, user):
        with PoolCursor() as cursor:
            log.debug(cursor.closed)
            values = (user.username, user.password, user.id)
            cursor.execute(cls._UPDATE, values)
            log.debug(f'User updated: {user}')
            return cursor.rowcount

    @classmethod
    def delete(cls, user):
        with PoolCursor() as cursor:
            log.debug(cursor.closed)
            value = (user.id, )
            cursor.execute(cls._DELETE, value)
            return cursor.rowcount
