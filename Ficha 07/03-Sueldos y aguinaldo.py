#Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

#a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.

#b) Determinar en qué mes recibió el sueldo más bajo del período.

#c) Informar el sueldo promedio del semestre.

i = 0
mayor_sueldo = None
menor_sueldo = None
mejor_mes = None
mes_menor = None
suma_sueldo = 0

meses = ('Enero','Febreo','Marzo','Abril','Mayo','Junio')

for mes in meses:
    sueldo = float(input('Ingrese el sueldo: '))
    suma_sueldo += sueldo
    if mayor_sueldo is None or mayor_sueldo < sueldo:
        mayor_sueldo = sueldo
        mejor_mes = mes

    if menor_sueldo is None or menor_sueldo > sueldo:
        menor_sueldo = sueldo
        mes_menor = mes

aguinaldo = mayor_sueldo / 2
promedio = suma_sueldo / 6

print('Peor mes:',mes_menor)
print('Aguinaldo:',aguinaldo)
print('Sueldo Promedio:',promedio)
