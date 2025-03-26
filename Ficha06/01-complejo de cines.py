#Constantes

precio_full = 75
precio_descuento = 50 #entrada_full*0.66666666666666667

llave = 1
entradas_descuento = 0
entradas_full = 0

while llave != 0:
    entradas = int(input('Entradas: '))
    if entradas != 0:
        descuento = input('Descuento(S/N): ')

        if descuento == 'S':
            entradas_descuento += entradas
        else:
            entradas_full += entradas
    llave = entradas

recaudado_descuento = entradas_descuento * precio_descuento
recaudado_full = entradas_full * precio_full
total_entradas = entradas_descuento + entradas_full
total_recaudado = recaudado_descuento + recaudado_full

porcentaje_descuento = (entradas_descuento * 100) / total_entradas

print('total entradas: ', total_entradas)
print('total recaudado: $', total_recaudado)
print('porcentaje entradas con descuento: ', porcentaje_descuento,'%')




