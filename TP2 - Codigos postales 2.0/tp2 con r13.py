# FUNCIONES
def Type_of_controll(line):
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


def Destination_adress(line):
    dd = ''
    aux = line[9:28]  # Extrae los caracteres correspondientes  a la direcciond e destino
    for i in aux:
        if i != " " and i != ".":
            dd += i
    return dd


def Letras_digitos(dd):
    word = ""
    other = ""
    for d in dd:
        # Puse isdigit para safar porque no me funca ('0'<= d <='9')
        if d.isdigit() or ('a' <= d <= 'z') or ('A' <= d <= 'Z'):
            word += d
        else:
            other += d

    if other == "":
        valid = True
    else:
        valid = False
    return valid


def Dos_mayus(dd):  # Detecta si hay dos mayus
    first_mayus = False
    mm = False
    for m in dd:
        if 'A' <= m <= 'Z':
            if first_mayus == True:
                mm = True
                break
            first_mayus = True
        else:
            first_mayus = False
    return mm


def Calcular_importe(control, line):
    if control == 'Soft Control':

        cp = Codigo_postal(line)  # cp = codigo postal
        cp_pais = Procedencia_cp(cp)
        importe_carta = Importe_carta(line)
        importe_pais = Importe_pais(cp_pais, cp, importe_carta)

    else:
        if validHC == True:
            cp = Codigo_postal(line)
            cp_pais = Procedencia_cp(cp)
            importe_carta = Importe_carta(line)
            importe_pais = Importe_pais(cp_pais, cp, importe_carta)
        else:
            cp = Codigo_postal(line)
            importe_pais = 0

    return importe_pais, cp


def Codigo_postal(line):
    cp = ''
    aux = line[:9]
    for i in aux:
        if i != ' ':
            cp += i  # cp = codigo postal

    return cp


