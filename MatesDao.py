from logger import log
from Mates import Mates
from CursorPool import CursorPool

class MatesDao:
    _SELECCIONAR = 'SELECT * FROM mates ORDER BY id'
    _INSERTAR = 'INSERT INTO mates(codigo, nombre, categoria, precio_compra, precio_mayor, precio_menor) VALUES (%s, %s, %s, %s, %s, %s)'
    _ACTUALIZAR = 'UPDATE mates SET codigo=%s, nombre=%s, categoria=%s, precio_compra=%s, precio_mayor=%s, precio_menor=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM mates WHERE id=%s'
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            print(registros)
            mates = []
            for registro in registros:
                mate = Mates(registro[0], registro[1], registro[2], registro[3], registro[4])
                mates.append(mate)
            return mates

    @classmethod
    def insertar(cls, mate):
        with CursorPool() as cursor:
            valores = (mate.codigo, mate.nombre, mate.categoria, mate.precio, mate.precio_mayor, mate.precio_menor)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Mate insertado: {mate}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, mate):
        with CursorPool() as cursor:
            valores = (mate.codigo, mate.nombre, mate.categoria, mate.precio, mate.precio_mayor, mate.precio_menor, mate.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Mate actualizado: {mate}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, id):
        with CursorPool() as cursor:
            cursor.execute(cls._ELIMINAR, id)
            log.debug(f'Mate eliminado: {mate}')



if __name__ == '__main__':
    # mate1 = Mates(1, 'M001', 'Marshmallow', 'Fortnite', 1150)
    # MatesDao.insertar(mate1)
    # mate2 = Mates(2, 'M002', 'Wilson', 'Pelicula Pelota Naufrago', 1150)
    # MatesDao.insertar(mate2)

    mates = MatesDao.seleccionar()
    for mate in mates:
        log.debug(mate)
