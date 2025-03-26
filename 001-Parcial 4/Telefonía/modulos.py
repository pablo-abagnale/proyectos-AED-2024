from Clases import Usuario
import random

def menu():

    print('-'*50)
    print('1.Cargar datos')
    print('2.Mostrar datos')
    print('3.Consumo por hora y tipo')
    print('4.')
    print('5.')
    print('0.')

    opc = int( input('indique la opción seleccionada: ') )
    return opc

def add_in_order(array,dato):
    n = len(array)
    izq = 0
    der = n-1
    while izq <= der:
        c = (izq+der)//2
        if array[c].tel == dato.tel:
            pos = c
        elif array[c].tel < dato.tel:
            izq = c+1
        else:
            der = c-1
    else:
        pos = izq
    array[pos:pos] = [dato]

def cargar_array():
    array = []
    n = int(input('Ingrese la cantidad de datos a cargar: '))
    for i in range(n):
        tel = random.randint(11111111,99999999)
        hora = int(random.randrange(24))
        tipo = int(random.randint(1,3))
        monto = float(random.randint(1,100))
        usuario = Usuario(tel,hora,tipo,monto)
        add_in_order(array,usuario)

    return array

def mostrar_array(array):

    if not array:
        print('No hay datos')
    else:
        for i in array:
            print('-'*50)
            if i.tipo == 1:
                i.tipo = 'SMS'
            elif i.tipo == 2:
                i.tipo = 'Llamada'
            else:
                i.tipo = 'Datos'
            print(i)

def cargar_matriz(array):
    matriz = [[0]*3 for c in range(24)]
    for i in array:
        f = i.tipo
        c = i.hora
        matriz[f][c] +=1

    for i in len(matriz):
        for j in len(matriz[0]):
            if matriz[i][j] > -1 and matriz[i][j] < 13:
                print(matriz[i][j])

