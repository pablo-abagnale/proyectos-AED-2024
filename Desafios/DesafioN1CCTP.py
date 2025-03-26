def segundos_a_hms(segundos):
    # Calcula las horas, minutos y segundos
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    return horas, minutos, segundos


def hms_a_segundos(horas, minutos, segundos):
    # Calcula el total de segundos
    total_segundos = horas * 3600 + minutos * 60 + segundos
    return total_segundos


# Entrada: Cantidad de segundos
segundos_input = int(input("Ingresa la cantidad de segundos: "))

# Convierte segundos a horas, minutos y segundos
horas, minutos, segundos = segundos_a_hms(segundos_input)

# Verifica si el total de horas es menor o igual a 24
if horas <= 24:
    print(f"Tiempo transcurrido: {horas} horas, {minutos} minutos, {segundos} segundos")
else:
    print("Excedido")

# Entrada: Horas, minutos y segundos
horas_input = int(input("Ingresa la cantidad de horas: "))
minutos_input = int(input("Ingresa la cantidad de minutos: "))
segundos_input = int(input("Ingresa la cantidad de segundos: "))

# Convierte horas, minutos y segundos a total de segundos
total_segundos = hms_a_segundos(horas_input, minutos_input, segundos_input)
print(f"Total de segundos: {total_segundos}")
