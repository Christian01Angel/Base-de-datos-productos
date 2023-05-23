from PoolConexiones import Conexion
from logger import log


class CursorPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Se hace rollback debido a que ocurrío un error: {valor_excepcion}--{tipo_excepcion}--{detalle_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Se hizo commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM mates')
        log.debug(cursor.fetchall())
