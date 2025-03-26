import csv
import io
import os
import pickle
from Clases import Envio

__Autor__ = "<G196[1K13] Abagnale 96984 Baumann 41728 Briones 413712 >"

#Fuciones utiles y Constantes
FD = 'envios.dat' # Archivo Binario
def calcular_precio(tipo,pago,cp):
    precio = 0
    #Precio por tipo de envio
    if tipo == 0:
        precio = 1100
    elif tipo == 1:
        precio = 1800
    elif tipo == 2:
        precio = 2450
    elif tipo == 3:
        precio = 8300
    elif tipo == 4:
        precio = 10900
    elif tipo == 5:
        precio = 14300
    elif tipo == 6:
        precio = 17900

    #Modificador por region
    pais = identificar_pais(cp)

    if pais == 'Argentina':
        precio
    elif pais == 'Brasil':
        if cp[0] in [0,1,2,3]:
            precio = precio * 1.25
        elif cp[0] in [4,5,6,7]:
            precio = precio * 1.3
        elif cp[0] in [8,9]:
            precio = precio * 1.2
    elif pais == 'Uruguay':
        if cp[0] == 1:
            precio = precio * 1.2
        else:
            precio = precio * 1.25
    elif pais == 'Bolivia' or pais == 'Paraguay':
        precio = precio * 1.2
    elif pais == 'Chile':
        precio = precio * 1.25
    else:
        precio = precio * 1.5

    #Modificador por tipo de pago
    if pago == 1:
        precio = precio * 0.9

    return precio
def identificar_pais(cp):
    n = len(cp)
    if n == 8:  # ARGENTINA
        if 'A' <= cp[0] <= 'Z' and cp[0] != 'I' and cp[0] != 'O':
            if '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                if 'A' <= cp[5] <= 'Z' and 'A' <= cp[6] <= 'Z' and 'A' <= cp[7] <= 'Z':
                    pais = 'Argentina'
                else:
                    pais = 'Otro'
            else:
                pais = 'Otro'
        else:
            pais = 'Otro'
    else:
        if n == 4:  # BOLIVIA
            if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                pais = 'Bolivia'
            else:
                pais = 'Otro'
        else:
            if n == 9:  # BRASIL
                if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                    if '0' <= cp[4] <= '9' and cp[5] == '-':
                        if '0' <= cp[6] <= '9' and '0' <= cp[7] <= '9' and '0' <= cp[8] <= '9':
                            pais = 'Brasil'
                        else:
                            pais = 'Otro'
                    else:
                        pais = 'Otro'
                else:
                    pais = 'Otro'
            else:
                if n == 7:  # CHILE
                    if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                        if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9' and '0' <= cp[6] <= '9':
                            pais = 'Chile'
                        else:
                            pais = 'Otro'
                    else:
                        pais = 'Otro'
                else:
                    if n == 6:  # PARAGUAY
                        if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                            if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9':
                                pais = 'Paraguay'
                            else:
                                pais = 'Otro'
                        else:
                            pais = 'Otro'
                    else:
                        if n == 5:  # URUGUAY
                            if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9':
                                if '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                                    pais = 'Uruguay'
                                else:
                                    pais = 'Otro'
                            else:
                                pais = 'Otro'
                        else:
                            pais = 'Otro'
    return pais

#Menu
def mostrar_menu():

    print('\033[92m-'*50)
    print('\t\t\tMenu principal:')
    print('-' * 50,'\033[00m')
    print('\t\u27A4 1.Cargar datos desde archivo')
    print('\t\u27A4 2.Carga manual de datos')
    print('\t\u27A4 3.Mostrar todos los datos del registro')
    print('\t\u27A4 4.Mostrar registros de un CP')
    print('\t\u27A4 5.Buscar direccion')
    print('\t\u27A4 6.Mostrar envios por medio de pago')
    print('\t\u27A4 7.Envios por tipo  y en envios por pago')
    print('\t\u27A4 8.Importe promoedio de los envios cargados')
    print('\t\u27A4 0.Salir')
    print('\033[92m-' * 50, '\033[00m')
