from logger import log
from Mates import Mates
from CursorPool import CursorPool

class MatesDao:
    _SELECCIONAR = 'SELECT * FROM mates ORDER BY id'
    _INSERTAR = 'INSERT INTO mates(codigo, nombre, categoria, precioCompra, precioMayor, precioMenor) VALUES (%s, %s, %s, %s, %s, %)'
    _ACTUALIZAR = 'UPDATE mates SET codigo=%s, nombre=%s, categoria=%s, precioCompra=%s, precioMayor=%s, precioMenor=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM mates WHERE id=%s'
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            mates = []
            for registro in registros:
                mate = Mates(registro[0], registro[1], registro[2], registro[3])
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
    def eliminar(cls, mate):
        with CursorPool() as cursor:
            cursor.execute(cls._ELIMINAR, mate.id)
            log.debug(f'Mate eliminado: {mate}')
            return cursor.rowcount


if __name__ == '__main__':
    mate1 = Mates('M001', 'Marshmallow', 'Fortnite Cabeza Epic Juegos', 1150)
    mate2 = Mates('M002', 'Wilson', 'Pelicula Pelota Naufrago', 1150)
    MatesDao.insertar(mate1)
    MatesDao.insertar(mate2)

    mates = MatesDao.seleccionar()
    for mate in mates:
        log.debug(mate)
