import random

opcion = int(input('Ingrese una opcion:'))
i = 0
suma_num1 = 0
num1 = 0
num2 = 0
num_mayor = 0
num_menor = 0
menor_10k = 0
while opcion > 0 and opcion < 4:

    if opcion == 1:
        while i < 1000:
            i +=1
            num1 = random.randint(1,100000)
            suma_num1 = suma_num1 + num1
        promedio = (suma_num1/1000)
        print('resultado opcion 1:',promedio)
    elif opcion == 2:
        while i < 10000:
            i += 1
            num2 = random.randint(1, 100000)
            if num2 > num_mayor:
                num_mayor = num2
        print('resultado opcion 2:',num_mayor)
    elif opcion == 3:
        while i < 5000:
            i += 1
            num3 = random.randint(1, 100000)
            if num3 > num_menor:
                num_menor = num3
            if num3 < 10000:
                menor_10k += num3
        promedio_menor = (menor_10k/i)
        print('resultado opcion 3:',num_menor,'promedio menor a 10k:',promedio_menor)

    opcion = int(input('Ingrese una opcion:'))