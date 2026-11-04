class Envio:
    def __init__(self, codigo, peso, distancia):
        self.codigo = codigo      # Público (+)
        self.__peso = peso        # Privado (-)
        self.__distancia = distancia  # Privado (-)

    def __del__(self):
        print(f"Envío {self.codigo} eliminado")

    # Encapsulamiento 1: get y set
    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self.__peso = nuevo_peso
        else:
            print("El peso no puede ser negativo")

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, nueva_distancia):
        if nueva_distancia > 0:
            self.__distancia = nueva_distancia
        else:
            print("La distancia no puede ser negativa")

    def calcular_costo(self):
        return (self.__peso * 10) + (self.__distancia * 5)

    # Sobrecarga del operador '+' para sumar costos de dos envíos
    def __add__(self, otro_envio):
        return self.calcular_costo() + otro_envio.calcular_costo()
