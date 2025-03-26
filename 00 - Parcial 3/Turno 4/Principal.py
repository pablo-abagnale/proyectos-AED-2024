from Clase import Juicio
import random

def cargar():
        '''
        codigo = int(input("Ingrese el codigo del juicio: "))
        caratula = input("Ingrese la caratula / descripcion del juicio: ")
        tipo = int(input("Ingrese el tipo del juicio (1 a 15): "))
        while tipo < 1 or tipo > 15:
           print("\nIngrese un tipo valido - entre 1 y 15\n ")
           tipo = int(input("Ingrese el tipo del juicio (1 a 15): "))
        else: tipo = int(tipo)
        cliente = input("Ingrese el nombre del cliente: ")
        honorario = int(input("Ingrese el monto de los horarios del juicio: "))
        '''
        nombres = ("Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad","Pablo","Levi","Luciana","Florencia","Laura")
        apellidos = ("Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)

        codigo = random.randint(1, 5000)
        caratula = "Juicio de "+nombre+" "+apellido
        tipo = random.randint(1,15)
        cliente = nombre+" "+apellido
        honorario = random.randint(0,10000)
        

        juicio = Juicio(codigo, caratula, tipo,cliente ,honorario)

        return juicio

def mostrar(array):

    for i in array:
        print (i)

def ordenar(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def contar(array):
    c = int(input(' 0 para mostrar todos los juicios o  solo los tipos con mas de '))
    tipos = list(range(1, 16))
    x = [0] * 15
    for i in range(len(array)):
        ind = array[i].tipo - 1
        x[ind] += 1
    for i in range(len(x)):
        if x[i] > c:
            print('Tipo', tipos[i], '-', x[i])

def modificar(array):

    buscado = int(input("Ingrese el expediente buscado: "))

    for i in range(len(array)):
        if array[i].codigo == buscado:
            encotrado = True
            print(array[i])
            monto = int(input("Ingrese el monto de los horarios del juicio: "))
            array[i].honorario = monto
            print(array[i])

        else:
            encotrado = False

    if encotrado == False:
        print("El expediente no se encuentra en la lista")









def principal():

    array_jucios = []
    opc = -1
    while opc != 0:
        # Menu
        print('\n')
        print("1 - Cargar juicios ")
        print("2 - Mostrar juicios ")
        print("3 - Mostrar Jucios por tipo ")
        print("4 - Modificar honorarios ")
        print("0 - Salir ")
        opc = int(input("\nSeleccione una opcion: "))
        if opc == 1:
            n = int(input("cuantos jucios desea cargar? : "))

            for i in range(n):
                print('\nJuicio', i + 1)
                array_jucios.append(cargar())
                print(array_jucios[i])

                print('Juicio cargado con exito\n')

        elif opc == 2:
            array_jucios_montos = []

            if array_jucios == []:
                print("No hay juicios para mostrar, seleccione 1 para cargar .")
                pass
            else:
                print('0 - para cargar todos los juicios o selecciona un monto')
                mon = int(input("Mostrar juicios por honorarios mayores a : "))


                for i in range(len(array_jucios)):
                   if array_jucios[i].honorario > mon:
                       array_jucios_montos.append(array_jucios[i])

                mostrar(array_jucios_montos)


        elif opc == 3:
            if array_jucios == []:
                print("No hay juicios para mostrar, seleccione 1 para cargar .")
                pass
            else:
                contar(array_jucios)

        elif opc == 4:
            if array_jucios == []:
                print("No hay juicios para mostrar, seleccione 1 para cargar .")
                pass
            else:
                modificar(array_jucios)

        elif opc >= 5:
            print("Seleccione una opcion valida ")
            pass





if __name__ == "__main__":
    principal()