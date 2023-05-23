from logger import log
from MatesDao import MatesDao
from Mates import Mates

def tomarDesicion(accion, producto):
    respuesta = input(f'Desea continuar {accion} {producto}? (S/N):')
    if respuesta in 'Ss':
        return True
    elif respuesta in 'Nn':
        return False
    else:
        print('Valor ingresado invalido, por favor intentelo de nuevo')
        tomarDesicion(accion, producto)



print('Bienvenido al sistema de administración de productos')

condicion = True

while condicion:
    print('''
    Seleccione una opcion del menu:
    1-Insertar un producto
    2-Actualizar un producto
    3-Ver los productos en el registro
    4-Buscar un producto
    5-Eliminar un producto
    6-Boleta para pedido
    7-Salir
    ''')

    opcion_menu = int(input('Opción seleccionada(1-7): '))

    if opcion_menu == 1:
        decision = True
        while decision:
            id = int(input('Ingrese el ID: '))
            codigo = input('Ingrese el código: ')
            nombre = input('Ingrese el nombre: ')
            categoria = input('Ingrese las categorías separadas por un espacio: ')
            precio = int(input('Ingrece el precio de compra: '))
            mate = Mates(id, codigo, nombre, categoria, precio)
            MatesDao.insertar(mate)
            decision = tomarDesicion('insertar', 'mate')

    elif opcion_menu == 2:
        decision = True
        while decision:
            id = int(input('Indique el ID del mate a modificar: '))
            codigo = input('Ingrese el código a actualizar: ')
            nombre = input('Ingrese el nombre a actualizar: ')
            categoria = input('Ingrese las categorías a actualizar, separadas por un espacio: ')
            precio = int(input('Ingrece el precio de compra a actualizar: '))
            mate = Mates(id, codigo, nombre, categoria, precio)
            MatesDao.actualizar(mate)
            desicion = tomarDesicion('actualizar', 'mate')

    elif opcion_menu == 3:
        mates = MatesDao.seleccionar()
        for mate in mates:
            log.debug(mate)

    elif opcion_menu == 4:
        print('''
        Categorías de busqueda:
        1- ID
        2- Código
        3- Nombre
        4- Categoría
        5- Precio
        ''')
        # busqueda = int(input('Elija una categoría de busqueda (1-5): '))
        # if busqueda==1:
        #     id = int(input('Indique el ID a buscar: '))
        #     mates = MatesDao.buscar('id')
        #     for mate in mates:
        #         log.debug(mate)
        # elif busqueda == 2:
        #     codigo = int(input('Indique el Código a buscar: '))
        #     mates = MatesDao.buscar('codigo')
        #     for mate in mates:
        #         log.debug(mate)
        # elif busqueda == 3:
        #     nombre = int(input('Indique el Nombre a buscar: '))
        #     mates = MatesDao.buscar('nombre')
        #     for mate in mates:
        #         log.debug(mate)
        # elif busqueda == 4:
        #     categoria = int(input('Indique el Categoría a buscar: '))
        #     mates = MatesDao.buscar('categoria')
        #     for mate in mates:
        #         log.debug(mate)
        # elif busqueda == 5:
        #     precio = int(input('Indique el Precio a buscar: '))
        #     mates = MatesDao.buscar(precio)
        #     for mate in mates:
        #         log.debug(mate)


