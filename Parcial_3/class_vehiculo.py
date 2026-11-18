class vehiculo:
    def __init__(self, marca, tarifa):
        self.marca = marca
        self.__tarifa = tarifa

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        if tarifa < 0:
            raise ValueError("La tarifa no puede ser negativa")
        self.__tarifa = tarifa