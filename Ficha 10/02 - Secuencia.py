s1 = False
s12 = False
divisible4 = 0
num_mayor = None
primer_num =0
rpn = 1
numeros = 0
ingresos = 0
csec = 0
anterior = 0
num = int(input("Ingrese un numero: "))
primer_num = num

while num > 0:

    num = int(input("Ingrese un numero: "))
    ingresos += 1
    if num % 4 == 0 and num != 0:
        divisible4 += 1
    if num_mayor == None:
        num_mayor = num
    else:
        if num > num_mayor:
            num_mayor = num
    if num == primer_num:
        rpn += 1

    # Secuencia 123

    if num == 1:
        s1 = True
        s12 = False
    else:
        if num == 2 and s1:
            s12 = True
        else:
            if num == 3 and s12:
                csec += 1
                print('secuencia ok')
            s12 = False
        s1 = False


print ('-'*40)

print ('Cantidad de numeros divisible 4 =', divisible4)
print ('Numero mayor =', num_mayor)
print ('Cantidad de veces que se ingreso ',primer_num,' el primer numero =', rpn)

print ('-'*40)

print ( 'Cantidad de veces que se repite la seccuencia =', csec)
print ('-'*40)