#Punto 1
def cargar_archivo():

    #Leer / Crear archivos
    fdatos = open('envios-tp4.csv', 'r')
    next(fdatos)#Saltar la primera linea de fdatos
    next(fdatos)#Saltar la segunda linea de fdatos
    fenvios = open( FD, 'wb')
    fenvios.seek(0,io.SEEK_SET)

    for dato in fdatos:
            partes = dato.strip().split(',')
            cp = partes[0]
            direccion = partes[1]
            tipo = int(partes[2])
            pago = int(partes[3])
            pais = identificar_pais(cp)
            monto = calcular_precio(tipo,pago,cp)
            envio = Envio(cp,direccion,tipo,pago,pais,monto)
            pickle.dump(envio, fenvios)
    #Cerrar archivos
    fdatos.close()
    fenvios.close()
#Punto 2
def carga_manual():

    fenvios = open(FD, 'ab')

    print('Ingrese los datos del envio:')

    cp = input('\tCodigo postal: ')
    while len(str(cp)) < 0 or len(str(cp)) > 9:
        if len(str(cp)) > 9:
            print('\n\t\033[91m--El codigo ingresado es demaciado largo--\033[00m\n')
        else: print('\n\t\033[91m--debe ingresar un codigo postal--\033[00m\n')
        cp = int(input('\tCodigo postal: '))

    direccion = input('\tIngresa la direccion de envio: ')

    print('\tTipos de envio : '
          '\n\t\t0-Carta simple hasta 20g'
          '\n\t\t1-Carta simple de 20g a 150g'
          '\n\t\t2-Carta simple de 150g a 500g'
          '\n\t\t3-Carta certificada hasta 150g'
          '\n\t\t4-Carta certificada desde 150g'
          '\n\t\t5-Carta expresa hasta 150g'
          '\n\t\t6-Carta expresa desde 150g')
    tipo = int(input('\tIngresa la tipo de envio: '))
    while not tipo in [0,1,2,3,4,5,6]:
        print('\t\033[91m--El tipo de envio ingresado es invalido--\033[00m')
        tipo = int(input('\tIngresa la tipo de envio valido: '))

    print('\tMedio de pago : '
          '\n\t\t1-Efectivo'
          '\n\t\t2-Tarjeta')
    pago = int(input('\tSelecciona el metodo  de pago: '))
    while not pago in [1,2]:
        print('\t\033[91m--El metodo de pago ingresado es invalido--\033[00m')
        pago = int(input('\tSelecciona el metodo  de pago valido: '))
    pais = identificar_pais(cp)
    monto = calcular_precio(tipo,pago,cp)
    envio = Envio(cp, direccion, tipo, pago,pais,monto)
    fenvios.seek(0,io.SEEK_END)
    pickle.dump(envio, fenvios)

    fenvios.close() # Cerrar archivos
#Punto 3
def mostrar():

    if os.path.exists(FD):
        fenvios = open(FD, 'rb')

        tm = os.path.getsize(FD)
        while fenvios.tell() < tm:
            envio = pickle.load(fenvios)
            print(envio)

    else:
        print('\t\033[91m--No hay datos cargados--\033[00m')
        print('\t\033[91m--Seleccione las opciones 1 o 2 en el Menu principal--\033[00m')

#Punto 4
def buscar_mostrar_cp():

    buscado = input('\tIngresa el codigo postal: ')
    print('\n')
    encotrado = False
    if os.path.exists(FD):
        fenvios = open(FD, 'rb')

        tm = os.path.getsize(FD)
        while fenvios.tell() < tm:
            envio = pickle.load(fenvios)
            if envio.cp == buscado:
                encotrado = True
                print(envio)

        if not encotrado: print(f'\n\t\033[91m--No se encotro el CP: {buscado} --\033[00m')

    else:
        print('\t\033[91m--No hay datos cargados--\033[00m')
        print('\t\033[91m--Seleccione las opciones 1 o 2 en el Menu principal--\033[00m')

