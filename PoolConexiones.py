from psycopg2 import pool
from logger import log
import sys

class Conexion:
    _DATABASE = 'productos3d'
    _USERNAME = 'postgres'
    _PASSWORD = 'River01plate'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password= cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE,)
                log.debug(f'Creación del pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrío un error al crear el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida al pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al poo: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.debug('Se han cerrado todas las conexiones')


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()
    # conexion7 = Conexion.obtenerConexion()
