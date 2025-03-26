#Ingreso de datos

segundos_ingresados= int(input("Ingrese los segungos registrados: "))

if segundos_ingresados > 89999:

    print('Excedido')
else:
    hh = segundos_ingresados//3600
    mm = (segundos_ingresados % 3600)//60
    ss = (segundos_ingresados % 3600)%60

    print(hh,':',mm,':',ss)

h_ingresada = input('Ingrese el tiempo ingresado en el formato hh:mm:ss: ')

hh = int(h_ingresada[0:2])*3600
mm = int(h_ingresada[3:5])*60
ss = int(h_ingresada[6:8])

total_segundos = hh+mm+ss

print(total_segundos)