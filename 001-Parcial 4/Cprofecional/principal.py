from Clases import Profecional
from modulos import *
def principal():
    opc = -1
    array_profecionales = []
    while opc != 0:
        opc = menu()
        if opc == 1:
            array_profecionales = cargar_datos()
        elif opc == 2:
            mostrar_array(array_profecionales)
        elif opc == 3:
            buscar_desactulizado(array_profecionales)
        elif opc == 4:
            crear_archivo(array_profecionales)
        elif opc == 5:
            mostrar_archivo(array_profecionales)
        elif opc == 6:
            buscar_nombre(array_profecionales)
        elif opc == 7:
            crear_matriz(array_profecionales)

if __name__ == '__main__':
    principal()