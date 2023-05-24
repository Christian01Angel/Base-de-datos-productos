from logger import log


class Mates:
    _id = 0

    def __init__(self, id, codigo, nombre, categoria, precio):
        self._id = id
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._precio_menor = precio*1.75
        self._precio_mayor = precio*1.4

    @property
    def id(self):
        return self._id
    @property
    def codigo(self):
        return self._codigo
    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def precio_mayor(self):
        return self._precio_mayor

    @property
    def precio_menor(self):
        return self._precio_menor

    def __str__(self):
        return f'''ID={self._id}  --  CODIGO: {self._codigo} -- NOMBRE: {self._nombre}  --  CATEGORÍA: {self._categoria}  --  PRECIO COMPRA: {self._precio} --  PRECIO MENOR:{self._precio_menor}  --  PRECIO MAYOR: {self._precio_mayor}'''


if __name__ == '__main__':
    mate1 = Mates(1, 'M001', 'Marshmallow', 'Fortnite', 1150)
    print(mate1)
    mate2 = Mates(2, 'M002', 'Wilson', 'Pelicula', 1300)
    print(mate2)
