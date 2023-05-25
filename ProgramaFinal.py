import time

from logger import log
from MatesDao import MatesDao
from Mates import Mates

def tomarDesicion(accion, producto):
    time.sleep(1)
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
    time.sleep(1)
    print('''
    Seleccione una opcion del menu:
    1-Insertar un producto
    2-Actualizar un producto
    3-Ver los productos en el registro
    4-Buscar un producto
    5-Eliminar un producto
    6-Salir
    ''')

    opcion_menu = int(input('Opción seleccionada(1-7): '))
    time.sleep(1)

    if opcion_menu == 1:
        decision = True
        while decision:
            id = int(input('Ingrese el ID: '))
            codigo = input('Ingrese el código: ')
            nombre = input('Ingrese el nombre: ')
            categoria = input('Ingrese las categorías separadas por un espacio: ')
            precio = int(input('Ingrese el precio de compra: '))
            mate = Mates(id, codigo, nombre, categoria, precio)
            MatesDao.insertar(mate)
            decision = tomarDesicion('insertando', 'mates')

    elif opcion_menu == 2:
        decision = True
        while decision:
            id = int(input('Indique el ID del mate a modificar: '))
            codigo = input('Ingrese el código a actualizar: ')
            nombre = input('Ingrese el nombre a actualizar: ')
            categoria = input('Ingrese las categorías a actualizar, separadas por un espacio: ')
            precio = int(input('Ingrese el precio de compra a actualizar: '))
            mate = Mates(id, codigo, nombre, categoria, precio)
            MatesDao.actualizar(mate)
            decision = tomarDesicion('actualizando', 'mates')

    elif opcion_menu == 3:
        mates = MatesDao.seleccionar()
        for mate in mates:
            log.debug(mate)

    elif opcion_menu == 4:
        decision = True
        while decision:
            print('''
            Categorías de busqueda:
            1- Código
            2- Nombre
            3- Categoría
            4- Precio Mayorista
            5- Precio Minorista
            6- Volver atras
            ''')
            busqueda = int(input('Elija una categoría de busqueda (1-6): '))
            time.sleep(1)
            mates = MatesDao.seleccionar()
            time.sleep(0.2)

            if busqueda == 1:
                codigo = input('Ingrese el código que desea buscar: ')
                for mate in mates:
                    if codigo == mate.codigo:
                        log.debug(mate)

            elif busqueda == 2:
                nombre = input('Ingrese el nombre que desea buscar: ')
                for mate in mates:
                    if nombre == mate.nombre:
                        log.debug(mate)

            elif busqueda == 3:
                categoria = input('Ingrese la categoría que desea buscar: ')
                for mate in mates:
                    if categoria in mate.categoria:
                        log.debug(mate)

            elif busqueda == 4:
                precio_mayor = int(input('Ingrese el precio por mayor que desea buscar: '))
                for mate in mates:
                    if precio_mayor == mate.precio_mayor:
                        log.debug(mate)

            elif busqueda == 5:
                precio_menor = int(input('Ingrese el precio por menor que desea buscar: '))
                for mate in mates:
                    if precio_menor == mate.precio_menor:
                        log.debug(mate)

            elif busqueda == 6:
                decision = False

            else:
                print('Comando invalido, por favor intentelo otra vez.')
                time.sleep(0.5)

            if str(busqueda) in '12345':
                decision = tomarDesicion('buscando', 'mates')

    elif opcion_menu == 5:
        id = int(input('Ingrese el id del mate a eliminar'))
        MatesDao.eliminar(id)

    elif opcion_menu == 6:
        print('Gracias por utilizar el sistema')
        time.sleep(0.5)
        print('Adios')
        time.sleep(0.5)
        condicion = False

    else:
        print('Comando invalido, por favor intentelo otra vez.')
        time.sleep(0.5)
