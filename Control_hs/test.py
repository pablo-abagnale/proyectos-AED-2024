def guardar_cntl_horas(array):

    archivo = 'ctrl_hs_digital.xlsx'
    try:
        wb = openpyxl.load_workbook(archivo)
    except FileNotFoundError:
        wb = openpyxl.Workbook()

    if 'BBDD_HS' in wb.sheetnames:
        ws_BBDD = wb['BBDD_HS']
    else:
        ws_BBDD = wb.create_sheet('BBDD_HS')

    # Verificar si la tabla "cntrl" existe
    tabla_existente = None
    for tbl in ws_BBDD.tables.values():
        if tbl.name == "cntrl":
            tabla_existente = tbl
            break

    if tabla_existente:
        # Borrar todos los datos de la tabla existente
        ws_BBDD.delete_rows(2, ws_BBDD.max_row)
    else:
        # Añadir encabezados si la tabla no existe
        ws_BBDD.append(['Mail', 'Agente', 'Fecha', 'Servicio', 'Estado', 'Duracion'])

    # Añadir datos
    for i in array:
        ws_BBDD.append([i.mail, i.agente, i.fecha, i.cola, i.estado, i.time])

    # Definir el rango de la tabla
    min_col = 1
    max_col = ws_BBDD.max_column
    min_row = 1
    max_row = ws_BBDD.max_row
    tabla_rango = f"A{min_row}:F{max_row}"

    if tabla_existente:
        # Actualizar el rango de la tabla existente
        tabla_existente.ref = tabla_rango
    else:
        # Crear Tabla
        tabla = Table(displayName="cntrl", ref=tabla_rango)
        estilo = TableStyleInfo(
            name="TableStyleMedium9",
            showFirstColumn=False,
            showLastColumn=False,
            showRowStripes=True,
            showColumnStripes=True
        )
        tabla.tableStyleInfo = estilo
        ws_BBDD.add_table(tabla)

    wb.save(archivo)
    wb.close()