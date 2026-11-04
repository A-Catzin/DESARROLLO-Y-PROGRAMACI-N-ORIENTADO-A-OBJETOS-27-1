class HojaRuta:
    def __init__(self, folio, zona):
        self.folio = folio
        self.zona = zona
        self.__repartidor = None
        self.__envios = []

    def __del__(self):
        print(f"Hoja de ruta {self.folio} eliminada")

    @property
    def repartidor(self):
        return self.__repartidor

    @repartidor.setter
    def repartidor(self, nuevo_repartidor):
        self.__repartidor = nuevo_repartidor

    def agregar_envio(self, envio):
        self.__envios.append(envio)

    def mostrar_ruta(self):
        print(f"--- Hoja de Ruta: {self.folio} ({self.zona}) ---")
        print(f"Repartidor: {self.__repartidor.nombre} - Vehículo: {self.__repartidor.vehiculo}")
        print(f"Cantidad de envíos: {len(self.__envios)}")
