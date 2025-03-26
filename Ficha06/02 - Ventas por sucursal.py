# Ingreso de datos

ventas = int(input('Ingrese el numero de ventas:'))

q_ventas = 0
q_ventas300 = 0
q_ventas400 = 0
q_ventas500 = 0
q_ventas600 = 0
ventas_menos = False

while ventas > 0:

    q_ventas += 1

    if ventas > 99 and ventas < 301:
        q_ventas300 +=1
    elif ventas == 400 :
        q_ventas400 +=1
    elif ventas == 500 :
        q_ventas500 +=1
    elif ventas == 600 :
        q_ventas600 +=1
    elif ventas < 50 :
        ventas_menos = True

    ventas = int(input('Ingrese el numero de ventas:'))

print('el total de ventas es:', q_ventas,'\n')
print('el numero de ventas entre 100 y 300 es ',q_ventas300,'\n')
print('Ventas de 400',q_ventas400,'\nVentas de 500',q_ventas500,'\nVentas de 600',q_ventas600,'\n')

if ventas_menos == True:
    print('Hubo ventas con menos de 50')
else:
    print('No hubo ventas con menos de 50')
