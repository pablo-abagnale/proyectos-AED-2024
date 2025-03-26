class Juicio:

    def __init__(self, codigo, caratula, tipo, cliente,honorario):
        self.honorario = honorario  # Monto de los honorarios
        self.codigo = codigo #Codigo del expediente
        self.caratula = caratula #Caratula o descripcion del juicio
        self.tipo = tipo # Tipo de juicio ( int del 1 al 15 )
        self.cliente = cliente # nombre del clietne


    def __str__(self):
        return f"\nExpediente:{self.codigo:<5} \nCaratula: {self.caratula:<5} \ntipo de juicio: {self.tipo} \nCliente: {self.cliente} \nHonorarios: ${self.honorario}"

    def __lt__(self, other):
        return self.honorario < other.honorario
