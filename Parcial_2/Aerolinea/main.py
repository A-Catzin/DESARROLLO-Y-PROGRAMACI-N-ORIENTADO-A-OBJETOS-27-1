from Pago import Pago
from Reserva import Reserva

# Usando Reserva con @property
reserva1 = Reserva("RES-01", "2026-10-19", "Pendiente", 1500.0)
print("Total inicial:", reserva1.total)

reserva1.total = 1800.0
print("Nuevo total:", reserva1.calcularTotal())
reserva1.confirmar()
print("Estado reserva:", reserva1.estado)

print("-" * 30)

# Usando Pago con get y set
pago1 = Pago("PAG-01", 1800.0, "Tarjeta", "Pendiente")
print("Monto inicial:", pago1.get_monto())

pago1.set_monto(2000.0)
print("Nuevo monto:", pago1.get_monto())
pago1.procesar()
print("Estado pago:", pago1.get_estado())