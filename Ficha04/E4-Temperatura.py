#Ingreso de datos

t1 = float(input('ingrese la primer temperatura : '))
t2 = float(input('ingrese la segunda temperatura : '))
t3 = float(input('ingrese la tercer temperatura : '))

prmedio = (t1 + t2 + t3)/3

if prmedio < t1:
    print('El promedio de las temperaturas del dia es: ', prmedio)
    print('la primer temperatura',t1,'° es mayor que el promedio ')
elif prmedio < t2:
    print('el promedio de las temperaturas es: ', prmedio)
    print('la segunda temperatura',t2,'° es mayor que el promedio ')
elif prmedio < t3:
    print('el promedio de las temperaturas es: ', prmedio)
    print('la tercer temperatura',t3,'° es mayor que el promedio ')
else:
    print('el promedio de las temperaturas es: ', prmedio)
    print('Ninguna temperatura es mayor que el promedio ')

