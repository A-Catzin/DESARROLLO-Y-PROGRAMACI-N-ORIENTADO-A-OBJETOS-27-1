class Habitacion:
    def __init__(self, numero_habitacion, precio_por_noche):
        self.numero_habitacion = numero_habitacion
        self.precio_por_noche = precio_por_noche
        self.disponible = True

    def verificarDisponibilidad(self):
        return self.disponible

    def actualizarEstado(self, nuevo_estado):
        self.disponible = nuevo_estado

    # Sobrecarga: se puede llamar con 1 o 2 datos (noches y, opcionalmente, descuento)
    def calcularCosto(self, num_noches, descuento=0):
        total = self.precio_por_noche * num_noches
        return total - (total * descuento / 100)


class Cliente:
    def __init__(self, id_cliente, nombre_completo):
        self.id_cliente = id_cliente
        self.nombre_completo = nombre_completo
        self.historial = []

    # Sobrecarga: se puede llamar solo con el nombre, o con nombre e id
    def registrarDatos(self, nombre, id_cliente=None):
        self.nombre_completo = nombre
        if id_cliente is not None:
            self.id_cliente = id_cliente

    def consultarHistorial(self):
        return self.historial


class Pago:
    def __init__(self, id_pago, monto):
        self.id_pago = id_pago
        self.monto = monto

    def procesarTransaccion(self):
        print(f"Pago {self.id_pago} procesado por ${self.monto}")

    def validarMonto(self, total_requerido):
        return self.monto >= total_requerido

    def generarComprobante(self):
        print(f"Comprobante del pago {self.id_pago}: ${self.monto}")


class Reservacion:
    def __init__(self, codigo_reserva, fecha_ingreso):
        self.codigo_reserva = codigo_reserva
        self.fecha_ingreso = fecha_ingreso
        self.fecha_salida = None
        self.confirmada = False

    # Sobrecarga: se puede dar solo la entrada o entrada y salida
    def registrarPeriodo(self, check_in, check_out=None):
        self.fecha_ingreso = check_in
        self.fecha_salida = check_out

    def calcularTotal(self, precio_por_noche, num_noches):
        return precio_por_noche * num_noches

    def confirmarReserva(self):
        self.confirmada = True

    def gestionarCancelacion(self):
        self.confirmada = False


class Hotel:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.habitaciones = []

    # Sobrecarga: se puede consultar sin filtro o con filtro de precio máximo
    def consultarDisponibilidad(self, precio_maximo=None):
        resultado = []
        for h in self.habitaciones:
            if h.verificarDisponibilidad():
                if precio_maximo is None or h.precio_por_noche <= precio_maximo:
                    resultado.append(h)
        return resultado

    def gestionarHabitaciones(self, habitacion):
        self.habitaciones.append(habitacion)
