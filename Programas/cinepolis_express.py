"""
Sistema Cinépolis Express (Versión Educativa e Interactiva)
===========================================================
Ejemplo base de Programación Orientada a Objetos (POO) en Python,
diseñado para aprender clases, objetos, herencia y relaciones.

Permite interactuar directamente desde la terminal eligiendo
opciones numeradas (1, 2, 3...) e ingresando los datos del cliente.
"""

# =====================================================================
# 1. USUARIOS (HERENCIA)
# =====================================================================

class Usuario:
    """Clase base: datos comunes de una persona en el sistema."""
    def __init__(self, id_usuario: str, nombre_completo: str, correo: str, telefono: str, password: str):
        self.id_usuario = id_usuario
        self.nombre_completo = nombre_completo
        self.correo = correo
        self.telefono = telefono
        self.password = password
        self.sesion_activa = False

    def iniciar_sesion(self, password: str) -> bool:
        if self.password == password:
            self.sesion_activa = True
            print(f"✅ Sesión iniciada: ¡Bienvenido(a), {self.nombre_completo}!")
            return True
        print(f"❌ Contraseña incorrecta para {self.nombre_completo}.")
        return False

    def cerrar_sesion(self) -> None:
        self.sesion_activa = False
        print(f"👋 Sesión cerrada para {self.nombre_completo}.")


class Cliente(Usuario):
    """Clase derivada: cliente que acumula puntos Club Cinépolis."""
    def __init__(self, id_usuario: str, nombre_completo: str, correo: str, telefono: str, password: str, numero_tarjeta_club: str):
        super().__init__(id_usuario, nombre_completo, correo, telefono, password)
        self.numero_tarjeta_club = numero_tarjeta_club
        self.puntos_acumulados = 50  # Puntos de bienvenida

    def consultar_puntos(self) -> int:
        return self.puntos_acumulados

    def acumular_puntos(self, monto_compra: float) -> None:
        nuevos_puntos = int(monto_compra // 10)  # 1 punto por cada $10 MXN
        self.puntos_acumulados += nuevos_puntos
        print(f"⭐ Acumulaste {nuevos_puntos} puntos Club Cinépolis. Total: {self.puntos_acumulados} pts.")

    def redimir_puntos(self, cantidad: int) -> bool:
        if cantidad <= self.puntos_acumulados:
            self.puntos_acumulados -= cantidad
            print(f"🎁 Se canjearon {cantidad} puntos. Saldo restante: {self.puntos_acumulados} pts.")
            return True
        print("❌ Puntos insuficientes.")
        return False


class Empleado(Usuario):
    """Clase derivada: personal operativo que valida boletos y despacha dulcería."""
    def __init__(self, id_usuario: str, nombre_completo: str, correo: str, telefono: str, password: str, codigo_empleado: str, puesto: str, turno: str):
        super().__init__(id_usuario, nombre_completo, correo, telefono, password)
        self.codigo_empleado = codigo_empleado
        self.puesto = puesto
        self.turno = turno

    def validar_acceso_qr(self, codigo_qr: 'CodigoQR') -> bool:
        print(f"\n👮 Empleado(a) {self.nombre_completo} escaneando código en puerta...")
        return codigo_qr.validar_acceso_sala()

    def despachar_dulceria(self, codigo_qr: 'CodigoQR') -> bool:
        print(f"\n🍿 Empleado(a) {self.nombre_completo} escaneando código en dulcería...")
        return codigo_qr.validar_canje_dulceria()


# =====================================================================
# 2. CINE, PELÍCULA, SALA Y ASIENTOS
# =====================================================================

class Pelicula:
    """Información de una película."""
    def __init__(self, id_pelicula: str, titulo: str, duracion_minutos: int, clasificacion: str, genero: str, sinopsis: str):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.duracion_minutos = duracion_minutos
        self.clasificacion = clasificacion
        self.genero = genero
        self.sinopsis = sinopsis

    def obtener_detalles(self) -> str:
        return f"{self.titulo} [{self.clasificacion}] | {self.duracion_minutos} min | {self.genero}"


class Asiento:
    """Butaca individual."""
    def __init__(self, id_asiento: str, fila: str, numero: int, tipo_asiento: str = "Tradicional"):
        self.id_asiento = id_asiento
        self.fila = fila
        self.numero = numero
        self.tipo_asiento = tipo_asiento
        self.estado = "Disponible"  # Disponible, Bloqueado, Ocupado

    @property
    def codigo(self) -> str:
        return f"{self.fila}{self.numero}"

    def bloquear_temporal(self) -> bool:
        if self.estado == "Disponible":
            self.estado = "Bloqueado"
            print(f"🔒 Asiento {self.codigo} apartado temporalmente.")
            return True
        print(f"❌ El asiento {self.codigo} ya no está disponible.")
        return False

    def liberar(self) -> None:
        if self.estado != "Ocupado":
            self.estado = "Disponible"
            print(f"🔓 Asiento {self.codigo} liberado.")

    def confirmar_ocupado(self) -> None:
        self.estado = "Ocupado"
        print(f"🎟️ Asiento {self.codigo} asignado definitivamente.")


class Sala:
    """Sala física que contiene asientos (Composición)."""
    def __init__(self, id_sala: str, numero_sala: int, tipo_sala: str, capacidad_total: int):
        self.id_sala = id_sala
        self.numero_sala = numero_sala
        self.tipo_sala = tipo_sala
        self.capacidad_total = capacidad_total
        self.asientos: list[Asiento] = []

    def agregar_asiento(self, asiento: Asiento) -> None:
        self.asientos.append(asiento)

    def consultar_mapa_asientos(self) -> list[Asiento]:
        return self.asientos


class Funcion:
    """Proyección de una película en una sala y horario específico."""
    def __init__(self, id_funcion: str, pelicula: Pelicula, sala: Sala, horario: str, precio_boleto_base: float):
        self.id_funcion = id_funcion
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario
        self.precio_boleto_base = precio_boleto_base

    def verificar_disponibilidad(self) -> list[Asiento]:
        return [a for a in self.sala.asientos if a.estado == "Disponible"]

    def buscar_asiento(self, codigo: str) -> Asiento | None:
        for a in self.sala.asientos:
            if a.codigo == codigo.strip().upper():
                return a
        return None


# =====================================================================
# 3. DULCERÍA
# =====================================================================

class ComboDulceria:
    """Combo o alimento de dulcería express."""
    def __init__(self, id_combo: str, nombre: str, descripcion: str, precio: float, stock: int):
        self.id_combo = id_combo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad: int) -> bool:
        return self.stock >= cantidad

    def descontar_stock(self, cantidad: int) -> None:
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"📦 Stock de '{self.nombre}' actualizado ({self.stock} disponibles).")
        else:
            print("❌ Stock insuficiente en dulcería.")