def Procedencia_cp(cp):
    destino = ''

    if len(cp) == 9:  # Brasil
        if cp[0] != '0' and cp[0] != '1' and cp[0] != '2' and cp[0] != '3' and cp[0] != '4' and cp[0] != '5' and cp[
            0] != '6' and cp[0] != '7' and cp[0] != '8' and cp[0] != '9':
            destino = 'Otro'
        elif cp[1] != '0' and cp[1] != '1' and cp[1] != '2' and cp[1] != '3' and cp[1] != '4' and cp[1] != '5' and cp[
            1] != '6' and cp[1] != '7' and cp[1] != '8' and cp[1] != '9':
            destino = 'Otro'
        elif cp[2] != '0' and cp[2] != '1' and cp[2] != '2' and cp[2] != '3' and cp[2] != '4' and cp[2] != '5' and cp[
            2] != '6' and cp[2] != '7' and cp[2] != '8' and cp[2] != '9':
            destino = 'Otro'
        elif cp[3] != '0' and cp[3] != '1' and cp[3] != '2' and cp[3] != '3' and cp[3] != '4' and cp[3] != '5' and cp[
            3] != '6' and cp[3] != '7' and cp[3] != '8' and cp[3] != '9':
            destino = 'Otro'
        elif cp[4] != '0' and cp[4] != '1' and cp[4] != '2' and cp[4] != '3' and cp[4] != '4' and cp[4] != '5' and cp[
            4] != '6' and cp[4] != '7' and cp[4] != '8' and cp[4] != '9':
            destino = 'Otro'
        elif cp[5] != '-':
            destino = 'Otro'
        elif cp[6] != '0' and cp[6] != '1' and cp[6] != '2' and cp[6] != '3' and cp[6] != '4' and cp[6] != '5' and cp[
            6] != '6' and cp[6] != '7' and cp[6] != '8' and cp[6] != '9':
            destino = 'Otro'
        elif cp[7] != '0' and cp[7] != '1' and cp[7] != '2' and cp[7] != '3' and cp[7] != '4' and cp[7] != '5' and cp[
            7] != '6' and cp[7] != '7' and cp[7] != '8' and cp[7] != '9':
            destino = 'Otro'
        elif cp[8] != '0' and cp[8] != '1' and cp[8] != '2' and cp[8] != '3' and cp[8] != '4' and cp[8] != '5' and cp[
            8] != '6' and cp[8] != '7' and cp[8] != '8' and cp[8] != '9':
            destino = 'Otro'
        else:
            destino = 'Brasil'
        '''
        brasil = True

        for i in cp:
            if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i != '-':
                brasil = False
            elif cp[5] != '-':
                brasil = False
        if brasil == True:
            destino = 'Brasil'
        else:
            destino = 'Otro'
        '''

    elif len(cp) == 8:  # Argentina
        argentina = True
        count_cp = 0
        for c in range(len(cp)):
            i = cp[c]

            if c == 0 or c >= 5:

                caracter = ord(cp[c])

                if (caracter < 64 or caracter > 122) or (caracter > 91 and caracter < 97) or (
                        caracter == 105 or caracter == 73 or caracter == 164 or caracter == 165 or caracter == 79 or caracter == 111):
                    Argentina = False
            else:

                i = cp[c]

                if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':
                    Argentina = False
        if cp[0] == 'A':
            provincia = "Salta"
        elif cp[0] == 'B':
            provincia = "Provincia de Buenos Aires"
        elif cp[0] == 'C':
            provincia = 'Ciudad Autónoma de Buenos Aires'
        elif cp[0] == 'D':
            provincia = 'San Luis'
        elif cp[0] == 'E':
            provincia = 'Entre Ríos'
        elif cp[0] == 'F':
            provincia = 'La Rioja'
        elif cp[0] == 'G':
            provincia = 'Santiago del Estero'
        elif cp[0] == 'H':
            provincia = 'Chaco'
        elif cp[0] == 'J':
            provincia = 'San Juan'
        elif cp[0] == 'K':
            provincia = 'Catamarca'
        elif cp[0] == 'L':
            provincia = 'La Pampa'
        elif cp[0] == 'M':
            provincia = 'Mendoza'
        elif cp[0] == 'N':
            provincia = 'Misiones'
        elif cp[0] == 'P':
            provincia = 'Formosa'
        elif cp[0] == 'Q':
            provincia = 'Neuquén'
        elif cp[0] == 'R':
            provincia = 'Rio Negro'
        elif cp[0] == 'S':
            provincia = 'Santa Fe'
        elif cp[0] == 'T':
            provincia = 'Tucuman'
        elif cp[0] == 'U':
            provincia = 'Chubut'
        elif cp[0] == 'V':
            provincia = 'Tierra del Fuego'
        elif cp[0] == 'W':
            provincia = 'Corrientes'
        elif cp[0] == 'X':
            provincia = 'Cordoba'
        elif cp[0] == 'Y':
            provincia = 'Jujuy'
        elif cp[0] == 'Z':
            provincia = 'Santa Cruz'
        else:
            destino = 'Otro'
            argentina = False

        if argentina == True:
            destino = 'Argentina'
        else:
            destino = 'Otro'

    elif len(cp) == 7:  # Chile
        if cp[0] != '0' and cp[0] != '1' and cp[0] != '2' and cp[0] != '3' and cp[0] != '4' and cp[0] != '5' and cp[
            0] != '6' and cp[0] != '7' and cp[0] != '8' and cp[0] != '9':
            destino = 'Otro'
        elif cp[1] != '0' and cp[1] != '1' and cp[1] != '2' and cp[1] != '3' and cp[1] != '4' and cp[1] != '5' and cp[
            1] != '6' and cp[1] != '7' and cp[1] != '8' and cp[1] != '9':
            destino = 'Otro'
        elif cp[2] != '0' and cp[2] != '1' and cp[2] != '2' and cp[2] != '3' and cp[2] != '4' and cp[2] != '5' and cp[
            2] != '6' and cp[2] != '7' and cp[2] != '8' and cp[2] != '9':
            destino = 'Otro'
        elif cp[3] != '0' and cp[3] != '1' and cp[3] != '2' and cp[3] != '3' and cp[3] != '4' and cp[3] != '5' and cp[
            3] != '6' and cp[3] != '7' and cp[3] != '8' and cp[3] != '9':
            destino = 'Otro'
        elif cp[4] != '0' and cp[4] != '1' and cp[4] != '2' and cp[4] != '3' and cp[4] != '4' and cp[4] != '5' and cp[
            4] != '6' and cp[4] != '7' and cp[4] != '8' and cp[4] != '9':
            destino = 'Otro'
        elif cp[5] != '0' and cp[5] != '1' and cp[5] != '2' and cp[5] != '3' and cp[5] != '4' and cp[5] != '5' and cp[
            5] != '6' and cp[5] != '7' and cp[5] != '8' and cp[5] != '9':
            destino = 'Otro'
        elif cp[6] != '0' and cp[6] != '1' and cp[6] != '2' and cp[6] != '3' and cp[6] != '4' and cp[6] != '5' and cp[
            6] != '6' and cp[6] != '7' and cp[6] != '8' and cp[6] != '9':
            destino = 'Otro'
        else:
            destino = 'Chile'
    # chile = True
    #   for i in cp:
    #      if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':
    #         chile = False
    # if chile == True:
    #   destino = 'Chile'
    # else:
    #   destino = 'Otro'

    elif len(cp) == 6:  # Paraguay
        if cp[0] != '0' and cp[0] != '1' and cp[0] != '2' and cp[0] != '3' and cp[0] != '4' and cp[0] != '5' and cp[
            0] != '6' and cp[0] != '7' and cp[0] != '8' and cp[0] != '9':
            destino = 'Otro'
        elif cp[1] != '0' and cp[1] != '1' and cp[1] != '2' and cp[1] != '3' and cp[1] != '4' and cp[1] != '5' and cp[
            1] != '6' and cp[1] != '7' and cp[1] != '8' and cp[1] != '9':
            destino = 'Otro'
        elif cp[2] != '0' and cp[2] != '1' and cp[2] != '2' and cp[2] != '3' and cp[2] != '4' and cp[2] != '5' and cp[
            2] != '6' and cp[2] != '7' and cp[2] != '8' and cp[2] != '9':
            destino = 'Otro'
        elif cp[3] != '0' and cp[3] != '1' and cp[3] != '2' and cp[3] != '3' and cp[3] != '4' and cp[3] != '5' and cp[
            3] != '6' and cp[3] != '7' and cp[3] != '8' and cp[3] != '9':
            destino = 'Otro'
        elif cp[4] != '0' and cp[4] != '1' and cp[4] != '2' and cp[4] != '3' and cp[4] != '4' and cp[4] != '5' and cp[
            4] != '6' and cp[4] != '7' and cp[4] != '8' and cp[4] != '9':
            destino = 'Otro'
        elif cp[5] != '0' and cp[5] != '1' and cp[5] != '2' and cp[5] != '3' and cp[5] != '4' and cp[5] != '5' and cp[
            5] != '6' and cp[5] != '7' and cp[5] != '8' and cp[5] != '9':
            destino = 'Otro'
        else:
            destino = 'Paraguay'
    # paraguay = True
    # for i in cp:
    #   if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':
    #      paraguay = False
    # if  paraguay == True:
    #   destino = 'Paraguay'
    # else:
    #   destino = 'Otro'

    elif len(cp) == 5:  # Uruguay
        if cp[0] != '0' and cp[0] != '1' and cp[0] != '2' and cp[0] != '3' and cp[0] != '4' and cp[0] != '5' and cp[
            0] != '6' and cp[0] != '7' and cp[0] != '8' and cp[0] != '9':
            destino = 'Otro'
        elif cp[1] != '0' and cp[1] != '1' and cp[1] != '2' and cp[1] != '3' and cp[1] != '4' and cp[1] != '5' and cp[
            1] != '6' and cp[1] != '7' and cp[1] != '8' and cp[1] != '9':
            destino = 'Otro'
        elif cp[2] != '0' and cp[2] != '1' and cp[2] != '2' and cp[2] != '3' and cp[2] != '4' and cp[2] != '5' and cp[
            2] != '6' and cp[2] != '7' and cp[2] != '8' and cp[2] != '9':
            destino = 'Otro'
        elif cp[3] != '0' and cp[3] != '1' and cp[3] != '2' and cp[3] != '3' and cp[3] != '4' and cp[3] != '5' and cp[
            3] != '6' and cp[3] != '7' and cp[3] != '8' and cp[3] != '9':
            destino = 'Otro'
        elif cp[4] != '0' and cp[4] != '1' and cp[4] != '2' and cp[4] != '3' and cp[4] != '4' and cp[4] != '5' and cp[
            4] != '6' and cp[4] != '7' and cp[4] != '8' and cp[4] != '9':
            destino = 'Otro'
        else:
            destino = 'Uruguay'
    #  uruguay = True
    #  for i in cp:
    #      if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':
    #         uruguay = False
    # if  uruguay == True:
    #    destino = 'Uruguay'
    # else:
    #    destino = 'Otro'

    elif len(cp) == 4:  # Bolivia
        if cp[0] != '0' and cp[0] != '1' and cp[0] != '2' and cp[0] != '3' and cp[0] != '4' and cp[0] != '5' and cp[
            0] != '6' and cp[0] != '7' and cp[0] != '8' and cp[0] != '9':
            destino = 'Otro'
        elif cp[1] != '0' and cp[1] != '1' and cp[1] != '2' and cp[1] != '3' and cp[1] != '4' and cp[1] != '5' and cp[
            1] != '6' and cp[1] != '7' and cp[1] != '8' and cp[1] != '9':
            destino = 'Otro'
        elif cp[2] != '0' and cp[2] != '1' and cp[2] != '2' and cp[2] != '3' and cp[2] != '4' and cp[2] != '5' and cp[
            2] != '6' and cp[2] != '7' and cp[2] != '8' and cp[2] != '9':
            destino = 'Otro'
        elif cp[3] != '0' and cp[3] != '1' and cp[3] != '2' and cp[3] != '3' and cp[3] != '4' and cp[3] != '5' and cp[
            3] != '6' and cp[3] != '7' and cp[3] != '8' and cp[3] != '9':
            destino = 'Otro'
        else:
            destino = 'Bolivia'

    # bolivia = True
    # for i in cp:
    #    if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':
    #       bolivia = False
    # if  bolivia == True:
    #   destino = 'Bolivia'
    # else:
    #   destino = 'Otro'

    return destino


