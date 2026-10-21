class Pagos:
    def __init__(self, id, monto, tipo_op, costo):
        self.id = id
        self.tipo_op = tipo_op
        self.__monto = monto
        self.__costo = costo

    # Getters y Setters
    def get_monto(self):
        return self.__monto

    def set_monto(self, monto):
        self.__monto = monto

    def get_costo(self):
        return self.__costo

    def set_costo(self, costo):
        self.__costo = costo

    # Métodos
    def procesarTransaccion(self):
        print(f"Pago {self.id} procesado con {self.tipo_op} por ${self.__monto}")

    def validarMonto(self):
        return self.__monto >= self.__costo

    def generarComprobante(self):
        print(f"Comprobante {self.id}: ${self.__monto} ({self.tipo_op})")


# Demostración
pago1 = Pagos("PAG-001", 500, "Tarjeta", 450)

print("Monto:", pago1.get_monto())
print("Costo:", pago1.get_costo())

pago1.set_monto(600)
print("Nuevo monto:", pago1.get_monto())

print("¿Monto válido?", pago1.validarMonto())
pago1.procesarTransaccion()
pago1.generarComprobante()
