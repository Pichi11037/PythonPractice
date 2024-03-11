import logging as log
import sys
from psycopg2 import pool

log.basicConfig(level=log.DEBUG)

class Connection:
    _DATABASE = 'test_db'
    _USERNAME = 'pichi'
    _PASSWORD = '11037'
    _DBPORT = '5432'
    _HOST = '127.0.0.1'
    _pool = None
    _MIN = 1
    _MAX = 5
    # _connection =  None
    # _cursor = None

    @classmethod
    def getPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    user = cls._USERNAME,
                    password = cls._PASSWORD,
                    host = cls._HOST,
                    port = cls._DBPORT,
                    database = cls._DATABASE,
                    minconn= cls._MIN,
                    maxconn= cls._MAX
                    )
                log.debug(f'Pool connected successfully: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Error getting pool connection: {e}')
                sys.exit()
        else:
            return cls._pool
        
    @classmethod
    def getConnection(cls):
        connection = cls.getPool().getconn()
        log.debug(f'Connection retrieved successfully: {connection}')
        return connection
    
    @classmethod
    def freeConnection(cls, connection):
        cls.getPool().putconn(connection)
        log.debug(f'Connection freed: {connection}')

    @classmethod
    def closeConnections(cls):
        cls.getPool().closeall()

#     @classmethod
#     def getConnection(cls):
#         log.debug(cls._connection)
#         if cls._connection is None:
#             try:
#                 cls._connection = psycopg2.connect(
#                     user = cls._USERNAME,
#                     password = cls._PASSWORD,
#                     host = cls._HOST,
#                     port = cls._DBPORT,
#                     database = cls._DATABASE
#                 )
#                 log.debug(f'Succesfully connected to Database: {cls._connection}')
#                 return cls._connection
#             except Exception as e:
#                 log.error(f'Error {e}')
#                 sys.exit()
#         else:
#             return cls._connection

#     @classmethod
#     def getCursor(cls):
#         if cls._cursor is None or cls._cursor.closed is True:
#             try:
#                 cls._cursor = cls.getConnection().cursor()
#                 log.debug(f'Cursor successfully retrieved {cls._cursor}')
#                 return cls._cursor
#             except Exception as e:
#                 log.error(f'Error: {e}')
#                 sys.exit()
#         else:
#             return cls._cursor
    
#     @classmethod
#     def close(cls):
#         if cls._cursor is not None:
#             cls.getCursor.close()
#             log.info(f'Cursor closed')
        
#         if cls._connection is not None:
#             cls._connection.close()
#             log.info(f'Connection closed')

# if __name__ == '__main__':
#     Connection().getConnection()

#     @classmethod
#     def getCursor(cls):
#         if cls._cursor is None or cls._cursor.closed is True:
#             try:
#                 cls._cursor = cls.getConnection().cursor()
#                 log.debug(f'Cursor successfully retrieved {cls._cursor}')
#                 return cls._cursor
#             except Exception as e:
#                 log.error(f'Error: {e}')
#                 sys.exit()
#         else:
#             return cls._cursor
    
#     @classmethod
#     def close(cls):
#         if cls._cursor is not None:
#             cls.getCursor.close()
#             log.info(f'Cursor closed')
        
#         if cls._connection is not None:
#             cls._connection.close()
#             log.info(f'Connection closed')

if __name__ == '__main__':
    connection1 = Connection.getConnection()
    connection2 = Connection.getConnection()
    connection3 = Connection.getConnection()
    connection4 = Connection.getConnection()
    connection5 = Connection.getConnection()