def Importe_carta(line):
    tipo = int(line[29])
    pago = int(line[30])
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

    if (pago == 1):
        precio *= 0.9

    precio_truncado = int(precio)

    return precio_truncado


def Importe_pais(cp_pais, cp, importe_carta):
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

    return valor_truncado


def Contador_cartas(line, control, validHC):
    carta_simple = False
    carta_certificada = False
    carta_expresa = False
    tipo = int(line[29])
    if control == 'Soft Control':
        if tipo == 0 or tipo == 1 or tipo == 2:
            carta_simple = True
        elif tipo == 3 or tipo == 4:
            carta_certificada = True
        elif tipo == 5 or tipo == 6:
            carta_expresa = True
    if control == 'Hard Control' and validHC == True:
        if tipo == 0 or tipo == 1 or tipo == 2:
            carta_simple = True
        elif tipo == 3 or tipo == 4:
            carta_certificada = True
        elif tipo == 5 or tipo == 6:
            carta_expresa = True

    return carta_simple, carta_certificada, carta_expresa


def Carta_mas_enviada(count_s, count_c, count_e):
    a = count_s
    b = count_c
    c = count_e
    carta_may = ' '

    if a > b:
        aux = a
    else:
        aux = b
    if aux > c:
        may = aux
    else:
        may = c

    if may == count_s:
        carta_may = "Carta Simple"
    elif may == count_c:
        carta_may = "Carta Certificada"
    elif may == count_e:
        carta_may = "Carta Expresa"

    return carta_may


