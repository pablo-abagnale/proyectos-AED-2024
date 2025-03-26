from Envio import Envio
def cargar_manualmente(): #Cargar manualmete

    cp= input('codigo postal:')
    direccion= input('Direccion:')
    print('Tipos de envio : \n0-Carta simple hasta 20g\t1-Carta simple de 20g a 150g\t2-Carta simple de 150g a 500g\t3-Carta certificada hasta 150g\t4-Carta certificada desde 150g\t5-Carta expresa hasta 150g\t6-Carta expresa desde 150g  ')
    tipo = int(input('Selecciona el tipo de envio: '))
    while tipo > 6 or tipo < 0:
        tipo = int(input(' Seleccionar una opcion valida, \ntipo de envio:'))
    else:
        tipo = int(tipo)
    print('Medios de pago:\n1-Efectivo\t2-trajeta ')
    pago = int(input('Selecciona medido de pago: '))
    while pago > 2 or pago < 1:
        pago = int(input(' Seleccionar una opcion valida, \npago:'))
    else:
        pago = int(pago)
    nuevo = Envio(cp,direccion,tipo,pago)

    return nuevo

def leer(): #leer desde el archivo .txt
   archivo = open('envios-tp3.txt','r')
   envios = []
   contador = 0
   while True:
       line = archivo.readline()
       largo= len(line)
       if contador == 0:  # Ingresa y coloca el tipo de control
           control = type_of_controll(line)
       if contador !=0 and largo == 32:
         cp=codigo_postal(line)
         #direccion= direccion_espacios(line)
         direccion= line[9:28]
         tipo = line[29]
         pago = line[30]
         nuevo = Envio(cp,direccion,tipo,pago)
         envios.append(nuevo)
       elif line == '':
           break
       else:
           contador +=1

   archivo.close()
   return envios, control

#funciones recuperadas del tp anterior
def codigo_postal(line):
    cp = ''
    aux = line[:9]
    for i in aux:
        if i != ' ':
            cp += i
    return cp

def direccion_espacios(line):
    aux = line[9:28]
    dd= ''
    contador = 0
    for i in aux:
        if i ==".":
            contador = 1
        elif contador == 0:
            dd += i
    return dd



def mostrar(vector):
    for x in vector:
        print(x)


