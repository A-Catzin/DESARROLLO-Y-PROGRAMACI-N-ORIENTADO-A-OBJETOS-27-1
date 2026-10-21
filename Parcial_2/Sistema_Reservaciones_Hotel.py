class Habitacion:
    def __init__(self, numero_habitacion, precio_por_noche):
        self.__numero_habitacion = numero_habitacion  
        self.__precio_por_noche = precio_por_noche    
        self.disponible = True

    @property
    def precio_por_noche(self):
        return self.__precio_por_noche

    @precio_por_noche.setter
    def precio_por_noche(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio_por_noche = nuevo_precio
            print(f"Precio actualizado a: ${self.__precio_por_noche}")
        else:
            print("El precio debe ser mayor a 0.")

    def get_numero_habitacion(self):
        return self.__numero_habitacion

    def verificarDisponibilidad(self):
        return self.disponible

    def actualizarEstado(self, nuevo_estado):
        self.disponible = nuevo_estado

    def calcularCosto(self, num_noches):
        return self.__precio_por_noche * num_noches


class Cliente:
    def __init__(self, id_cliente, nombre_completo):
        self.__id_cliente = id_cliente          
        self.__nombre_completo = nombre_completo  

    def get_nombre_completo(self):
        return self.__nombre_completo

    def set_nombre_completo(self, nuevo_nombre):
        if len(nuevo_nombre.strip()) > 0:
            self.__nombre_completo = nuevo_nombre
            print(f"Nombre actualizado a: {self.__nombre_completo}")
        else:
            print("El nombre no puede estar vacío.")

    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self, nuevo_id):
        if len(nuevo_id.strip()) > 0:
            self.__id_cliente = nuevo_id
            print(f"ID de cliente actualizado a: {self.__id_cliente}")
        else:
            print("El ID no puede estar vacío.")