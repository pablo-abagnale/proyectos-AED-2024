archivo = open("texto.txt", "r")
texto = archivo.read()
i = None
palabra = 0
mayores4 = 0
palabraxy = 0
silabamo = 0
mo = False
anterior = 0
letras = 0
palabras = 0

for letra in texto:
    palabra += 0
    if letra == ' ' or letra == '.':
        palabra += 1
        if palabra > 4:
            mayores4 += 1
        if letras > 0:
            palabras += 1
    else:
        letras += 1
        if letra == 'Y' or letra == 'x':
            palabraxy += 1
        if letra == 'm':
            anterior = 'm'
        if letra == 'o' and anterior == 'm':
            mo = True
            if mo == True:
                 silabamo += 1

    anterior = letra


print('*'*40)
print('Mayores a 4 letras = ',mayores4)
print('Contienen Y o X  = ',palabraxy)
print('Contienen silaba MO  = ',silabamo)
print('Promedio de letras por palabra =',letras/palabras)




