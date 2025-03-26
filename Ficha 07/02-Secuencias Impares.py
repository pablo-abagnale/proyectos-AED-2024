'''n1 = int(input('Ingrese numero de inicio: '))
n2 = int(input('Ingrese numero de fim: '))

for i in range(n1, n2+1):

    if i % 2 == 0:
        print(i)

for i in range(n2, n1,-1):

    if i % 2 == 0:
        print(i)'''

num1 = int(input('Ingrese un numero: '))
num2 = int(input('Ingrese un numero: '))

if num1 > num2:
    may,men = num1,num2
else:
    may,men = num2,num1



