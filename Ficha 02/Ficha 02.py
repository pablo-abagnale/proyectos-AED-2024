# Ejercicio nº1 - Cuadrados y cubos
'''
#Ingresar numeros

nummero1 = float(input("Ingrese el primer numero: "))
nummero2 = float(input("Ingrese el segundo numero:"))

#Operaciones

suma_cuadrados = (nummero1**2) + (nummero2**2)
promedio_cubos = ((nummero1**3) + (nummero2**3))/2

#Resultados
print("-----------------------------------------------------------------------------------\n")
print("La suma de los cuadrados de los numeros",nummero1,"y",nummero2,"es",suma_cuadrados)
print("La promedio de los cubos de los numeros",nummero1,"y",nummero2,"es",promedio_cubos,"\n")
print("-----------------------------------------------------------------------------------\n")
'''

'''
# Descuento en medicinas

#Ingresar el monto del medicamento

precio = float(input("Ingrese el precio del medicamento:"))

#Cuentas

descuento = precio*0.35

precio_final = precio*0.65

#salida por pantalla

print("-----------------------------------------------------------------------------------\n")
print("precio del medicamento",precio)
print("descuento",descuento,"\n")
print("precio final",precio_final)
print("-----------------------------------------------------------------------------------\n")

'''
'''
#Ecuación de Einstein

# Constante

c= 299792.458 #Km/seg
# E = mc2

#Ingreso del valor de m

masa = float(input("Ingrese el valor de la masa en Kilogramos:"))

#Caculo de energía
e = masa*(c**2)

#Salida por pantalla

print("La energía producida es de:",e)

'''
'''
#Polinomio de segundo grado

#Ingreso por teclado
a = float(input("Ingrese el valor de a:"))
b = float(input("Ingrese el valor de b:"))
c = float(input("Ingrese el valor de c:"))
print("-----------------------------------------------------------------------------------\n")
x = float(input("Ingrese el valor de x:"))
# Cuentas

Discriminante = (b**2) - (4*a*c)
x1 = (-b + ((Discriminante))/(2*a))**0.5
x2 = (-b - ((Discriminante))/(2*a))**0.5

#Print por pantalla

print("-----------------------------------------------------------------------------------\n")

print("El valor de la discriminante es:",Discriminante)
print("El valor de la raiz x1 es:",x1)
print("El valor de la raiz x2 es:",x2)

print("-----------------------------------------------------------------------------------\n")
'''
'''
#5. Cálculo de ángulos

# Ingresa los valores

x = float(input("Ingrese el valor de x:"))
y = float(input("Ingrese el valor de y:"))

# Calcular el valor de los angulos Alfa y beta

'''
'''
#6. Precio de venta

#Ingreso del precio del articulo

precio_original = float(input("Ingrese el precio:"))

# Nuevo precio

precio_contado  = precio_original*0.90
precio_tarjeta = precio_original*1.10

#Salida por pantalla
print("-----------------------------------------------------------------------------------\n")
print("Precio contado",precio_contado,"$")
print("Precio con tarjeta",round(precio_tarjeta,2),"$")
'''
'''
#7. Votación en el Congreso

#Ingresar los votos

favor = int(input("Ingresa la cantidad de votos a favor:"))
contra = int(input("Ingresa la cantidad de votos en contra:"))

#Cuentas

total_votos = favor+contra

porcentaje_favor = (favor*100)/total_votos
porcentaje_contra = (contra*100)/total_votos

# Salida

print("La porcentaje de votos a favor es: ",round(porcentaje_favor,2),"porcentaje de votos en contra",round(porcentaje_contra,2))
print("total de votos es:",total_votos)

'''
'''
#8. Rinde de un Campo Agricola

#Ingreso

largo = float(input("Ingrese el largo del campo en mts:"))
ancho = float(input("Ingrese el ancho del campo en mts:"))

# Cuentas

perimetro = largo*ancho

quintales  = (perimetro/10)*2

# salida

print("El campo rinde",quintales,"quintales")

'''
'''
#9. Datos de un rectángulo

#Ingreso

alto = float(input("Ingrese el alto del rectangulo:"))
ancho = float(input("Ingrese el ancho del rectangulo:"))

#cuentas

area = alto*ancho
perimetro = (alto*2) + (ancho*2)

# Salida

print("El area del rectangulo es:",area)
print("El perimetro es:",perimetro)
'''
'''
#10. Calculo de Ganancias de Pelicula

#ingresar datos

actor = input("Ingrese el nombre del actor:")
recaudado = float(input("Ingrese lo recaudado por la pelicula: "))
porcentaje = float(input("Ingrese el porcentaje que le corresponde al actor: "))

#cuentas

corresponde = recaudado*(porcentaje/100)

#Salida

print("corresponden a ",actor,": $",corresponde)
'''