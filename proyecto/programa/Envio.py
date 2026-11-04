class Envio:
    def __init__(self, codigo, peso, distancia):
        self.codigo = codigo
        self.__peso = peso
        self.__distancia = distancia

    def __del__(self):
        print(f"Envío {self.codigo} eliminado")

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

    def __add__(self, otro_envio):
        return self.calcular_costo() + otro_envio.calcular_costo()

    def __sub__(self, otro_envio):
        return self.calcular_costo() - otro_envio.calcular_costo()

    def __mul__(self, otro_envio):
        return self.calcular_costo() * otro_envio.calcular_costo()

    def __truediv__(self, otro_envio):
        return self.calcular_costo() / otro_envio.calcular_costo()
