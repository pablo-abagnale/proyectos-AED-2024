import random
from Ticket import Ticket

def cargar():

    letras = ("A","B","C","D")
    codigo = random.choice(letras)+random.choice(letras)+str(random.randint(100,999))
    pasajero = random.randint(1000,8000)
    pais =  random.randint(1,20)
    asiento = random.randint(1,500)
    importe = random.randint(2000, 20000)

    ticket = Ticket(codigo,pasajero, pais, asiento, importe)

    return ticket

def mostrar(array):

    for i in range(len(array)):
        print('-' * 250)
        print(array[i])
    print('-' * 250)

def ordernar (array):

    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j].codigo > array[j+1].codigo:
                array[j],array[j+1] = array[j+1],array[j]
    return array

def buscar(array):

    buscado = int(input("Ingrese el id que desea buscar: "))
    encotrado = False
    for i in range(len(array)):
        if int(array[i].pasajero) == buscado:
            encotrado = True
            print('N° de asiento:', array[i].asiento,'Destino:', array[i].pais)
    if not encotrado:
        print('el Id buscado no existe')


def principal():
    array_tickt = []
    opc = -1

    while opc != 0:

        print('1. Cargar ticket de vuelos')
        print('2. Mostrar ticket')
        print('3. Mostrar ticket por pais')
        print('4. Buscar por id de pasajero')
        print('0. Salir')
        opc = int(input('\nIngrese una opcion:'))

        if opc == 1:
            c = int(input('\n Cuantos tickets desea cargar:'))
            for i in range(c):
                array_tickt.append(cargar())
            mostrar(array_tickt)
        if opc == 2:
            c = int(input('\n Mostrar ticket con nuemro de asiento mayor a:'))
            ordernar(array_tickt)
            for i in range(len(array_tickt)):
                if array_tickt[i].asiento > c:
                    print(array_tickt[i])

        if opc == 3:

            t = int(input('valor superior a :'))

            tipos = list (range(1,20))
            x = [0]*20
            for i in range(len(array_tickt)):
                ind = array_tickt[i].pais - 1
                x[ind] += array_tickt[i].importe
            for i in range(len(tipos)):
                if x[i] > t:
                    print('Tipo ',tipos[i],':$',x[i])

        if opc == 4:
            buscar(array_tickt)
        if opc >= 5:
            pass

if __name__ == '__main__':
    principal()