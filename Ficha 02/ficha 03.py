'''
#1. Plazo fijo

#Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente de un banco y calcular
# el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3% y que el banco cobra una tasa fija
# de gastos por servicios financieros igual $20 por cuenta.

#Ingreso de datos por teclado

monto_inicial=float(input('Ingrese el monto inicial $: '))

#Procesos

INTERES = 0.023
TASA_FIJA  = 20 #$
monto_interes = monto_inicial * INTERES
monto_final = monto_inicial + monto_interes - TASA_FIJA

#Salida

print('-'*25,'\n')

print('El monto final es $: ', monto_final)
print('-'*25,'\n')
'''
'''
#2. Fecha como cadena
#Desarrollar un programa que cargue por teclado una cadena de caracteres que se supone representa una fecha en formato 'dd/mm/aaaa',
# y muestre por separado el día, el mes y el año. Ejemplo: si la cadena ingresada es '16/03/2016' el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.

#Ingreso de datos

fecha = input('Ingrese la fecha usando el formato DD/MM/YYYY: ')

print('-'*25,'\n')
print('Día:',fecha[0]+fecha[1],'\n')
print('Mes:',fecha[3]+fecha[4],'\n')
print('Año:',fecha[6]+fecha[7]+fecha[8]+fecha[9],'\n')
print('\n','-'*25)
'''
'''
#3. Importe como cadena
#Desarrollar un programa que cargue por teclado un importe (cantidad de dinero) expresado como número en coma flotante y muestre un mensaje con esa cantidad pero en dos formatos:
# en uno debe aparecer precedida por el signo '$' y en el otro debe aparecer precedida por la palabra "pesos".

#Ingresar datos

pesos = float(input('Ingrese la cantidades de pesos: '))

print('-'*25,'\n')
print('El monto es: $',pesos)
print('El monto es:',pesos,'pesos')
print('\n','-'*25)
'''
'''
#4. Duración de un vuelo
#Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos),determine cuál es su duración en minutos.
#Si el viajero necesita luego 45 minutos más para ir del aeropuerto al hotel que ha reservado, ¿a qué hora llegara al mismo?

#Ingreso de datos

h_partida = input('ingrese la hora de partida HH:MM del vuelo:')
h_llegada = input('ingrese la hora de llegada HH:MM del vuelo:')

#cuentas

h_partida_num = int(h_partida[0:2])
m_partida_num = int(h_partida[-2:])
h_llegada_num = int(h_llegada[0:2])
m_llegada_num = int(h_llegada[-2:])

#tiempo en minutos

tiempo1 = h_partida_num * 60 + m_partida_num
tiempo2 = h_llegada_num * 60 + m_llegada_num

duracion = tiempo2 - tiempo1

#Hora de llegada al hotel

tiempo3 = tiempo2 + 45

hora_hotel = tiempo3 // 60
minutos_hotel = tiempo3 % 60

#Salidas

print('-'*25,'\n')
print('El viaje dura:',duracion,'min')
print('La hora de llegada al hotel es:',hora_hotel,':',minutos_hotel)
'''
'''
#5. Control electoral
#Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen, para cierto candidato: apellido, nombre y cantidad de votos.
#Luego presentar en pantalla un resumen que muestre: iniciales del candidato, cantidad de votos entre paréntesis, y debajo una línea con tantas  "x" como votos obtenidos
#(por ejemplo, el candidato obtuvo 4 votos, deberá aparecer una línea como esta:  "xxxx"  con cuatro letras "x") (Asumimos que en el centro vecinal no hay demasiados electores,
#de forma que podamos estar seguros que no habrá miles o millones de votos... sólo unos pocos para darle sentido al enunciado).


#Ingreso por teclado

nombre =input('Ingrese el nombre del candidato: ')
apellido =input('Ingrese el apellido del candidato: ')
votos = int(input('Ingrese la cantidad de votos: '))

print('='*25,'\n')
print(nombre[0]+apellido[0],'('+str(votos)+')')
print('x'*votos)
print('\n','='*25)

'''
'''
#6. Cálculo de sueldo
#Ingreso de datos
nombre = input('Ingrese el nombre del empleado: ')
area = input('Ingrese el area del empleado: ')
sueldo_actual = float(input('Ingrese el sueldo actual: '))

#Cuentas
INCREMENTO = 1.08#%
DESCUENTO= 0.975 #%

sueldo_incremento = sueldo_actual * INCREMENTO
sueldo_final = sueldo_incremento * DESCUENTO

#Salida

print('='*25,'\n')
print('\tNombre Empleado:',nombre,'\t\tNuevo Salario:$',sueldo_final,'\n')
print('\tÁrea Funcional:',area,'\n')
print('\tSueldo Actual: $',sueldo_actual)
print('\n','='*25,'\n')
'''
'''
#7. Cálculo presupuestario

#Ingreso de datos

presupuesto = float(input('Ingrese el presupuesto: '))

#Cuentas

procentaje_urgencias = 0.37
procentaje_pediatria = 0.42
porcentaje_traumatologia = 0.21

p_urgencias = presupuesto * procentaje_urgencias
p_pediatria = presupuesto * procentaje_pediatria
p_traumatologia = presupuesto * porcentaje_traumatologia

#Salida

print('='*50,'\n')
print('\tEl presupuesto total del hospital es:',presupuesto)
print('\t\tEl presupuesto para uregencias:',p_urgencias)
print('\t\tEl presupuesto para pediatria:',p_pediatria)
print('\t\tEl presupuesto para traumatologia:',p_traumatologia)
print('\n','='*50,'\n')
'''
'''
#8. Calculo Distancia de Viaje

#Ingreso de datos

metros_recorridos = float(input('Ingrese metros recorridos: '))

#Proecesos

distancia_recorrida_km = metros_recorridos / 1000

DISTANCIA_TOTAL_KM = 3641.3 #Distancia Ushuahia - La Quiaca
DISTANCIA_TOTAL_M = (DISTANCIA_TOTAL_KM * 1000)

porcentaje_recorrido = (metros_recorridos * 100) / DISTANCIA_TOTAL_M
#Salida

print('=' * 50,'\n')
print('Distancia recorrida km:',distancia_recorrida_km,'km\n')
print('Distancia recorrida m:',metros_recorridos,'mts\n')
print('Porcentaje recorrido de la distancia:', round(porcentaje_recorrido,2),'%\n')
print('=' * 50,'\n')
'''
'''
#9. Costos del Proyecto

#Ingreso de datos

presupuesto = float(input('Ingrese el presupuesto: $'))

#Cuentas

costos_maximos = presupuesto * 0.83

#salida

print('costos maximos:$',costos_maximos)
'''
'''
#10. Tiempos de Triatlon

#Ingreso de datos

tiempo_natacion = input('Ingrese el tiempo natacion en MM:SS: ')
tiempo_ciclismo = input('Ingrese el tiempo clismo en MM:SS: ')
tiempo_pedestre = input('Ingrese el tiempo pedestre en MM:SS: ')

#Procesos

#Natacion

min_natacion = int(tiempo_natacion[0:2])
seg_natacion = int(tiempo_natacion[-2:])
total_natacion = min_natacion * 60 + seg_natacion

#Ciclismo

min_ciclismo = int(tiempo_ciclismo[0:2])
seg_ciclismo = int(tiempo_ciclismo[-2:])
total_ciclismo = min_ciclismo * 60 + seg_ciclismo

#pedestre

min_pedestre = int(tiempo_pedestre[0:2])
seg_pedestre = int(tiempo_pedestre[-2:])
total_pedestre = min_pedestre * 60 + seg_pedestre

tiempos = total_natacion, total_ciclismo, total_pedestre

tiempo_max = max(tiempos)
tiempo_min = min(tiempos)
promedio = (total_natacion + total_ciclismo + total_pedestre) / 3

# total de tiempos en HH:MM:SS

suma_min = (min_ciclismo + min_natacion + min_pedestre)
horas = suma_min // 60


suma_seg = (seg_ciclismo + seg_pedestre + seg_natacion)
minutos = suma_seg // 60 + suma_min % 60

segundos = suma_seg % 60



#Salida

print('='*50,'\n')
print('Tiempo total de la prueba:',horas,':',minutos,':',segundos)
print('-' * 50)
print('tiempo maximo:',tiempo_max,'seg  Tiempo minimo:',tiempo_min,'seg')
print('-' * 50)
print('promedio:',round(promedio,2))
print('\n','='*50,'\n')
'''
'''
#11. Palabra enmascarada

#Ingreso de datos

palabra_original = input('Ingrese la palabra original: ')

#procesos

largo_mascara = len(palabra_original)-2

#salida

print(palabra_original[0],'*'*largo_mascara,palabra_original[-1],sep = '')

'''
#12. Calculo de Posta de Natacion















