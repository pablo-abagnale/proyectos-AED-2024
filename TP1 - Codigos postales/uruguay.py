cp = input("Ingrese el código postal del lugar de destino: ")
Montevideo = False
if len(cp) == 6:

    if cp[0] != '0' and cp[0] != '1' and cp[0] != '2' and cp[0] != '3' and cp[0] != '4' and cp[0] != '5' and cp[0] != '6' and cp[0] != '7' and cp[0] != '8' and cp[0] != '9':
        destino = 'Otro'
    elif cp[1] != '0' and cp[1] != '1' and cp[1] != '2' and cp[1] != '3' and cp[1] != '4' and cp[1] != '5' and cp[1] != '6' and cp[1] != '7' and cp[1] != '8' and cp[1] != '9':
        destino = 'Otro'
    elif cp[2] != '0' and cp[2] != '1' and cp[2] != '2' and cp[2] != '3' and cp[2] != '4' and cp[2] != '5' and cp[2] != '6' and cp[2] != '7' and cp[2] != '8' and cp[2] != '9':
        destino = 'Otro'
    elif cp[3] != '0' and cp[3] != '1' and cp[3] != '2' and cp[3] != '3' and cp[3] != '4' and cp[3] != '5' and cp[3] != '6' and cp[3] != '7' and cp[3] != '8' and cp[3] != '9':
        destino = 'Otro'
    elif cp[4] != '0' and cp[4] != '1' and cp[4] != '2' and cp[4] != '3' and cp[4] != '4' and cp[4] != '5' and cp[4] != '6' and cp[4] != '7' and cp[4] != '8' and cp[4] != '9':
        destino = 'Otro'
    else:
        destino = 'Uruguay'

    if cp[0] == '1':
        Montevideo = True
    else:
        Montevideo = False

if Montevideo == True:
    provincia = 'Montevideo'
else:
    provincia = 'otra'

print(destino)
print(provincia)

