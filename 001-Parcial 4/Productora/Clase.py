class Pelicula:
    def __init__(self, identificador,titulo,importe,tipo,pais):
        self.identificador = identificador
        self.titulo = titulo
        self.importe = importe
        self.tipo = tipo
        self.pais = pais

    def __str__(self):
        return f'Id:{self.identificador:>4} Titulo: {self.titulo:<25} Costo de la prodiución: ${round(self.importe,2):<10} ID Tipo:{self.tipo:<3} ID Pais:{self.pais:<3}'