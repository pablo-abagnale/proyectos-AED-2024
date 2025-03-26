def buscar_titulo(array,titulo):
    izq = 0
    der = len(array) - 1
    pos = -1
    while izq <= der:
        c = (izq + der) // 2
        if array[c].titulo == titulo:
            pos = c
            break
        elif array[c].titulo > titulo:
            der = c - 1
        else:
            izq = c + 1
    return pos