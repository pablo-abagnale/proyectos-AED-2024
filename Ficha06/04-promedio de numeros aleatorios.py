#Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de [0, 100000]
import random

i = 0
suma = 0
while i < 1001:
    i += 1
    num = random.randint(1,100000)
    suma = suma + num

promedio = suma/1000

print(promedio)
