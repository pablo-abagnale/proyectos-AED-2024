#Ingreso de datos
print('='*40)
print('Tunos de los operarios \n\t1-Diurno\n\t2-Nocturno')
turno = int(input('Ingrese el tuno: '))

print('='*40)

h_diurno = 35.5
h_nocturno = 40.60
if turno == 1:
    qhora = float(input('Ingrese la cantidad de horas diurnas trabajadas: '))
    pago = h_diurno * qhora
    print('Al empleado le corresponden $:',pago,'por realizar',qhora,'Diurnas')
elif turno == 2:
    qhora = float(input('Ingrese la cantidad de horas nocturnas trabajadas: '))
    pago = h_nocturno * qhora
    print('Al empleado le corresponden $:', pago, 'por realizar', qhora, 'nocturnas')
elif turno > 2 or turno < 1:
    print('El tuno es invalido')

