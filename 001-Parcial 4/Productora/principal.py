from modulos import *
__author__ = '<Abagnale Pablo>'
def principal():

    opc = -1
    array_peliculas = []
    while opc != 0:
        opc = menu()
        if opc == 1:
            array_peliculas = carga_manual()
        elif opc == 2:
            mostrar(array_peliculas)
        elif opc == 3:
            buscar_modificar_importe(array_peliculas)
        elif opc == 4:
            cargar_archivo(array_peliculas)
        elif opc == 5:
            mostrar_archivo()
        elif opc == 6:
            mostrar_id(array_peliculas)
        elif opc == 7:
            matriz_pais_tipo(array_peliculas)


if __name__ == '__main__':
    principal()
