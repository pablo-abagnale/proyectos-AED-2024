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

def direccion_espacios(line):
    aux = line[9:28]
    return aux

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

def palabra_compuesta_digito(solo_digitos, direccion):
    #print(dd)
    posicion = 0
    for c in direccion:
        if c == '.' or c == ' ':
            #al terminar palabra en la direccion
            if solo_digitos:
                return solo_digitos
            else:
                #print('la palabra no es unicamente de digitos')
                solo_digitos =True
        else:
            if not(c.isdigit()):
                solo_digitos = False
            posicion +=1
    return solo_digitos



def Calcular_importe(control, line):
    if control == 'Soft Control':

        cp = Codigo_postal(line)  # cp = codigo postal
        cp_pais = Procedencia_cp(cp)
        importe_carta = Importe_carta(line)
        importe_pais = Importe_pais(cp_pais, cp, importe_carta,line)

    else:
        if validHC == True:
            cp = Codigo_postal(line)
            cp_pais = Procedencia_cp(cp)
            importe_carta = Importe_carta(line)
            importe_pais = Importe_pais(cp_pais, cp, importe_carta,line)
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
    global provincia
    n = len(cp)
    if n == 8:
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
        # ¿es Bolivia?
        if n == 4:
            if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                destino = 'Bolivia'
            else:
                destino = 'Otro'

        else:
            # ¿es Brasil?
            if n == 9:
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
                # ¿es Chile?
                if n == 7:
                    if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                        if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9' and '0' <= cp[6] <= '9':
                            destino = 'Chile'
                        else:
                            destino = 'Otro'
                    else:
                        destino = 'Otro'
                else:
                    # ¿es Paraguay?
                    if n == 6:
                        if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9' and '0' <= cp[3] <= '9':
                            if '0' <= cp[4] <= '9' and '0' <= cp[5] <= '9':
                                destino = 'Paraguay'
                            else:
                                destino = 'Otro'
                        else:
                            destino = 'Otro'

                    else:
                        # ¿es Uruguay?
                        if n == 5:
                            if '0' <= cp[0] <= '9' and '0' <= cp[1] <= '9' and '0' <= cp[2] <= '9':
                                if '0' <= cp[3] <= '9' and '0' <= cp[4] <= '9':
                                    destino = 'Uruguay'
                                else:
                                    destino = 'Otro'
                            else:
                                destino = 'Otro'
                        else:
                            destino = 'Otro'


    # 2. Determinación de la provincia del lugar de destino.
    if destino == 'Argentina':
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


def Importe_carta(line):
    tipo = int(line[29])
    #pago = int(line[30])
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

   # print('pago', pago)

   # if (pago == 1):
   #     print('entre')
   #     print(precio)
   #     precio *= 0.9
   #     print(precio)

    precio_truncado = int(precio)
    return precio_truncado


def Importe_pais(cp_pais, cp, importe_carta, line):
    pago = int(line[30])
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
        valor_truncado *=0.9
        valor_truncado = int(valor_truncado)
    #return valor_truncado
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

#funcion r11 y r12
def envio_brasil(veri, menor_importe, importe, pais,cp):
    global menimp
    global mencp
    if pais == 'Brasil' and veri:
        if menor_importe is None or importe < menor_importe:
            menimp = importe
            mencp = cp

##funciones r13

def verificacion(control, validHC):
    return ((control == 'Hard Control' and validHC) or control == 'Soft Control')

def envios_exterior(verificacion, pais):
    if verificacion and pais != 'Argentina':
        return 1
    return 0


def porcentaje (total_envios_exterior,total_envios):
    if total_envios!= 0:
        porcentaje = (total_envios_exterior * 100) / total_envios
    else:
        porcentaje = 0
    porcentaje = int(porcentaje)
    return porcentaje

#r14
def monto_final_promedio_buenos_aires(verif,pais, cod_provincia,aux):
    if verif and pais == 'Argentina' and cod_provincia == 'Buenos Aires':
        return 1, aux
    return 0,0

def calcular_promedio(suma_total, cantidad_total):
    if cantidad_total != 0:
        promedio = suma_total / cantidad_total
    else:
        promedio = 0
    promedio = int(promedio)
    return promedio

#Codigo principal


archivo = open("c/../envios100SC.txt", "r")
#archivo = open('C:/Users/luciana.briones/PycharmProjects/runner_tp2/envios100SC.txt','r')  # hay que cambiar la ruta segun donde tengan el archivo

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
#r11
provincia = ''
menimp = None
importe_brasil_mas_bajo = 0
mencp = 0

#r13
total_envios_exterior = 0
bandera_registros = False
total_envios = 0

#r14
cant_envios_buenos_aires = 0
total_envios_buenos_aires = 0
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
        solo_digitos = True
        direccion= direccion_espacios(line)
        pc = palabra_compuesta_digito(solo_digitos,direccion) #pc = palabra compuesta


        if ld == True and mm == False and pc:
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

    #r11
    verificacion_linea = verificacion(control,validHC)
    pais = Procedencia_cp(cp)
    importe_brasil_mas_bajo = envio_brasil(verificacion_linea, menimp, aux, pais,cp)

    # r13
    total_envios_exterior += envios_exterior(verificacion_linea, pais) #calculo cant de envios al exterior

    #r14
    aux_cant_buenos_aires, aux_total_envios_buenos_aires = monto_final_promedio_buenos_aires(verificacion_linea,pais,provincia,aux)
    cant_envios_buenos_aires += aux_cant_buenos_aires
    total_envios_buenos_aires += aux_total_envios_buenos_aires

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

#r13 segunda parte
porc = porcentaje(total_envios_exterior,total_envios) #calculo porcentaje envios al exterior

#r14
prom = calcular_promedio(total_envios_buenos_aires, cant_envios_buenos_aires)


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
print(' (r11) - Importe menor pagado por envios a Brasil:',menimp)
print(' (r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
print(' (r13) - Porcentaje de envios al exterior sobre el total:', porc)
print(' (r14) - Importe final promedio de los envios a Buenos Aires:', prom)


########################
