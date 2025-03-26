#Ingreso de dato

n = 13251

v = 1
suma = n
mayor = 0
orbita = [n]

while n != 1:
    v +=1

    if n % 2 != 0:
        n = int(n * 3) + 1
    else:
       n = int(n/2)


    if n > mayor:
        mayor = n
    suma = suma +  n

    orbita.append(n)

promedio = (suma/ v)

print('='*25)
print('Orbita',orbita)
print('longitud ',v)
print('Promedio ',promedio)
print('Mayor',mayor)
#Ingreso de dato

n = 234519

v = 1
suma = n
mayor = 0
orbita = [n]

while n != 1:
    v +=1

    if n % 2 != 0:
        n = int(n * 3) + 1
    else:
       n = int(n/2)


    if n > mayor:
        mayor = n
    suma = suma +  n

    orbita.append(n)

promedio = (suma/ v)

print('='*25)
print('Orbita',orbita)
print('longitud ',v)
print('Promedio ',promedio)
print('Mayor',mayor)

#Ingreso de dato

n = 9386

v = 1
suma = n
mayor = 0
orbita = [n]

while n != 1:
    v +=1

    if n % 2 != 0:
        n = int(n * 3) + 1
    else:
       n = int(n/2)


    if n > mayor:
        mayor = n
    suma = suma +  n

    orbita.append(n)

promedio = (suma/ v)

print('='*25)
print('Orbita',orbita)
print('longitud ',v)
print('Promedio ',promedio)
print('Mayor',mayor)