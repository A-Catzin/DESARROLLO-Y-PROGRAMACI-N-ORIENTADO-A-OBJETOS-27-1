class Repartidor:
    def __init__(self, id_repartidor, nombre, vehiculo):
        self.nombre = nombre                 # Público (+)
        self.vehiculo = vehiculo             # Público (+)
        self.__id_repartidor = id_repartidor # Privado (-)

    def __del__(self):
        print(f"Repartidor {self.nombre} liberado de memoria.")

    # Encapsulamiento Método 1: Getter y Setter tradicional para el dato privado
    def get_id_repartidor(self):
        return self.__id_repartidor

    def set_id_repartidor(self, nuevo_id):
        if len(nuevo_id.strip()) > 0:
            self.__id_repartidor = nuevo_id
        else:
            print("El ID del repartidor no puede estar vacío.")

    def mostrar_datos(self):
        return f"{self.nombre} (ID: {self.__id_repartidor} | Vehículo: {self.vehiculo})"
