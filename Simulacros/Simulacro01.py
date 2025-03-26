import random

multiplo5 = 0
multiplo7 = 0
multiplo9 = 0
numero_mayor = None
pares1500 = 0
random.seed(49)
suma = 0

for i in range(20000):

    num = random.randint(1, 45000)
    suma += num
    if num % 5 == 0:
        multiplo5 += 1
    if num % 7 == 0:
        multiplo7 += 1
    if num % 9 == 0:
        multiplo9 += 1

    inicio2 = str(num)
    inicio =int(inicio2[-1])
    int(num)
    if 5 <= inicio % 10 <= 8:
        if numero_mayor is None or numero_mayor < num:
            numero_mayor = num

    if num <= 15000 and num % 2 == 0:
        pares1500 += 1

porcentaje = (pares1500 * 100) // 20000

int(porcentaje)

if suma == 451459554:
    print('ok')
else:
    print('error')
    print(suma)

print ('1 multiplos de 5 :',multiplo5,'\nMultipos de 7',multiplo7,'\nMultiplos de 9',multiplo9 )
print('='*40)
print('2:Numero mayor cuyo ultimo digito esta entre 5 y 8',numero_mayor)
print('='*40)
print('3:cantidad de pares menores a 1500:',pares1500)
print('='*40)
print('4:Porcentaje truncado:',porcentaje)
