class Empleo:
    def __init__(self, identificador, descripcion, tipo,sueldo):
        self.identifiacador = identificador
        self.descripcion = descripcion
        self.tipo = tipo
        self.sueldo = sueldo

    def __str__(self):
        return f"N° de indetificador {self.identifiacador}  Descripcion:{self.descripcion:<17} Tipo:{self.tipo:<7} Sueldo:${self.sueldo}"
    def __lt__(self, other):
        return self.identifiacador < other.identificaror or self.descripcion > other.descripcion