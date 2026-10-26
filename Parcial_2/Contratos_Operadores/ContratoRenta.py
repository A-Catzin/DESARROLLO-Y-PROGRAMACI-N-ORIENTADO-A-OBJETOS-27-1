class ContratoRenta:
    def __init__(self, folio, total):
        self.folio = folio
        self.total = total

    # Suma (+)
    def __add__(self, otro_contrato):
        return self.total + otro_contrato.total

    def __radd__(self, monto):
        return monto + self.total

    # Resta (-)
    def __sub__(self, monto_devolucion):
        return self.total - monto_devolucion.total

    def __rsub__(self, monto):
        return monto - self.total

    # Multiplicación (*)
    def __mul__(self, otro_contrato):
        return self.total * otro_contrato.total

    # División (/)
    def __truediv__(self, otro_contrato):
        return self.total / otro_contrato.total

    # Destructor
    def __del__(self):
        print("Contrato eliminado")