#Punto 5
def buscar_mostrar_direccion():

    d = input('\tIngresa la direccion de envio: ')
    print('\n')
    encotrado = False
    if os.path.exists(FD):
        fenvios = open(FD, 'rb')

        tm = os.path.getsize(FD)
        while fenvios.tell() < tm:
            envio = pickle.load(fenvios)
            if envio.direccion == d:
                encotrado = True
                print(envio)
                break
        if not encotrado: print(f'\n\t\033[91m--No hay registros en la direccion: {d} --\033[00m')

    else:
        print('\t\033[91m--No hay datos cargados--\033[00m')
        print('\t\033[91m--Seleccione las opciones 1 o 2 en el Menu principal--\033[00m')

#Punto 6
def matriz_conteo_tipo_pago():
    if os.path.exists(FD):
        fenvios = open(FD, 'rb')

        # Crear matriz de conteo
        matriz = [[0] * 7 for x in range(2)]
        tm = os.path.getsize(FD)
        while fenvios.tell() < tm:
            envio = pickle.load(fenvios)
            #Cargar la matiz
            fila = envio.pago -1
            columna = envio.tipo
            matriz[fila][columna] +=1

        return matriz

    else:
        print('\t\033[91m--No hay datos cargados--\033[00m')
        print('\t\033[91m--Seleccione las opciones 1 o 2 en el Menu principal--\033[00m')

#Punto 7
def total_envios_pagos(matriz):

    if os.path.exists(FD):
        fenvios = open(FD, 'rb')

        f = len(matriz)
        c = len(matriz[0])
        total_envio = 0
        total_pago = 0
        for i in range(f):
            for j in range(c):
                total_pago = 0
                total_pago += int(matriz[i][j])
            print(f"\033[33mTotal de pagos {i+1}:\033[00m{total_pago}")
        # Calcular la suma de cada columna
        for j in range(c):
            for i in range(f):
                total_envio = 0
                total_envio += int(matriz[i][j])
            print(f"\033[34mTotal envios del tipo {j}:\033[00m {total_envio}")
    else:
        print('\t\033[91m--No hay datos cargados--\033[00m')
        print('\t\033[91m--Seleccione las opciones 1 o 2 en el Menu principal--\033[00m')

#Punto 8
def promedio_pago():
    suma = 0
    cont = 0
    if os.path.exists(FD):
        fenvios = open(FD, 'rb')

        tm = os.path.getsize(FD)
        while fenvios.tell() < tm:
            envio = pickle.load(fenvios)
            cont += 1
            suma += envio.monto
        promedio = suma/cont
        return promedio
    else:
        print('\t\033[91m--No hay datos cargados--\033[00m')
        print('\t\033[91m--Seleccione las opciones 1 o 2 en el Menu principal--\033[00m')
def add_in_order(array,dato):

    #Modificar el Atributo fecha por el que se desee usar

    n = len(array)
    izq = 0
    der = n - 1
    while izq <= der:
        centro = (izq + der) // 2
        if array[centro].cp == dato.cp:
            pos = centro
            break
        elif array[centro].cp > dato.cp:
            der = centro - 1
        else:
            izq = centro + 1
    else:
        pos = izq

    array[pos:pos] = [dato]
def cargar_mayores(promedio):
    array_mayores = []
    promedio

    if os.path.exists(FD):
        fenvios = open(FD, 'rb')

        tm = os.path.getsize(FD)
        while fenvios.tell() < tm:
            envio = pickle.load(fenvios)
            if envio.monto > promedio:
                add_in_order(array_mayores,envio)
    return array_mayores
def mostrar_arreglo(array):
    cout = 0
    for i in array:
        cout += 1
        print(i)
    print(f'\n\033[34mcantidad de envios con precio mayor que el promedio: \033[00m {cout}\n')
def mayore_promedio():
    if os.path.exists(FD):
        fenvios = open(FD, 'rb')

        promedio = promedio_pago()
        print(f'\033[34mPromedio:\033[00m {round(promedio,2)}\n')
        array_mayores = cargar_mayores(promedio)
        mostrar_arreglo(array_mayores)
    else:
        print('\t\033[91m--No hay datos cargados--\033[00m')
        print('\t\033[91m--Seleccione las opciones 1 o 2 en el Menu principal--\033[00m')