def shell_short(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y < v[k]:
                v[k + h] = v[k]
                k -= h
            v[k + h] = y
        h //= 3
    return v

def convertir_str(v):
    return [str(i) for i in v]

def destination_adress(line):
    dd = ''

    for i in line:
        if i != " " :
            dd += i
    return dd

def buscar_direccion(vector, direccion_b, tipoenvio_b):
        direccion_c = destination_adress(direccion_b)
        for p in vector:
            aux = destination_adress(p.direccion)
            if aux == direccion_c and p.tipo == tipoenvio_b:
                return p
        return None
def buscar_cp(array_envios, buscado_cp):

    for p in array_envios:
        if p.cp.strip() == buscado_cp:
            if p.pago == '1':
                p.pago = '2'
            elif p.pago == '2':
                p.pago = '1'
            return p
    return None

def type_of_controll(line):
    vc = False
    hc = False
    for i in line:
        if i == "H":
            vc = True
        else:
            if i == 'C' and vc == True:
                hc = True
            vc = False
    if hc == True:  # Hard control
        control = 'Hard Control'


    else:  # Soft control
        control = 'Soft Control'

    return control

def dos_mayus(dd):  # Detecta si hay dos mayus
    primer_mayuscula = False
    bandera_mayus = False

    for m in dd:
        if primer_mayuscula and m.isupper():
            bandera_mayus = True
            primer_mayuscula = False
            break
        elif m.isupper():
            primer_mayuscula = True
        else:
            primer_mayuscula = False

    return bandera_mayus
def es_separador(c):
    return c in " ."


def es_digito(c):
    return c.isdigit()


def palabra_compuesta_digito(line):
    es_digit = False

    for c in line:
        if es_separador(c):
            if es_digit:
                return True
            es_digit = False
        elif es_digito(c):
            es_digit = True
        else:
            es_digit = False
    return False

def letras_digitos(dd):
    word = ""
    other = ""
    for d in dd:
        if d.isdigit() or ('a' <= d <= 'z') or ('A' <= d <= 'Z')or d == '.' or d == ' ':
            word += d
        else:
            other += d

    if other == "":
        valid = True
    else:
        valid = False
    return valid

def validar_hardcontrol(array):

    vector_conteo = [0]*7

    for i in array:

        bandera_direccion = letras_digitos(i.direccion) #TRUE

        bandera_mayuscula = dos_mayus(i.direccion) #FALSE

        bandera_palabrac = palabra_compuesta_digito(i.direccion) #TRUE

        if bandera_mayuscula == False and bandera_palabrac and bandera_direccion:
            vector_conteo[int(i.tipo)] += 1

    return vector_conteo




def validar_softcontrol(array):

    vector_conteo = [0]*7

    for i in array:
            vector_conteo[int(i.tipo)] += 1
    return vector_conteo


def procedencia_cp(cp):
    global provincia
    n = len(cp)
    if n == 8: #ARGENTINA
        if 'A' <= cp[0] <= 'Z' and cp[0] != 'I' and cp[0] != 'O':
            if '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                if 'A' <= cp[5] <= 'Z' and 'A' <= cp[6] <= 'Z' and 'A' <= cp[7] <= 'Z':
                    destino = 'Argentina'
                else:
                    destino = 'Otro'
            else:
                destino = 'Otro'
        else:
            destino = 'Otro'
    else:
        if n == 4:  #BOLIVIA
            if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                destino = 'Bolivia'
            else:
                destino = 'Otro'

        else:
            if n == 9: # BRASIL
                if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                    if '0' <= cp[4] <= '9' and cp[5] == '-':
                        if '0' <= cp[6] <= '9' and '0' <= cp[7] <= '9' and '0' <= cp[8] <= '9':
                            destino = 'Brasil'
                        else:
                            destino = 'Otro'
                    else:
                        destino = 'Otro'
                else:
                    destino = 'Otro'

            else:
                if n == 7: #CHILE
                    if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                        if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9' and '0' <= cp[6] <= '9':
                            destino = 'Chile'
                        else:
                            destino = 'Otro'
                    else:
                        destino = 'Otro'
                else:
                    if n == 6: #PARAGUAY
                        if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                            if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9':
                                destino = 'Paraguay'
                            else:
                                destino = 'Otro'
                        else:
                            destino = 'Otro'

                    else:
                        if n == 5: #URUGUAY
                            if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9':
                                if '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                                    destino = 'Uruguay'
                                else:
                                    destino = 'Otro'
                            else:
                                destino = 'Otro'
                        else:
                            destino = 'Otro'


    if destino == 'Argentina':  # DETERMINAR PROVINCIAS
        p = cp[0]
        if p == 'A':
            provincia = 'Salta'
        elif p == 'B':
            provincia = 'Buenos Aires'
        elif p == 'C':
            provincia = 'Ciudad Autónoma de Buenos Aires'
        elif p == 'D':
            provincia = 'San Luis'
        elif p == 'E':
            provincia = 'Entre Ríos'
        elif p == 'F':
            provincia = 'La Rioja'
        elif p == 'G':
            provincia = 'Santiago del Estero'
        elif p == 'H':
            provincia = 'Chaco'
        elif p == 'J':
            provincia = 'San Juan'
        elif p == 'K':
            provincia = 'Catamarca'
        elif p == 'L':
            provincia = 'La Pampa'
        elif p == 'M':
            provincia = 'Mendoza'
        elif p == 'N':
            provincia = 'Misiones'
        elif p == 'P':
            provincia = 'Formosa'
        elif p == 'Q':
            provincia = 'Neuquén'
        elif p == 'R':
            provincia = 'Río Negro'
        elif p == 'S':
            provincia = 'Santa Fe'
        elif p == 'T':
            provincia = 'Tucumán'
        elif p == 'U':
            provincia = 'Chubut'
        elif p == 'V':
            provincia = 'Tierra del Fuego'
        elif p == 'W':
            provincia = 'Corrientes'
        elif p == 'X':
            provincia = 'Córdoba'
        elif p == 'Y':
            provincia = 'Jujuy'
        elif p == 'Z':
            provincia = 'Santa Cruz'
        else:
            provincia = 'Otro'

    else:
        provincia = "Otro"

    return destino

def calcular_importe(control, array):
    array_importes = [0.0] * 7

    for i in range(len(array)):

        if control == 'Soft Control':

            cp = array[i].cp
            cp_pais = procedencia_cp(cp)
            importe__carta = importe_carta(array[i].tipo)
            importe__pais = importe_pais(cp_pais, cp, importe__carta,array[i].pago)
            array_importes[int(array[i].tipo)] += importe__pais

        else:
            if control == 'Hard Control':


                    bandera_direccion = letras_digitos(array[i].direccion)  # TRUE

                    bandera_mayuscula = dos_mayus(array[i].direccion)  # FALSE

                    bandera_palabrac = palabra_compuesta_digito(array[i].direccion)  # TRUE

                    if bandera_mayuscula == False and bandera_palabrac and bandera_direccion:
                        cp = array[i].cp
                        cp_pais = procedencia_cp(cp)
                        importe__carta = importe_carta(array[i].tipo)
                        importe__pais = importe_pais(cp_pais, cp, importe__carta, array[i].pago)
                        array_importes[int(array[i].tipo)] += importe__pais

    return array_importes

def importe_carta(tipo):
    tipo = int(tipo)
    precio = 0

    if (tipo == 0):
        precio = 1100

    elif (tipo == 1):
        precio = 1800

    elif (tipo == 2):
        precio = 2450

    elif (tipo == 3):
        precio = 8300

    elif (tipo == 4):
        precio = 10900

    elif (tipo == 5):
        precio = 14300

    elif (tipo == 6):
        precio = 17900

    precio_truncado = int(precio)
    return precio_truncado

def importe_pais(cp_pais, cp, importe_carta, pago):
    pago = int(pago)
    aux = importe_carta
    if cp_pais == 'Brasil':
        codigo = int(cp[0])
        if codigo == 8 or codigo == 9:
            aux *= 1.2
        elif codigo == 0 or codigo == 1 or codigo == 2 or codigo == 3:
            aux *= 1.25
        elif codigo == 4 or codigo == 5 or codigo == 6 or codigo == 7:
            aux *= 1.30
    elif cp_pais == 'Argentina':
        aux *= 1
    elif cp_pais == 'Chile':
        aux *= 1.25
    elif cp_pais == 'Paraguay':
        aux *= 1.2
    elif cp_pais == 'Uruguay':
        if int(cp[0]) == 1:
            aux *= 1.2
        else:
            aux *= 1.25
    elif cp_pais == 'Bolivia':
        aux *= 1.2
    elif cp_pais == 'Otro':
        aux *= 1.5

    valor_truncado = int(aux)
    if pago == 1:
        valor_truncado *= 0.9
        valor_truncado = int(valor_truncado)

    return valor_truncado
def buscar_mayor(vc):
    mayor = None
    indice = None

    for i in range(len(vc)):

        if mayor is None:
            mayor = vc[i]
            indice = i

        elif vc[i] > mayor:
            mayor = vc[i]
            indice = i

    return mayor, indice

def calcular_total_importe(vector):
    importe = 0
    for i in range(len(vector)):
        importe += vector[i]
    return importe


def calcular_porcentaje(mayor,suma):
    return (mayor/suma)*100


def contar_menores_promedio(array,promedio):
        contador = 0
        for i in range(len(array)):
            if array[i] < promedio:
                contador += 1
        return contador


def importes_envios(array):
    array_importes = [0.0] * len(array)

    for i in range(len(array)):

            cp = array[i].cp
            cp_pais = procedencia_cp(cp)
            importe__carta = importe_carta(array[i].tipo)
            importe__pais = importe_pais(cp_pais, cp, importe__carta, array[i].pago)
            array_importes[i] += importe__pais  # Usar el índice i para actualizar array_importes

    return array_importes


def principal(): #MENU
   opcion = -1
   array_envios = []
   control = 'Hard Control'
   control_nuevo = 'Hard Control'
   bandera_7 = False
   while opcion != 0:
       print('Menu de opciones')
       print('1 - Cargar los envios del archivo txt')
       print('2 - Cargar un envio manualmente')
       print('3 - Mostrar los envios ordenados por codigo postal')
       print('4 - buscar Envios de envio por direccion y tipo')
       print('5 - Cambiar metodo de pago')
       print('6 - Envios con direccion valida')
       print('7 - Mostrar total recaudado por cada envio')
       print('8 - Tipo de envio con mayor importe final')
       print('9 - Promedio y porcentaje sobre el total de envios')
       print('0 - Salir')


       opcion = int(input('Ingrese la opcion: '))


       if opcion == 1:
           continuar = int(input('Se van a perder los datos del envio anterior.  \n 1 - Si \n 2 - no \nDesdea continuar:'))
           while continuar != 1 and continuar != 2:
               continuar = int(input('la opcion elegida no es correcta, selecciona 1 para continuar o 2 para continuar con el envio actual: '))
           else:
               if continuar == 1:
                   array_envios, control_nuevo = leer()
               else:
                   principal()
       elif opcion == 2:  # Carga manulamente
                array_envios.append(cargar_manualmente())

       elif opcion == 3:
           if array_envios == []:
               print('La app no tiene datos, seleccione otra opcion\n')
               principal()
           else:
               shell_short(array_envios)
               registros = int(input('Ingrese la cantidad de registros que desea ver, use 0 para ver todos los registros:  '))
               while registros < 0:
                   registros = int(
                       input('Ingrese la cantidad de registros que desea ver, use 0 para ver todos los registros:  '))
               else:
                   registros = int(registros)

               if registros == 0:
                   for i in array_envios:
                       print(procedencia_cp(i.cp),'-',i)
               else:
                   for i in range(registros):
                       print(procedencia_cp(array_envios[i].cp),'-',array_envios[i])

       elif opcion == 4:
           if array_envios == []:
               print('La app no tiene datos, seleccione otra opcion\n')
               principal()
           else:
               tipoenvio_buscar = input('Ingrese el tipo de envio a buscar: ')
               direccion_buscar = input("Ingrese la direccion a buscar: ")
               encontrado = buscar_direccion(array_envios, direccion_buscar, tipoenvio_buscar)

               if encontrado:
                   print(encontrado)
               else:
                   print("\nNo se encontro")


       elif opcion == 5:

           if array_envios == []:
               print('La app no tiene datos, seleccione otra opcion\n')
               principal()
           else:
               buscado_cp= input('Ingrese cp que desea buscar:  ')
               buscado_cp = buscado_cp.strip()
               solicitado_cp = buscar_cp(array_envios, buscado_cp)

               if solicitado_cp == None:

                   print('No se encontró el codigo postal solicitado')

               else:

                   print(solicitado_cp)

       elif opcion == 6:
           tipo = -1
           if array_envios == []:
               print('La app no tiene datos, seleccione otra opcion\n')
               principal()
           else:
                if control_nuevo == 'Hard Control':
                    vector_conteo = validar_hardcontrol(array_envios)
                    for i in vector_conteo:
                        tipo += 1
                        print(f'tipo de envio {tipo} - {i}')
                else:
                    vector_conteo = validar_softcontrol(array_envios)
                    for i in vector_conteo:
                        tipo += 1
                        print(f'tipo de envio {tipo} - {i}')


       elif opcion == 7:
           if array_envios == []:
               print('La app no tiene datos, seleccione otra opcion\n')
               principal()
           else:
             bandera_7 = True
             tipo = -1
             array_importes_total = calcular_importe(control_nuevo, array_envios)
             for i in array_importes_total:
                 tipo += 1
                 print(f'tipo de envio {tipo} - $ {i}')
       elif opcion == 8:
             if bandera_7 == False:
                 print('La app no tiene datos, seleccione otra opcion\n')
                 principal()
             else:
                 mayor, indice = buscar_mayor(array_importes_total)
                 print('El tipo de envio con mayor importe es el - ',indice)
                 importe_total = calcular_total_importe(array_importes_total)
                 porcentaje_mayor_envio = calcular_porcentaje(mayor, importe_total)
                 print(f"{porcentaje_mayor_envio:.2f}%")

       elif opcion == 9:
           if array_envios == []:
               print('La app no tiene datos, seleccione otra opcion\n')
               principal()
           else:
               array_importes_total = calcular_importe('Soft Control', array_envios)
               importe_total = calcular_total_importe(array_importes_total)
               envios = len(array_envios)
               promedio = importe_total/envios

               importes = importes_envios(array_envios)
               menores = contar_menores_promedio(importes,promedio)

               print('promedio',promedio,'Envios que tuvieron en importe menor',menores)

# Crear el menu primero
if __name__ == '__main__':
   principal()
