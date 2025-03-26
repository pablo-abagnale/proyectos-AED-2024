from Class_3 import *
import openpyxl
from datetime import datetime
import platform
import os
from modulos_3 import *
import calendar

# Cargar los archivos de Excel
wb_nomina = openpyxl.load_workbook('Nomina_Omnia.xlsx')
st_nomina = wb_nomina['nomina']
wb_botmaker = openpyxl.load_workbook('botmaker.xlsx')
st_botmaker = wb_botmaker['Sheet1']

def menu():
    array_agentes = []
    opc = -1
    array_agentes = cargar()
    print('\n', '-' * 20, '\tCARGA Nomina OK\t', '-' * 20)


    #mes = ingresar_mes()
    ctrl_horas(array_agentes)
    #utilizacion(mes)


if __name__ == '__main__':
    menu()
