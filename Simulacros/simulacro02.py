multipos3 = 0
multipos5 = 0
mayor = None
pares = 0
suma = 0
import random
random.seed(20220512)


for i in range(25000):

    num = random.randint(1,45000)

    if num % 3 == 0:
        multipos3 += 1
    if num % 5 == 0 and num % 3 != 0:
        multipos5 += 1

    inicio2 = str(num)
    inicio = int(inicio2[0])

    if inicio == 1:
        if mayor is None or mayor < num:
            mayor = num

    if num % 2 == 0 and num % 11 == 0:
        suma += num
        pares += 1


promedio = suma // pares
int(promedio)
no_cumplen = 25000 - multipos3 - multipos5
porcentaje_mul3 = (multipos3 * 100) // 25000
porcentaje_mul5 = (multipos5 * 100) // 25000
pocentaje_no_cumplen = (no_cumplen * 100) // 25000

porcentaje_punto1 = (no_cumplen + multipos3 + multipos5 * 100) // 25000


print('1:\nMultiplos de 3 :', multipos3,'\nMultiplos de 5 y no de 3 :', multipos5,'\nNumeros que no cumplen niguna condicion:',no_cumplen)
print('='*40)
print('2: Mayor de los numeros que empiezan con 1',mayor)
print('='*40)
print('3: Promedio truncado de numeros pares y mutiplos de 11',promedio)
print('='*40)
print('4: porcentaje entero contador 1 multiplo de 3:',porcentaje_mul3,'Contador 2 mutiplo de 5:',porcentaje_mul5, 'contador 3 no cumplen:',pocentaje_no_cumplen)
print('todos los contadores:',porcentaje_punto1)
print('='*40)


