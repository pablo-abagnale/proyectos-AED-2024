

ganador = ""
mejor_tiempo = None
total_tiempos = 0

competidores = int(input('Cantidad de competidores: '))
tiempo_recor =  int(input('tiempo recor en segundos: '))

for competidor in range(competidores):

    nombre = input('Nombre del competidore: ')
    tiempo = int(input('Tiempo en segundos: '))
    total_tiempos += tiempo
    if mejor_tiempo is None or mejor_tiempo > tiempo:
        mejor_tiempo = tiempo
        ganador = nombre

promedio = total_tiempos / competidores

print('El tiempo promedio de la carrera es:',promedio)

print('El ganador es:',ganador)

if mejor_tiempo < tiempo_recor:
    print('romper el recor!!!!')

