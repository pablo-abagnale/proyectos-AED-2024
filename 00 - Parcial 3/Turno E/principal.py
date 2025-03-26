import random
from Publicacion import Publicacion


def cargar():
        letras = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n")
        nlibro =random.randint(1, 500)
        codigo = random.choice(letras)+random.choice(letras)+str(random.randint(1, 500))
        titulo = 'LibroN'+str(nlibro)
        tipo = random.randint(1, 30)
        costo = random.randint(5000, 30000)
        publicacion = Publicacion(codigo, titulo, tipo, costo)

        return publicacion
def mostrar(array):
    for i in array:
        print(i)

def ordenar(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def contar(array):
    valor = int(input('Mostrar cuantas publicaciones de cada tipo tienen un valor mayor a: '))
    tipos = list(range(1, 31))
    x = [0] * 30

    mostrar(array)
    print('-' * 50)
    print('-' * 50)

    for i in range(len(array)):
        ind = array[i].tipo - 1
        x[ind] += 1
    for i in range(len(tipos)):
        if x[i] > valor:
            print('Tipo ', tipos[i], ': ', x[i])

def buscar(array):

    titulo_b = input('Ingrese el titulo de la publicacion: ').strip()
    tipo_b = int(input('Ingrese el tipo de la publicacion: '))

    titulo_encotrado = False
    tipo_encotrado = False

    for i in array:
        if i.titulo == titulo_b:
            titulo_encotrado = True
            if i.tipo == tipo_b:
                tipo_encotrado = True
                print('\n')
                print(i)

    if not titulo_encotrado:
        print('Titulo', titulo_b, 'no se encotro')
    if not tipo_encotrado:
        print('Tipo ', tipo_b, 'no se encotro')


def principal():
    array_publicaciones =[]
    opc = -1
    while opc != 0:

        #Menu
        print('Bienvenido al menu\n')
        print('1- Cargar publicaciones')
        print('2- Mostrar publicaciones')
        print('3- Mostrar publicaiones por tipo')
        print('4- buscar por tiutlo y tipo')
        print('0 - Salir')
        opc=int(input('\nSeleccione una opcion: '))

        if opc == 1:
            n = int(input('Cuantas publicaciones desea cargar: '))
            for i in range(n):
                array_publicaciones.append(cargar())

            mostrar(array_publicaciones)

        elif opc == 2:
            if array_publicaciones == []:
                print('No hay publicaciones cargadas - selecciona la opcion 1')
                pass
            else:
                mostrar(array_publicaciones)
                print('-'*50)
                cos = int(input('mostrar publicaciones con un costo mayor a: '))
                ordenar(array_publicaciones)
                for i in array_publicaciones:
                    if cos < i.costo:
                        print('\n')
                        print(i)
        elif opc == 3:
            if array_publicaciones == []:
                print('No hay publicaciones cargadas - selecciona la opcion 1')
                pass
            else:
                contar(array_publicaciones)

        elif opc == 4:
            buscar(array_publicaciones)
        elif opc >= 5:
            pass

if __name__ == "__main__":
    principal()