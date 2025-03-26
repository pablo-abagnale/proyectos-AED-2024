#ingreso de datos
n1 = float(input('ingrese el primer numero: '))
n2 = float(input('ingrese el segundo numero: '))
n3 = float(input('ingrese el tercer numero: '))

suma = n1 + n2 + n3

if suma > 10:
    res = suma // 2
else:
    res = suma**2

print(res)