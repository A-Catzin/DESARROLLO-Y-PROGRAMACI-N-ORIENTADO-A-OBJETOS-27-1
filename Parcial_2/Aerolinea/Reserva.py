class Reserva:
    def __init__(self, codigo, fecha_creacion, estado, total):
        self.__codigo = codigo
        self.__fecha_creacion = fecha_creacion
        self.__estado = estado
        self.__total = total

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, nuevo_total):
        self.__total = nuevo_total

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    # Métodos del UML
    def confirmar(self):
        self.__estado = "Confirmada"
        print(f"Reserva {self.__codigo} confirmada.")

    def cancelar(self):
        self.__estado = "Cancelada"
        return True

    def calcularTotal(self):
        return self.__total
