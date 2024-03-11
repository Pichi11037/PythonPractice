from logger_base import log
from service.Connection import Connection

class PoolCursor:
    def __init__(self):
        self._connection = None
        self._cursor = None

    def __enter__(self):
        
        log.debug('enter method start')
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor
    
    def __exit__(self, exceptionType, exceptionValue, exceptionTraceback):
        log.debug('exit method start')
        if exceptionValue:
            self._connection.rollback()
            log.error(f'Error, rollback done: {exceptionValue}, {exceptionType}, {exceptionTraceback}')
        else:
            self._connection.commit()
            log.debug('Transaction commited')
        self._cursor.close()
        Connection.freeConnection(self._connection)