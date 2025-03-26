#Sistema Simple de Gestión de Envíos por Correo

#Ingreso de datos

cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))


internacional = True
recargo1= 1.20
recargo2= 1.25
recargo3= 1.30
recargo4= 1.50


if len(cp) == 8: #ARG
    internacional = False
    #Tipo de envio
    #Provincia destino
elif len(cp) == '9': #BRASIL
    cp=int(cp)
    # Tipo de envio
    #regiones
    if cp[0] >=0 and cp[0] <= 3:
        recargo = recargo2
    elif cp[0] >=8 and cp[0] <= 9:
        recargo = recargo1
    elif cp[0] >=4 cp[0] <= 7:
        recargo = recargo3
elif len(cp) == 7: #CHILE
    recargo = recargo1
elif len(cp) == 6: #PARAGUAY
    recargo = recargo1
elif len(cp) == 5: #URUGUAY
    montevideo = False
    if cp[0] == 1 :
        montevideo == True
        recargo = recargo1
    else:
        recargo = recargo2
elif len(cp) == 4:#Bolibia
    recargo = recargo1
else:#OTROS PAISES
    recargo = recargo4



#Tipo de envio
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
    precio =