from Envio import Envio


class Paquete(Envio):
    def __init__(self, codigo, peso, distancia, volumen):
        super().__init__(codigo, peso, distancia)
        self.__volumen = volumen

    def __del__(self):
        print(f"Paquete {self.codigo} eliminado")

    @property
    def volumen(self):
        return self.__volumen

    @volumen.setter
    def volumen(self, nuevo_volumen):
        if nuevo_volumen > 0:
            self.__volumen = nuevo_volumen
        else:
            print("El volumen no puede ser negativo")

    def calcular_costo(self):
        return super().calcular_costo() + (self.__volumen * 20)
