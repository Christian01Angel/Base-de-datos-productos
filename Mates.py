from logger import log


class Mates:
    id = 1

    def __init__(self, nombre, precio, categoria):
        self._nombre = nombre
        self._precio = precio
        self._categoria = categoria
        self._precio_menor = precio*1.75
        self._precio_mayor = precio*1.4
        if self.id < 10:
            self._codigo = 'M00' + str(self.id)
        elif 10 <= self.id < 100:
            self._codigo = 'M0' + str(self.id)
        elif self.id >= 100:
            self._codigo = 'M' + str(self.id)
        self.id += 1

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def categoria(self):
        return self._categoria

    @property
    def codigo(self):
        return self._codigo

    def __str__(self):
        return f''' CODIGO: {self._codigo} -- NOMBRE: {self._nombre}  --  PRECIO COMPRA: {self._precio} --  PRECIO MENOR:{self._precio_menor}  --  PRECIO MAYOR: {self._precio_mayor}'''


if __name__ == '__main__':
    mate1 = Mates('Marshmallow', 1150, 'Fortnite')
    print(mate1)
