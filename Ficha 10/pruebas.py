
num = int(input("Ingrese un numero: "))
contador = 0
while num > 0:
    num = int(input("Ingrese un numero: "))
    if num % 4 == 0:
        contador += 1

    print(contador)
