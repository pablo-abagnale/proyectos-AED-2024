#Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.

#Los requerimientos funcionales del programa son:

#a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.

#b) Cantidad de valores pares ingresados.

#c) Cantidad de valores impares ingresados.

#d) Informar si en la carga de números se ingreso al menos un número 0.

#e) Informar si la serie contiene solo números pares e impares alternados

i = int(input('ingresa un numero:'))
pares = 0
impares = 0
ingreso_cero = False
suma = 0
while i >= 0:

    if i > 49 and i < 101:
        suma = suma + i
    if i % 2 == 0:
        pares += 1
    if i % 2 != 0:
        impares += 1
    if i == 0:
        ingreso_cero = True

    i = int(input('ingresa un numero:'))

print('Suma de numeros entre 50 y 100:', suma)
print('cantidad de numeros pares:',pares)
print('cantidad de numeros impares:',impares)
if ingreso_cero == True:
    print('Se ingreso por lo menos un cero')
if pares == 0:
    print('Solo se ingresaron numeros inpares')