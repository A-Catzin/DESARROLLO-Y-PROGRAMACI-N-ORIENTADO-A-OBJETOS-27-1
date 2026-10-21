class Pago:
    def __init__(self, id_pago, monto, metodo, estado):
        self.__id_pago = id_pago
        self.__monto = monto
        self.__metodo = metodo
        self.__estado = estado

    # Getters y Setters
    def get_monto(self):
        return self.__monto

    def set_monto(self, monto):
        self.__monto = monto

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    # Métodos del UML
    def procesar(self):
        self.__estado = "Completado"
        return True

    def reembolsar(self):
        self.__estado = "Reembolsado"
        return True
