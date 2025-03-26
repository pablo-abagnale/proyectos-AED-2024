class Usuario():
    def __init__(self,tel,hora,tipo,monto):
        self.tel=tel
        self.hora = hora
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        return f'Usuario: {self.tel} hora: {self.hora}:00 tipo de consumo: {self.tipo} monto: ${self.monto}'