def Codigo_primer_envio(line):
    cp_1 = ''
    aux = line[:9]
    for i in aux:
        if i != ' ':
            cp_1 += i  # cp = codigo postal

    return cp_1


def Repeticion_cp_1(cp_1, cp):
    rep_cp1 = False
    if cp_1 == cp:
        rep_cp1 = True
    return rep_cp1

##funciones r13
def envios_exterior(control, validHC, pais):
    global total_envios_exterior  # cambia el valor de mi variable global
    if (control == 'Hard Control' and validHC) or control == 'Soft Control':
        if pais != 'Argentina':
            total_envios_exterior += 1


def porcentaje (total_envios_exterior,total_envios):
    if total_envios!= 0:
        porcentaje = (total_envios_exterior * 100) / total_envios
    else:
        porcentaje = 0
    porcentaje = int(porcentaje)
    return porcentaje

# Codigo principal


# archivo = open("../envios25.txt", "r")
archivo = open('C:/Users/luciana.briones/Downloads/envios25.txt',
               'r')  # hay que cambiar la ruta segun donde tengan el archivo

# Variables
control = ''
first_line = False  # bandera para detectar unicamente la primer linea sin que perjudique al codigo
cde_valid_SC = 0
count_valid_hc = 0
count_invalid_hc = 0
imp_acu_total = 0
ccs = 0
ccc = 0
cce = 0
second_line = False  # esto es para sacar el codigo postal del primer envio
cant_primer_cp = 0
validHC = False  # para comprobar si un envio es valido, asi trabajarlo en las funciones
cedvalid = 0
cedinvalid = 0
primer_cp = 0
cde_invalid_SC = 0
tipo_mayor = ''
#r13
total_envios_exterior = 0
bandera_registros = False
total_envios = 0

