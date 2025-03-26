#Ingreso de datos
nombre = input('Nombre del usuario: ')
apellido = input('Apellido del usuario: ')
dominio = input('Dominio del usuario: ')

#Proceso

if nombre[0] == apellido[0]:
    print('Mail sugerido: ',nombre+'.'+apellido+'@'+dominio)
else:
    print('Mail sugerido: ',nombre[0]+apellido+'@'+dominio)
