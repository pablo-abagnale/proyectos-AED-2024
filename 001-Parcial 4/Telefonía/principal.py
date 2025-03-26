from modulos import*

def principal():
    opc = -1
    array_usuarios = []
    while opc != 0:
        opc = menu()
        if opc == 1:
            array_usuarios = cargar_array()
        elif opc == 2:
            mostrar_array(array_usuarios)
        elif opc == 3:
            cargar_matriz(array_usuarios)
        elif opc == 4:
            pass
        elif opc == 5:
            pass
if __name__=='__main__':
    principal()