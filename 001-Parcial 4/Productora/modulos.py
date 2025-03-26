import io
import os.path
import pickle
from Clase import Pelicula
import random

FB = 'peliculas.dat'

def menu():
    print('-'*50)
    print('Menu principal')
    print('1.Carga manual')
    print('2.Mostrar datos')
    print('3.Buscar pelicula y modificar importe')
    print('4.Cargar archivo')
    print('5.Mostrar archivo')
    print('6.Buscar pelicula por Id ')
    print('7.Peliculas por pais y tipo')
    print('0.Salir')
    opc = int(input('\ningresa una opcion: '))
    return opc

def add_in_order(array,dato):
    n = len(array)
    izq = 0
    der = n-1
    while izq <= der:
        c = (izq + der)//2
        if array[c].titulo == dato.titulo:
            pos = c
            break
        elif array[c].titulo < dato.titulo:
            der = c-1
        else:
            izq = c+1
    else:
        pos = izq

    array[pos:pos] = [dato]

def carga_manual():
    peliculas = [
        "The Shawshank Redemption",
        "The Godfather",
        "The Dark Knight",
        "Pulp Fiction",
        "Forrest Gump",
        "Inception",
        "Fight Club",
        "The Matrix",
        "Goodfellas",
        "The Silence of the Lambs",
        "Schindler's List",
        "The Empire Strikes Back",
        "The Lord of the Rings",
        "Back to the Future",
        "Gladiator",
        "Braveheart",
        "The Lion King",
        "Jurassic Park",
        "Titanic",
        "Avatar"
    ]
    n = int(input('\ningrese cuantas peliculas desea cargar: '))
    array_peliculas = []
    for i in range(n):
        identificador = random.randint(000,999)
        titulo = str(random.choice(peliculas))
        titulo = titulo.strip()
        importe = random.uniform(1500,15000)
        tipo = random.randrange(10)
        pais = random.randrange(20)
        pelicula = Pelicula(identificador,titulo,importe,tipo,pais)

        add_in_order(array_peliculas,pelicula)
    return array_peliculas

def mostrar(array):
    if array == []:
        print('No hay datos, selecciona la opcion 1')
    else:
        for i in array:
            print(i)


def buscar_modificar_importe(array):
    if not array:
        print('No hay datos, selecciona la opción 1')
    else:
        mostrar(array)
        encontrado = False
        nom = input('\nBuscar película: ')
        for i in range(len(array)):
            if array[i].titulo == nom:
                encontrado = True
                nuevo_importe = float(input(f'\nIngresa nuevo importe para "{array[i].titulo}": '))
                array[i].importe = nuevo_importe
                print(array[i])
                break
        if not encontrado:
            print(f'No se encontró la película {nom}')

    if not encontrado:
        print(f'No se encotro la pelicula {nom}')


def cargar_archivo(array):
    if array == []:
        print('No hay datos, selecciona la opcion 1')
    else:
        fpeliculas = open(FB,'ab')
        n = len(array)
        for i in array:
            fpeliculas.seek(0,io.SEEK_END)
            pickle.dump(i,fpeliculas)
        print('El archivo se cargo correctamente')
    fpeliculas.close()

def mostrar_archivo():
    if not os.path.exists(FB):
        print('No hay datos, selecciona la opcion 1')
    else:
        fpeliculas = open(FB,'rb')
        tm = os.path.getsize(FB)
        while fpeliculas.tell() < tm:
            pelicula = pickle.load(fpeliculas)
            print(pelicula)

def mostrar_id(array):
    if array == []:
        print('No hay datos, selecciona la opcion 1')
    else:
        encontrado = False
        num = int(input('\ningresa un el id que desea buscar: '))
        for pelicula in array:
            if pelicula.identificador == num:
                encontrado = True
                print(pelicula)
        if not encontrado:
                print(f'No se encontro la pelicula con id {num}')

def matriz_pais_tipo(array):

    matriz = [[0]*20 for c in range(10)]
    for pelicula in array:
        f = pelicula.tipo
        c = pelicula.pais
        matriz[f][c] +=1
    fila = len(matriz)
    column = len(matriz[0])
    for i in range(fila):
        for j in range(column):
            if matriz[i][j] > 0:
                print(i, j, matriz[i][j])



