import sys
from psycopg2 import pool
from logger_base import log

class Connection:
    _DATABASE = 'DataLayerProject'
    _USERNAME = 'pichi'
    _PASSWORD = '11037'
    _DBPORT = '5432'
    _HOST = '127.0.0.1'
    _pool = None
    _MIN = 1
    _MAX = 5

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
                    minconn = cls._MIN,
                    maxconn = cls._MAX
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
    def closeConnection(cls):
        cls.getPool().closeall()