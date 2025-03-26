class Publicacion:
    def __init__(self,codigo,titulo,tipo,costo):
        self.codigo = codigo
        self.titulo = titulo
        self.tipo = tipo
        self.costo = costo

    def __str__(self):
        return f'Identificador: {self.codigo}\ntitulo: {self.titulo}\nTipo: {self.tipo}\nCosto de publicacion: ${self.costo}'
    def __lt__(self, other):
        return self.codigo < other.codigo