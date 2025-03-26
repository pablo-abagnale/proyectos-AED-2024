
codigo = input("Codigo: ")

Argentina = True


for c in range(len(codigo)):

    i = codigo[c]

    if c == 0 or c >=4:
        
        caracter = ord(codigo[c])
        
        if (caracter < 64 or caracter > 122) or (caracter > 91 and caracter < 97) or (caracter == 105 or caracter == 73 or caracter == 164 or caracter == 165 or caracter == 79 or caracter == 111):

            Argentina = False
    else:

        i = codigo[c]

        if i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9':

            Argentina = False

    print(c,'-',caracter,'-',i,'-',Argentina)


if codigo[0] == 'A':
    provincia= "Salta"
elif codigo[0] == 'B':
    provincia = "Provincia de Buenos Aires"
elif codigo[0] == 'C':
    provincia='Ciudad Autónoma de Buenos Aires'
elif codigo[0]=='D':
    provincia= 'San Luis'
elif codigo[0]=='E':
    provincia='Entre Ríos'
elif codigo[0]=='F':
    provincia='La Rioja'
elif codigo[0]=='G':
    provincia='Santiago del Estero'
elif codigo[0]=='H':
     provincia='Chaco'
elif codigo[0]=='J':
    provincia='San Juan'
elif codigo[0]=='K':
    provincia='Catamarca'
elif codigo[0]=='L':
    provincia='La Pampa'
elif codigo[0]=='M':
    provincia='Mendoza'
elif codigo[0]=='N':
    provincia='Misiones'
elif codigo[0]=='P':
    provincia='Formosa'
elif codigo[0]=='Q':
    provincia='Neuquén'
elif codigo[0]=='R':
    provincia='Rio Negro'
elif codigo[0]=='S':
    provincia='Santa Fe'
elif codigo[0]=='T':
    provincia='Tucuman'
elif codigo[0]=='U':
    provincia='Chubut'
elif codigo[0]=='V':
    provincia='Tierra del Fuego'
elif codigo[0]=='W':
    provincia='Corrientes'
elif codigo[0]=='X':
    provincia ='Cordoba'
elif codigo[0]=='Y':
    provincia ='Jujuy'
elif codigo[0]=='Z':
    provincia ='Santa Cruz'

if Argentina  == True:
    destino = 'Argentina'
else:
    destino = 'Otro'
    
region = provincia

print(destino,provincia)


