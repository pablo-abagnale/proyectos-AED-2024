class Profecional():
    def __init__(self, documento,nombre,importe,afiliacion,trabajo,):
        self.documento = documento
        self.nombre = nombre
        self.importe = importe
        self.afilicacion = afiliacion
        self.trabajo = trabajo

    def __str__(self):
        return f'DNI: {self.documento:<10} Nombre:{self.nombre:<15} Cuota: ${self.importe:<5} Tipo de de afiliación: {self.afilicacion:<3} Tipo de trabajo: {self.trabajo:<3}'

