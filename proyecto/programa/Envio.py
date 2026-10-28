class Envio:
    def __init__(self, codigo, peso, distancia):
        self.codigo = codigo          # Público (+)
        self.__peso = 0.0             # Privado (-)
        self.__distancia = 0.0        # Privado (-)
        self.set_peso(peso)
        self.set_distancia(distancia)

    def __del__(self):
        print(f"Envío {self.codigo} eliminado de memoria.")

    # Encapsulamiento Método 1: Getters y Setters tradicionales para atributos privados
    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self.__peso = nuevo_peso
        else:
            print(f"[{self.codigo}] Error: El peso ({nuevo_peso} kg) no puede ser cero ni negativo.")

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, nueva_distancia):
        if nueva_distancia > 0:
            self.__distancia = nueva_distancia
        else:
            print(f"[{self.codigo}] Error: La distancia ({nueva_distancia} km) no puede ser cero ni negativa.")

    # Sobrecarga de método (parámetro opcional 'seguro')
    def calcular_costo(self, seguro=0.0):
        return (self.__peso * 15.0) + (self.__distancia * 8.0) + seguro

    # Sobrecarga de operadores: '+' para sumar el costo de dos envíos
    def __add__(self, otro_envio):
        return self.calcular_costo() + otro_envio.calcular_costo()

    def __radd__(self, monto_acumulado):
        return monto_acumulado + self.calcular_costo()

    # Sobrecarga de operadores: '-' para restar el costo de un envío devuelto/cancelado
    def __sub__(self, otro_envio):
        return self.calcular_costo() - otro_envio.calcular_costo()

    def __rsub__(self, monto_acumulado):
        return monto_acumulado - self.calcular_costo()
