class Ticket:
    def __init__(self,codigo,pasajero,pais,asiento,importe):
        self.codigo = codigo
        self.pasajero = pasajero
        self.pais = pais
        self.asiento = asiento
        self.importe = importe

    def __str__(self):
        return f'Codigo: {self.codigo:<10}N° indentificador de pasajero: {self.pasajero:<10}Pais destino: {self.pais:<10}N° de asiento: {self.asiento:<10}Importe: ${self.importe:<10}'