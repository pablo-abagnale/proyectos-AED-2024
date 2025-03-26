import io
import pickle
import os

from Clases import Profecional
import random

FB = 'profecionales.dat'
def menu():

    print('\nMenu principal')
    print('-'*50)
    print('1.Cargar los datos ')
    print('2.Mostrar los datos')
    print('3.Buscar DNI - Importes desactulizados')
    print('4.Crear archivos de datos')
    print('5.Mostrar archivos de datos')
    print('6.Buscar por nombre')
    print('7.Tipo de afiliaci{on por tipo de trabajo')
    print('0.Salir')

    opc = int(input('\nSeleccione una opcion: '))

    return opc

def add_in_order(array,dato):

    n = len(array)
    izq =  0
    der = n - 1
    while izq <= der:
        c = (izq+der)//2
        if array[c].documento == dato.documento:
            pos = c
        elif array[c].documento < dato.documento:
            izq = c + 1
        else:
            der = c - 1
    else:
        pos = izq
    array[pos:pos] = [dato]
def cargar_datos():
    array = []
    nombres = ["Carlos", "María", "Juan", "Ana", "José", "Laura", "Miguel", "Elena", "Luis", "Patricia"]
    apellidos = ["González", "Rodríguez", "Pérez", "Martínez", "Gómez", "López", "Díaz", "Fernández", "Muñoz",
                 "Hernández"]
    n = int(input('Ingrese la cantidad de datos a cargar : '))

    for i in range(n):
        documento = int(random.randint(11111111, 99999999))
        nombre = (random.choice(nombres)+' '+random.choice(apellidos))
        importe = float(random.randint(1000,100000))
        afilicion = int(random.randrange(4))
        trabajo = int(random.randrange(15))
        profecional = Profecional(documento,nombre,importe,afilicion,trabajo)
        add_in_order(array,profecional)
    return array

def mostrar_array(array):
    if not array:
        print('no hay datos cargados')
    else:
        for i in array:
            print('-'*110)
            print(i)

def buscaqueda_ordenada(array,valor):
    pos = - 1
    n = len(array)
    izq = 0
    der = n - 1
    while izq <= der:
        c = (izq+der)//2
        if array[c].documento == valor:
            pos = c
            break
        elif array[c].documento > valor:
            der = c -1
        else:
            izq = c +1
    return pos

def buscar_desactulizado(array):

    dni = int(input('Ingrese el DNI que desea buscar: '))
    pos = buscaqueda_ordenada(array,dni)
    exite = False
    print(pos)
    if pos != -1:
        exite = True
        valor_actual = float(input('Ingrese el valor actual: '))
        print(array[pos])
        if array[pos].importe < valor_actual:
            print(f'El improte ${array[pos].importe} esta desactualizado')
    if not exite:
        print('No hay concidencias')
def crear_archivo(array):
    fprof = open(FB,'ab')
    fprof.seek(0,io.SEEK_SET)
    for i in array:
        pickle.dump(i,fprof)
    fprof.close()
def mostrar_archivo(array):

    if not os.path.exists(FB):
        print('El archivo no existe')
    else:
        fprof = open(FB,'rb')
        tm = os.path.getsize(FB)
        while fprof.tell() < tm:
            profecional = pickle.load(fprof)
            print(profecional)

def buscar_nombre(array):
    if not array:
        print('no hay datos cargados')
    else:
        exisite = False
        nom = input('Ingrese el nombre que desea buscar: ')
        for i in array:
            if i.nombre == nom:
                exisite = True
                print(i)
                break
        if not exisite:
            print('No se encutro el nombre que desea buscar')


def crear_matriz(array):
    if not array:
        print('no hay datos cargados')
    else:
        matriz = [[0]*5 for i in range(15)]
        for i in array:
            f = i.afilicacion
            c = i.trabajo
            matriz[c][f] +=1
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] > 0:
                    print(i,j,matriz[i][j])