# =====================================================================
# 4. PAGOS Y TERMINAL POS
# =====================================================================

class TerminalExternaPOS:
    """Dispositivo bancario para cobro de tarjeta."""
    def __init__(self, id_terminal: str, puerto_ip: str):
        self.id_terminal = id_terminal
        self.puerto_ip = puerto_ip

    def enviar_monto_cobro(self, monto: float) -> None:
        print(f"\n💳 [Terminal POS {self.id_terminal}] Monto a cobrar: ${monto:.2f} MXN.")
        print("💳 Por favor aproxime o inserte su tarjeta bancaria...")

    def recibir_respuesta_transaccion(self, simular_exito: bool = True) -> bool:
        if simular_exito:
            print("💳 [Terminal POS] ¡Transacción Aprobada por el banco!")
            return True
        print("💳 [Terminal POS] Transacción Rechazada.")
        return False


class Pago:
    """Registro del pago realizado."""
    def __init__(self, id_pago: str, monto: float, metodo_pago: str = "Tarjeta"):
        self.id_pago = id_pago
        self.monto = monto
        self.metodo_pago = metodo_pago
        self.numero_autorizacion = ""
        self.estado = "Pendiente"

    def procesar_en_terminal(self, pos: TerminalExternaPOS, exito: bool = True) -> bool:
        pos.enviar_monto_cobro(self.monto)
        if pos.recibir_respuesta_transaccion(exito):
            self.estado = "Aprobado"
            self.numero_autorizacion = "AUTH-89234"
            print(f"✅ Pago exitoso. Núm. de autorización: {self.numero_autorizacion}")
            return True
        self.estado = "Rechazado"
        return False


# =====================================================================
# 5. DETALLES, CÓDIGO QR Y TICKET
# =====================================================================

