import logging as log
from connection import Connection

class PoolCursor:
    

    def __init__(self) -> None:
        self._connection = None
        self._cursor = None

    def __enter__(self):
        log.debug('__enter__ method start')
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor
    
    def __exit__(self, exceptionType, exceptionValue, exceptiontraceback):
        log.debug('__exit__ method start')
        if exceptionValue:
            self._connection.rollback()
            log.error(f'Error, rollback done: {exceptionValue} {exceptionType} {exceptiontraceback}')
        else:
            self._connection.commit()
            log.debug('Transaction commited')
        self._cursor.close()
        Connection.freeConnection(self._connection)