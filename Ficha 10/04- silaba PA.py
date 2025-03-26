archivo = open("texto2.txt", "r")
texto = archivo.read()

palabras_total = 0
spa = False
anterior = None
suma_spa = 0
for letra in texto:



    if letra == ' ' or letra == '.':
        if spa and ultima_letra:
            suma_spa +=1
        palabras_total += 1
    if letra == 'p':
        anterior = 'p'
    if letra == 'a' and anterior == 'p':
        spa = True
    else: spn = False
    if letra == 'n':
        ultima_letra = True
    else: ultima_letra = False

    if palabras_total > 2:
        2
        




print(palabras_total)
print(suma_spa)