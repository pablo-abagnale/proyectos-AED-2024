from modulos import *

__Autor__ = "<G196[1K13] Abagnale 96984 Baumann 41728 Briones 413712 >"

def principal():

    opc = -1

    while opc != 0:

        mostrar_menu()
        opc = input('Escribe una opcion: ')

        if opc == '1':#Cargar archivo binario
            print('\n\033[32m1.Cargar datos desde archivo\033[00m\n')
            continuar = 1
            while continuar != 2:
                print('\nVa a \033[91meliminar\033[00m el archivo anterior\n')
                continuar = int(input('\t1.Continuar\n\t2.Volver al menu anterior\n'))
                if continuar == 1:
                    cargar_archivo()
                    break
                elif continuar > 2 or continuar < 1:
                    print('\n\t\033[91mOpcion invalida\033[00m\n')

        if opc == '2':
            print('\n\033[32m2.Carga manual de datos\033[00m\n')
            carga_manual()
            continuar = 1
            while continuar != 2:
                print('\n\033[92mDesea continuar cargarndo\033[00m\n')
                continuar = int(input('\t1.Continuar\n\t2.Volver al menu principal\n'))
                if continuar == 1:
                    carga_manual()

        if opc == '3':
            print('\n\033[32m3.Mostrar todos los datos del registro\033[00m\n')
            mostrar()

        if opc == '4':
            print('\n\033[32m4.Mostrar registros de un CP\033[00m\n')
            buscar_mostrar_cp()
            continuar = 1
            while continuar != 2:
                print('\n\033[92mDesea buscar otro CP ?\033[00m\n')
                continuar = int(input('\t1.Buscar\n\t2.Volver al menu principal\n'))
                if continuar == 1:
                    buscar_mostrar_cp()

        if opc == '5':
            print('\n\033[32m5.Buscar direccion\033[00m\n')
            buscar_mostrar_direccion()
            continuar = 1
            while continuar != 2:
                print('\n\033[92mDesea buscar otra direccion ?\033[00m\n')
                continuar = int(input('\t1.Buscar\n\t2.Volver al menu principal\n'))
                if continuar == 1:
                    buscar_mostrar_direccion()
        if opc == '6':
            print('\n\033[32m6.Mostrar envios por medio de pago\033[00m\n')
            matriz = matriz_conteo_tipo_pago()
            # mostrar matriz
            f = len(matriz)
            c = len(matriz[0])
            for i in range(f):
                for j in range(c):
                    if matriz[i][j] != 0 and i == 0:
                        print(f'\033[33mTipo\033[00m {j} \033[33mcon fectivo:\033[00m {matriz[i][j]}')
                    if matriz[i][j] != 0 and i == 1:
                        print(f'\033[33mTipo\033[00m {j} \033[33mcon tarjeta:\033[00m {matriz[i][j]}')
        if opc == '7':
            print('\n\033[32m7.Envios por tipo  y en envios por pago\033[00m\n')
            matriz = matriz_conteo_tipo_pago()
            total_envios_pagos(matriz)
        if opc == '8':
            print('\n\033[32m8.Importe promoedio de los envios cargados\033[00m\n')
            mayore_promedio()
        if opc == '0':
            print('\n\033[32mHasta luego \033[00m \U0001F609\n')
            break

if __name__ == "__main__":
    principal()


