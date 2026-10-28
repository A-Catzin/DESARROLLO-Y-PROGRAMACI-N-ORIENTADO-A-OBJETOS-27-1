class HojaRuta:
    def __init__(self, folio, zona):
        self.folio = folio        # Público (+)
        self.zona = zona          # Público (+)
        self.__repartidor = None  # Privado (-)
        self.__envios = []        # Privado (-)

    def __del__(self):
        print(f"Hoja de ruta {self.folio} cerrada y eliminada de memoria.")

    # Encapsulamiento Método 2: @property para proteger acceso al repartidor y lista de envíos
    @property
    def repartidor(self):
        return self.__repartidor

    @repartidor.setter
    def repartidor(self, nuevo_repartidor):
        self.__repartidor = nuevo_repartidor
        print(f"[Ruta {self.folio}] Repartidor asignado: {nuevo_repartidor.mostrar_datos()}")

    def agregar_envio(self, envio):
        self.__envios.append(envio)
        print(f"[Ruta {self.folio}] Envío {envio.codigo} agrupado en la hoja de ruta.")

    def calcular_total_ruta(self):
        total = 0.0
        for envio in self.__envios:
            total = total + envio
        return total

    def calcular_peso_total(self):
        peso_total = 0.0
        for envio in self.__envios:
            peso_total = peso_total + envio.get_peso()
        return peso_total

    def mostrar_resumen(self):
        print(f"\n--- RESUMEN HOJA DE RUTA: {self.folio} ({self.zona}) ---")
        if self.__repartidor:
            print(f"Responsable: {self.__repartidor.mostrar_datos()}")
        else:
            print("Responsable: Sin asignar")
        print(f"Total de envíos agrupados: {len(self.__envios)}")
        print(f"Peso total de carga: {self.calcular_peso_total()} kg")
        print(f"Costo total de la ruta: ${self.calcular_total_ruta()}")
