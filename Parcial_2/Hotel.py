class Pagos:
        def __init__(self, id, monto, tipo_op, costo):
            self.id = id
            self.tipo_op = tipo_op
            self.__monto = monto
            self.__costo = costo
    
        def get_monto(self):
            return self.__monto

        def set_monto(self, monto):
            self.__monto = monto

        def get_costo(self):
            return self.__costo

        def set_costo(self, costo):
            self.__costo = costo

        def procesarTransaccion(self):
            print(f"Pago {self.id} procesado con {self.tipo_op} por ${self.__monto}")

        def validarMonto(self):
            return self.__monto >= self.__costo

        def generarComprobante(self):
            print(f"Comprobante {self.id}: ${self.__monto} ({self.tipo_op})")


pago_prueba = Pagos(1, 1500, "Tarjeta", 1000)
pago_prueba.procesarTransaccion()
print(f"¿El monto cubre el costo? {pago_prueba.validarMonto()}")
pago_prueba.generarComprobante()



