__Autor__ = "<G196[1K13] Abagnale 96984 Baumann 41728 Briones 413712 >"
class Envio:
    def __init__(self, cp, direccion, tipo, pago, pais, monto):
        self.cp = cp
        self.direccion = direccion
        self.tipo = tipo
        self.pago = pago
        self.pais = pais
        self.monto = monto

    def __str__(self):  # Retornar cadena de texto con los datos que se quiere mostrar
        return f'\033[33mPais:\033[00m {self.pais:<10} \033[33mCP:\033[00m {self.cp:<10} \033[33mDirección:\033[00m {self.direccion:<20} \033[33mTipo:\033[00m {self.tipo:<5} \033[33mPago:\033[00m {self.pago:<5}\033[33mPrecio final:\033[00m ${self.monto:<10} '

