cp = input("Ingrese el código postal del lugar de destino: ")

if len(cp) == 8:

    valor_ascii0 = ord(cp[0])
    valor_ascii5 = ord(cp[5])
    valor_ascii6 = ord(cp[6])
    valor_ascii7 = ord(cp[7])
#Primer caracter letra
    if (valor_ascii0 < 64 or valor_ascii0 > 122) or (valor_ascii0 > 91 and valor_ascii0 < 97):
        destino = 'Otro'
#Segundo caracter Numero
    elif cp[1] != '0' and cp[1] != '1' and cp[1] != '2' and cp[1] != '3' and cp[1] != '4' and cp[1] != '5' and cp[1] != '6' and cp[1] != '7' and cp[1] != '8' and cp[1] != '9':
        destino = 'Otro'
#Tercer caracter Numero
    elif cp[2] != '0' and cp[2] != '1' and cp[2] != '2' and cp[2] != '3' and cp[2] != '4' and cp[2] != '5' and cp[2] != '6' and cp[2] != '7' and cp[2] != '8' and cp[2] != '9':
        destino = 'Otro'
#cuarto caracter Numero
    elif cp[3] != '0' and cp[3] != '1' and cp[3] != '2' and cp[3] != '3' and cp[3] != '4' and cp[3] != '5' and cp[3] != '6' and cp[3] != '7' and cp[3] != '8' and cp[3] != '9':
        destino = 'Otro'
# Quinto caracter Numero
    elif cp[4] != '0' and cp[4] != '1' and cp[4] != '2' and cp[4] != '3' and cp[4] != '4' and cp[4] != '5' and cp[4] != '6' and cp[4] != '7' and cp[4] != '8' and cp[4] != '9':
        destino = 'Otro'
#Sexto caracter letra
    elif (valor_ascii5 < 64 or valor_ascii5 > 122) or (valor_ascii5 > 91 and valor_ascii5 < 97):
        destino = 'Otro'
#Septimo caracter letra
    elif (valor_ascii6 < 64 or valor_ascii6 > 122) or (valor_ascii6 > 91 and valor_ascii6 < 97):
        destino = 'Otro'
#Octavo caracter letra
    elif (valor_ascii7 < 64 or valor_ascii7 > 122) or (valor_ascii7 > 91 and valor_ascii7 < 97):
        destino = 'Otro'
#Argentina
    else:
        destino = 'Argentina'

print(destino)

'''
a = input("ingresa una letra: ")
valor_ascii = ord(a)
print(valor_ascii)
if  (valor_ascii < 64 or valor_ascii > 122) or (valor_ascii > 91 and valor_ascii < 97):
    print('otros')
else:
    print('Arg')
'''