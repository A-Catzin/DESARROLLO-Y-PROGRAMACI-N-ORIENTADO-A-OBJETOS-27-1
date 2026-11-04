class Repartidor:
    def __init__(self, id_repartidor, nombre, vehiculo):
        self.nombre = nombre
        self.vehiculo = vehiculo
        self.__id_repartidor = id_repartidor

    def __del__(self):
        print(f"Repartidor {self.nombre} eliminado")

    def get_id_repartidor(self):
        return self.__id_repartidor

    def set_id_repartidor(self, nuevo_id):
        self.__id_repartidor = nuevo_id
