from Envio import Envio


class Documento(Envio):
    def __init__(self, codigo, peso, distancia, urgente=False, tipo_sobre="Carta"):
        super().__init__(codigo, peso, distancia)
        self.tipo_sobre = tipo_sobre  # Público (+)
        self.__urgente = urgente      # Privado (-)

    def __del__(self):
        print(f"Documento {self.codigo} eliminado de memoria.")

    # Encapsulamiento Método 2: @property y @setter
    @property
    def urgente(self):
        return self.__urgente

    @urgente.setter
    def urgente(self, es_urgente):
        self.__urgente = es_urgente

    # Polimorfismo y sobrecarga de método
    def calcular_costo(self, seguro=0.0):
        costo_base = super().calcular_costo(seguro)
        if self.__urgente:
            return costo_base + 40.0
        return costo_base