class DetalleBoleto:
    """Partida individual de butaca en el ticket."""
    def __init__(self, id_detalle: str, precio: float, tipo_boleto: str, asiento: Asiento, funcion: Funcion):
        self.id_detalle = id_detalle
        self.precio = precio
        self.tipo_boleto = tipo_boleto
        self.asiento = asiento
        self.funcion = funcion


class DetalleDulceria:
    """Partida de producto de dulcería en el ticket."""
    def __init__(self, id_detalle: str, combo: ComboDulceria, cantidad: int):
        self.id_detalle = id_detalle
        self.combo = combo
        self.cantidad = cantidad
        self.precio_unitario = combo.precio
        self.subtotal = self.calcular_subtotal()

    def calcular_subtotal(self) -> float:
        return self.cantidad * self.precio_unitario


class CodigoQR:
    """Pase de acceso a sala y canje de dulcería."""
    def __init__(self, id_qr: str, codigo_texto: str):
        self.id_qr = id_qr
        self.codigo_texto = codigo_texto
        self.sala_accedida = False
        self.dulceria_canjeada = False

    def validar_acceso_sala(self) -> bool:
        if self.sala_accedida:
            print("❌ Este boleto YA FUE USADO para entrar a la sala.")
            return False
        self.sala_accedida = True
        print("✅ Acceso AUTORIZADO a la sala. ¡Que disfrutes la película!")
        return True

    def validar_canje_dulceria(self) -> bool:
        if self.dulceria_canjeada:
            print("❌ Este combo YA FUE ENTREGADO previamente.")
            return False
        self.dulceria_canjeada = True
        print("✅ Vale de dulcería VÁLIDO. ¡Aquí tienes tus alimentos!")
        return True


class Ticket:
    """Ticket principal que consolida boletos, dulcería, pago y QR."""
    def __init__(self, id_ticket: str, folio: str, cliente: Cliente | None = None):
        self.id_ticket = id_ticket
        self.folio = folio
        self.cliente = cliente
        self.detalles_boletos: list[DetalleBoleto] = []
        self.detalles_dulceria: list[DetalleDulceria] = []
        self.pago: Pago | None = None
        self.codigo_qr: CodigoQR | None = None
        self.subtotal_boletos = 0.0
        self.subtotal_dulceria = 0.0
        self.monto_total = 0.0
        self.estado = "Iniciado"

    def agregar_boleto(self, detalle: DetalleBoleto) -> None:
        self.detalles_boletos.append(detalle)
        self.calcular_total()

    def agregar_dulceria(self, detalle: DetalleDulceria) -> None:
        self.detalles_dulceria.append(detalle)
        self.calcular_total()

    def calcular_total(self) -> float:
        self.subtotal_boletos = sum(b.precio for b in self.detalles_boletos)
        self.subtotal_dulceria = sum(d.subtotal for d in self.detalles_dulceria)
        self.monto_total = self.subtotal_boletos + self.subtotal_dulceria
        return self.monto_total

    def asociar_pago(self, pago: Pago) -> None:
        self.pago = pago
        if pago.estado == "Aprobado":
            self.estado = "Pagado"
            for b in self.detalles_boletos:
                b.asiento.confirmar_ocupado()
            for d in self.detalles_dulceria:
                d.combo.descontar_stock(d.cantidad)
            if self.cliente:
                self.cliente.acumular_puntos(self.monto_total)
        else:
            self.estado = "Cancelado"
            self.cancelar()

    def emitir_ticket(self) -> None:
        if self.estado == "Pagado":
            self.codigo_qr = CodigoQR("QR-01", f"QR-CINEXPRESS-{self.folio}")
            self.estado = "EmitidoConQR"
            print(f"\n🎟️ Ticket {self.folio} generado con éxito.")

    def cancelar(self) -> None:
        for b in self.detalles_boletos:
            b.asiento.liberar()
        self.estado = "Cancelado"
        print(f"🚫 Ticket {self.folio} cancelado.")


# =====================================================================
# 6. COMPLEJO CINEMATOGRÁFICO
# =====================================================================

