'''Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.

Por cada habitante se ingresa: sexo (M/F) y edad. La carga de datos finaliza al ingresar cualquier otro valor para sexo.

El programa debe informar:

a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)

b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)

c) Si hay algún varón que supere los 80 años de edad'''

sexo = input("Ingrese el sexo del dato: ")
masculino = 0
femenino = 0
edad_escolar = 0
edad = 0
varon_mas80 = 0
while sexo == 'M' or sexo == 'F' or sexo == 'm' or sexo == 'f':

    edad = int(input("Ingrese el edad: "))

    if sexo == 'M' or sexo == 'm':
        masculino += 1
        if edad > 80:
            varon_mas80 += 1
    elif sexo == 'F' or sexo == 'f':
        femenino += 1
        if edad > 3 and edad < 19:
            edad_escolar += 1

    sexo = input("Ingrese el sexo del dato: ")

if masculino > femenino:
    print("hay mas varones.")
elif femenino > masculino:
    print("hay mas mujeres.")
else:
    print('hay la misma cantidad de habitantes hombres y mujeres .')

print('cantidad de mujeres en edad escolar entre 4 y 18 años inclusive es:',edad_escolar)
print('cantidad de varones mayores a 80 años:',varon_mas80)

