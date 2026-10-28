from Envio import Envio


class Paquete(Envio):
    def __init__(self, codigo, peso, distancia, volumen, descripcion="Paquete estándar"):
        super().__init__(codigo, peso, distancia)
        self.descripcion = descripcion  # Público (+)
        self.__volumen = 0.0            # Privado (-)
        self.volumen = volumen

    def __del__(self):
        print(f"Paquete {self.codigo} eliminado de memoria.")

    # Encapsulamiento Método 2: @property y @setter con validación (> 0)
    @property
    def volumen(self):
        return self.__volumen

    @volumen.setter
    def volumen(self, nuevo_volumen):
        if nuevo_volumen > 0:
            self.__volumen = nuevo_volumen
        else:
            print(f"[{self.codigo}] Error: El volumen ({nuevo_volumen} m3) no puede ser cero ni negativo.")

    # Polimorfismo y sobrecarga de método
    def calcular_costo(self, seguro=0.0):
        costo_base = super().calcular_costo(seguro)
        return costo_base + (self.__volumen * 50.0)
