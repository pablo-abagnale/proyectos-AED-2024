import random

from Empleo import Empleo
def cargar_empleos():

    empleos = ('programador','Carpintero', 'RAC Call center','Supervisor','limpieza','seguridad')
    identificador = random.randint(100,500)
    descripcion = random.choice(empleos)
    tipo = random.randint(0,39)
    sueldo = random.randint(10000,50000)

    empleo = Empleo(identificador,descripcion,tipo,sueldo)

    return empleo

def mostrar(array):
    for i in array:
        print(i)

def ordenar(array):

    n = len(array)
    for i in range(n -1):
        for j in range(n - i - 1):
            if array[j].identifiacador > array[j+1].identifiacador:
                array[j],array[j+1] = array[j+1],array[j]
    return array
def suma(array):
    suma = 0
    n = len(array)
    for i in range(n):
        suma += array[i].sueldo

    return suma
def cantida(array):
    tipos = list(range(0, 39))
    x = [0] * 40
    for i in range(len(array)):
        ind = array[i].tipo - 1
        x[ind] += 1
    for i in range(len(tipos)):
        if x[i] > 0:
            print('Tipo ', tipos[i], ': ', x[i])

def buscar(array):

    num = int(input('Ingrese un numero de indetificacion que desea buscar: '))

    encotrado = False
    for i in range(len(array)):
        if array[i].identifiacador == num:
            encotrado = True
            print('Descricion; ',array[i].descripcion,' Sueldo: $',array[i].sueldo)
        else: encotrado = False
    while not encotrado:
        print('\nNo se encotro ese identificador\n')
        num = int(input('Ingrese un numero de indetificacion que desea buscar: '))
        encotrado = True



def principal():

    array_empleos = []
    ops = -1
    while ops != 0:

        print('MENU\n')
        print('1. Cargar nuevos empleos')
        print('2. Mostrar Empleos y total de sueldos')
        print('3. Cantidad de empleos por tipo')
        print('4. Busca empleos')
        print('0. Salir')

        ops = int(input('Selecciona una opcion:'))

        if ops == 1:
            cant = int(input('Cuantos empleos desea cargar ?: '))
            while cant == 0:
                cant = int(input('La cantidad no puede ser 0, Ingrese una catidad valida:'))
            else: cant = int(cant)
            for i in range(cant):
                array_empleos.append(cargar_empleos())
            mostrar(array_empleos)
        elif ops == 2:
            mostrar(ordenar(array_empleos))
            print('Total de sueldos:$',suma(array_empleos))

        elif ops == 3:
            cantida(array_empleos)

        elif ops == 4:
            buscar(array_empleos)
        elif ops >= 5:
            pass

if __name__ == '__main__':
        principal()