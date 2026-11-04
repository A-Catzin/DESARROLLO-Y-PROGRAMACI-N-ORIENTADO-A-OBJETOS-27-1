from Envio import Envio


class Documento(Envio):
    def __init__(self, codigo, peso, distancia, urgente):
        super().__init__(codigo, peso, distancia)
        self.urgente = urgente  # Público (+)

    def __del__(self):
        print(f"Documento {self.codigo} eliminado")

    def calcular_costo(self):
        costo = super().calcular_costo()
        if self.urgente:
            return costo + 30
        return costo