class ComplejoCine:
    """Representa el cine y administra funciones, salas y dulcería."""
    def __init__(self, id_complejo: str, nombre: str, direccion: str):
        self.id_complejo = id_complejo
        self.nombre = nombre
        self.direccion = direccion
        self.salas: list[Sala] = []
        self.funciones: list[Funcion] = []
        self.combos: list[ComboDulceria] = []

    def agregar_sala(self, sala: Sala) -> None:
        self.salas.append(sala)

    def programar_funcion(self, funcion: Funcion) -> None:
        self.funciones.append(funcion)

    def agregar_combo(self, combo: ComboDulceria) -> None:
        self.combos.append(combo)

    def sincronizar_con_nube(self) -> bool:
        print(f"\n☁️ Sincronizando ventas de '{self.nombre}' con la nube corporativa...")
        print("☁️ Base de datos central actualizada con éxito.")
        return True


# =====================================================================
# 7. APLICACIÓN INTERACTIVA (KIOSCO EXPRESS)
# =====================================================================

def iniciar_kiosco_interactivo():
    print("=" * 65)
    print("      🎬 CINÉPOLIS EXPRESS: KIOSCO DE AUTOGESTIÓN 🎬")
    print("=" * 65)

    # 1. Configuración de salas y catálogo inicial
    cine = ComplejoCine("CMP-1", "Cinépolis Plaza Satélite", "Circuito Centro Comercial 2251")

    # Sala 1: Tradicional 2D (8 asientos)
    sala1 = Sala("S1", 1, "Tradicional 2D", 8)
    for fila in ["A", "B"]:
        for n in range(1, 5):
            sala1.agregar_asiento(Asiento(f"{fila}{n}", fila, n))
    cine.agregar_sala(sala1)

    # Sala 2: VIP 3D (6 asientos)
    sala2 = Sala("S2", 2, "VIP 3D", 6)
    for fila in ["A", "B"]:
        for n in range(1, 4):
            sala2.agregar_asiento(Asiento(f"VIP-{fila}{n}", fila, n, tipo_asiento="VIP"))
    cine.agregar_sala(sala2)

    # Películas y Funciones
    pelicula1 = Pelicula("P1", "Dune: Parte Dos", 166, "B15", "Ciencia Ficción", "Paul Atreides busca justicia.")
    pelicula2 = Pelicula("P2", "Spider-Man: Across the Spider-Verse", 140, "A", "Animación", "Miles Morales recorre el multiverso.")
    pelicula3 = Pelicula("P3", "Kung Fu Panda 4", 94, "A", "Comedia / Familiar", "Po busca al nuevo Guerrero Dragón.")

    cine.programar_funcion(Funcion("F1", pelicula1, sala1, "16:00 hrs", precio_boleto_base=85.0))
    cine.programar_funcion(Funcion("F2", pelicula1, sala2, "19:30 hrs", precio_boleto_base=160.0))
    cine.programar_funcion(Funcion("F3", pelicula2, sala1, "18:45 hrs", precio_boleto_base=85.0))
    cine.programar_funcion(Funcion("F4", pelicula3, sala1, "21:15 hrs", precio_boleto_base=80.0))

    # Combos de Dulcería
    cine.agregar_combo(ComboDulceria("C1", "Combo Cuates", "Palomitas Grandes + 2 Refrescos Grandes", 185.0, stock=20))
    cine.agregar_combo(ComboDulceria("C2", "Combo Pareja VIP", "Palomitas Grandes + 2 Refrescos + Nachos", 230.0, stock=15))
    cine.agregar_combo(ComboDulceria("C3", "Combo Individual", "Palomitas Medianas + 1 Refresco Mediano", 120.0, stock=30))

    # Empleado encargado de validar
    empleado = Empleado("EMP-1", "Mariana López", "mlopez@cinepolis.com", "5599887766", "admin123", "E-104", "Taquilla/Dulcería", "Vespertino")

    # -------------------------------------------------------------
    # PASO 1: Datos del Cliente
    # -------------------------------------------------------------
    print("\n--- PASO 1: Registro / Identificación del Cliente ---")
    nombre = input("Ingresa tu nombre completo: ").strip() or "Carlos Méndez"
    correo = input("Ingresa tu correo electrónico: ").strip() or "carlos@gmail.com"
    telefono = input("Ingresa tu teléfono: ").strip() or "5512345678"
    password = input("Crea una contraseña para tu cuenta: ").strip() or "1234"

    cliente = Cliente(
        id_usuario="CLI-01",
        nombre_completo=nombre,
        correo=correo,
        telefono=telefono,
        password=password,
        numero_tarjeta_club="CLUB-8877"
    )

    # Iniciar sesión
    print(f"\nIniciando sesión con el usuario '{cliente.nombre_completo}'...")
    cliente.iniciar_sesion(password)
    print(f"Puntos de bienvenida en Club Cinépolis: {cliente.consultar_puntos()} pts.")

    # -------------------------------------------------------------
    # PASO 2: Selección de Película y Función con Número (1, 2, 3...)
    # -------------------------------------------------------------
    print("\n--- PASO 2: Cartelera Disponible ---")
    print("Selecciona la función que deseas ver:")
    for i, func in enumerate(cine.funciones, start=1):
        print(f"  [{i}] {func.pelicula.titulo} [{func.pelicula.clasificacion}]")
        print(f"      Sala: {func.sala.numero_sala} ({func.sala.tipo_sala}) | Horario: {func.horario} | Precio: ${func.precio_boleto_base:.2f}")

    while True:
        seleccion_str = input(f"\nElige una opción (1 a {len(cine.funciones)}): ").strip()
        if seleccion_str.isdigit() and 1 <= int(seleccion_str) <= len(cine.funciones):
            funcion_seleccionada = cine.funciones[int(seleccion_str) - 1]
            break
        print("❌ Opción inválida. Ingresa un número de la lista.")

    print(f"\nHas seleccionado: {funcion_seleccionada.pelicula.titulo} a las {funcion_seleccionada.horario}")

    # -------------------------------------------------------------
    # PASO 3: Selección de Asientos
    # -------------------------------------------------------------
    print("\n--- PASO 3: Selección de Asientos ---")
    asientos_disponibles = funcion_seleccionada.verificar_disponibilidad()
    codigos_disp = [a.codigo for a in asientos_disponibles]
    print(f"Mapa de asientos libres en Sala {funcion_seleccionada.sala.numero_sala}:")
    print("  " + "  ".join([f"[{c}]" for c in codigos_disp]))

    ticket = Ticket("TCK-001", "FOLIO-2026", cliente=cliente)

    while True:
        entrada_asientos = input("\nIngresa los asientos que deseas separados por coma (ej. A1, A2): ").strip()
        asientos_elegidos = [cod.strip().upper() for cod in entrada_asientos.split(",") if cod.strip()]

        if not asientos_elegidos:
            print("❌ Debes ingresar al menos un asiento.")
            continue

        # Validar si todos existen y están disponibles
        validos = True
        objetos_asiento = []
        for codigo in asientos_elegidos:
            asiento = funcion_seleccionada.buscar_asiento(codigo)
            if not asiento or asiento.estado != "Disponible":
                print(f"❌ El asiento '{codigo}' no es válido o ya está ocupado.")
                validos = False
                break
            objetos_asiento.append(asiento)

        if validos:
            for asiento in objetos_asiento:
                asiento.bloquear_temporal()
                detalle_b = DetalleBoleto(
                    id_detalle=f"BOL-{asiento.codigo}",
                    precio=funcion_seleccionada.precio_boleto_base,
                    tipo_boleto="General",
                    asiento=asiento,
                    funcion=funcion_seleccionada
                )
                ticket.agregar_boleto(detalle_b)
            break

    print(f"Subtotal boletos ({len(ticket.detalles_boletos)} entrada(s)): ${ticket.subtotal_boletos:.2f}")

    # -------------------------------------------------------------
    # PASO 4: Selección de Dulcería con Número (1, 2, 3...)
    # -------------------------------------------------------------
    print("\n--- PASO 4: Dulcería Express (Opcional) ---")
    print("¿Deseas agregar algún combo a tu orden?")
    print("  [0] No agregar dulcería (Continuar al pago)")
    for i, combo in enumerate(cine.combos, start=1):
        print(f"  [{i}] {combo.nombre} (${combo.precio:.2f}) - {combo.descripcion}")

    while True:
        opcion_dulc = input(f"\nElige una opción (0 a {len(cine.combos)}): ").strip()
        if opcion_dulc.isdigit() and 0 <= int(opcion_dulc) <= len(cine.combos):
            idx = int(opcion_dulc)
            if idx == 0:
                print("No se agregaron productos de dulcería.")
            else:
                combo_elegido = cine.combos[idx - 1]
                cant_str = input(f"¿Cuántos '{combo_elegido.nombre}' deseas? [1]: ").strip()
                cantidad = int(cant_str) if cant_str.isdigit() and int(cant_str) > 0 else 1

                if combo_elegido.verificar_disponibilidad(cantidad):
                    detalle_d = DetalleDulceria(f"DUL-{combo_elegido.id_combo}", combo_elegido, cantidad)
                    ticket.agregar_dulceria(detalle_d)
                    print(f"Agregado: {cantidad}x {combo_elegido.nombre} (+${detalle_d.subtotal:.2f})")
                else:
                    print("❌ No hay suficiente stock disponible de ese combo.")
            break
        print("❌ Opción inválida. Elige un número de la lista.")

    print(f"\nTotal general a pagar: ${ticket.calcular_total():.2f}")

    # -------------------------------------------------------------
    # PASO 5: Selección de Método de Pago con Número (1 o 2)
    # -------------------------------------------------------------
    print("\n--- PASO 5: Pago en Terminal Bancaria POS ---")
    print("Selecciona tu método de pago:")
    print("  [1] Tarjeta Bancaria con Chip / Contactless (Terminal POS)")
    print("  [2] Tarjeta de Crédito / Débito física")

    while True:
        metodo_opc = input("Elige método de pago (1 o 2): ").strip()
        if metodo_opc in ["1", "2"]:
            metodo_nombre = "Tarjeta Contactless POS" if metodo_opc == "1" else "Tarjeta Chip POS"
            break
        print("❌ Opción inválida. Elige 1 o 2.")

    pos = TerminalExternaPOS("POS-01", "192.168.10.15")
    pago = Pago("PAG-101", ticket.monto_total, metodo_nombre)
    pago_exitoso = pago.procesar_en_terminal(pos, exito=True)
    ticket.asociar_pago(pago)

    # -------------------------------------------------------------
    # PASO 6: Emisión del Ticket y Código QR
    # -------------------------------------------------------------
    print("\n--- PASO 6: Emisión de Ticket Digital ---")
    ticket.emitir_ticket()

    print("\n" + "=" * 55)
    print("              CINÉPOLIS EXPRESS: TICKET")
    print("=" * 55)
    print(f"Folio: {ticket.folio} | Estado: {ticket.estado}")
    print(f"Cliente: {cliente.nombre_completo} | Club: {cliente.numero_tarjeta_club}")
    print(f"Película: {funcion_seleccionada.pelicula.titulo}")
    print(f"Sala: {funcion_seleccionada.sala.numero_sala} ({funcion_seleccionada.sala.tipo_sala}) | Horario: {funcion_seleccionada.horario}")
    print(f"Asiento(s): {', '.join([b.asiento.codigo for b in ticket.detalles_boletos])}")
    if ticket.detalles_dulceria:
        print(f"Dulcería: {', '.join([f'{d.cantidad}x {d.combo.nombre}' for d in ticket.detalles_dulceria])}")
    else:
        print("Dulcería: Ninguna")
    print(f"Total Pagado: ${ticket.monto_total:.2f}")
    print(f"Pase QR Digital: {ticket.codigo_qr.codigo_texto}")
    print(f"Saldo Club Cinépolis: {cliente.consultar_puntos()} pts")
    print("=" * 55)

    # -------------------------------------------------------------
    # PASO 7: Simulación de Validación por el Empleado
    # -------------------------------------------------------------
    input("\nPresiona [Enter] para simular la llegada a la sala del cine...")
    empleado.validar_acceso_qr(ticket.codigo_qr)

    # Simular intento de reingreso con el mismo boleto
    print("\nSimulando si alguien intenta volver a usar el mismo boleto:")
    empleado.validar_acceso_qr(ticket.codigo_qr)

    # Si compró dulcería, simular entrega
    if ticket.detalles_dulceria:
        input("\nPresiona [Enter] para simular el reclamo en la dulcería express...")
        empleado.despachar_dulceria(ticket.codigo_qr)
        print("\nSimulando si alguien intenta reclamar el combo por segunda vez:")
        empleado.despachar_dulceria(ticket.codigo_qr)

    # -------------------------------------------------------------
    # PASO 8: Sincronización con la Nube
    # -------------------------------------------------------------
    cine.sincronizar_con_nube()

    print("\n🎉 ¡Flujo de compra completado exitosamente!")


# =====================================================================
# EJECUCIÓN PRINCIPAL
# =====================================================================
if __name__ == "__main__":
    iniciar_kiosco_interactivo()