while True:
    line = archivo.readline()  # lee por linea

    # metodo de corte del while
    if line == '':
        break

    # de aca sale r1 y r2 SC
    if first_line == False:
        control = Type_of_controll(line)
        first_line = True
        bandera_registros = True
        if control == 'Soft Control':
            cde_invalid_SC = 0  # cde = "cantidad de envios invalidos Soft Control"
        continue
    # --------
    if bandera_registros:  #cuento cantidad de envios totales, independientemente si son validos o no en HC
        total_envios +=1

    # de aca sale r3 SC
    if control == 'Soft Control':
        for i in line:
            if i == ('\n'):
                cde_valid_SC += 1
    # --------------

    # aca sale r2 y r3 HC
    else:
        dd = Destination_adress(line)  # dd = "direccion de destino"
        ld = Letras_digitos(dd)  # ld = letras y digitos
        mm = Dos_mayus(dd)  # mm = mayus mayus

        # FALTA HACER ESTA VALIDACION pero el programa corre bien igual
        # pc = Palabra_compuesta_digito(dd) #pc = palabra compuesta

        if ld == True and mm == False:
            count_valid_hc += 1
            validHC = True
        else:
            count_invalid_hc += 1
            validHC = False

        # ......

    # ---------------

    # de aca sale r4
    aux, cp = Calcular_importe(control, line)  # traigo el codigo postal para usarlo en r10
    imp_acu_total += aux

    # ----

    # de aca sale r5 - r6 -r7
    carta_simple, carta_certificada, carta_expresa = Contador_cartas(line, control, validHC)
    if carta_simple == True:
        ccs += 1
    elif carta_certificada == True:
        ccc += 1
    elif carta_expresa == True:
        cce += 1
    # --------

    # de aca sale r8
    tipo_mayor = Carta_mas_enviada(ccs, ccc, cce)
    # --------

    # de aca sale r9
    if second_line == False:
        primer_cp = Codigo_primer_envio(line)
        second_line = True
    # --------

    # de aca sale r10
    cp_1_rep = Repeticion_cp_1(primer_cp, cp)
    if cp_1_rep == True:
        cant_primer_cp += 1
    # --------
    # r13
    envios_exterior(control, validHC, Procedencia_cp(cp))

archivo.close()

if control == "Soft Control":
    cedvalid = cde_valid_SC
else:
    cedvalid = count_valid_hc
if control == "Soft Control":
    cedinvalid = cde_invalid_SC
else:
    cedinvalid = count_invalid_hc

########################
pe = porcentaje(total_envios_exterior,total_envios)

# Salidas segun la estructura del ejercicio

print('  (r1) - Tipo de control de direcciones:', control)
print('  (r2) - Cantidad de envios con direccion valida:', cedvalid)
print('  (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
print('  (r4) - Total acumulado de importes finales:', imp_acu_total)
print('  (r5) - Cantidad de cartas simples:', ccs)
print('  (r6) - Cantidad de cartas certificadas:', ccc)
print('  (r7) - Cantidad de cartas expresas:', cce)
print('  (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
print('  (r9) - Codigo postal del primer envio del archivo:', primer_cp)
print(' (r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
# print(' (r11) - Importe menor pagado por envios a Brasil:', "-") #FALTA HACER
# print(' (r12) - Codigo postal del envio a Brasil con importe menor:', "-") #FALTA HACER
print(' (r13) - Porcentaje de envios al exterior sobre el total:', pe)
# print(' (r14) - Importe final promedio de los envios a Buenos Aires', "-" ) #FALTA HACER


########################
