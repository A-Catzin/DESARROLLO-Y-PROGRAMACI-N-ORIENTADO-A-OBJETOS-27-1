from Paquete import Paquete
from Documento import Documento
from Repartidor import Repartidor
from HojaRuta import HojaRuta

# 1. Crear objetos (Herencia de Envio)
paquete_1 = Paquete("PAQ-01", 5, 10, 2)
paquete_2 = Paquete("PAQ-02", 3, 8, 1)
doc_1 = Documento("DOC-01", 1, 4, True)

print(f"Costo Paquete 1: ${paquete_1.calcular_costo()}")
print(f"Costo Paquete 2: ${paquete_2.calcular_costo()}")
print(f"Costo Documento 1: ${doc_1.calcular_costo()}")

# 2. Probar encapsulamiento y validación de negativos (get/set y @property)
paquete_1.set_peso(-5)     # No permite negativo (get/set)
paquete_1.volumen = -3     # No permite negativo (@property)

paquete_1.set_peso(6)      # Cambio válido con set
paquete_1.volumen = 3      # Cambio válido con @property
print(f"Nuevo costo Paquete 1: ${paquete_1.calcular_costo()}")

# 3. Sobrecarga de operador '+' (__add__)
suma_envios = paquete_1 + paquete_2
print(f"Suma de Paquete 1 y Paquete 2: ${suma_envios}")

# 4. Hoja de ruta y repartidor responsable
repartidor_1 = Repartidor("REP-01", "Carlos", "Moto")
ruta_1 = HojaRuta("RUTA-100", "Centro")

ruta_1.repartidor = repartidor_1
ruta_1.agregar_envio(paquete_1)
ruta_1.agregar_envio(paquete_2)
ruta_1.agregar_envio(doc_1)

ruta_1.mostrar_ruta()

# 5. Destructores (__del__)
del paquete_1
del paquete_2
del doc_1
del ruta_1
del repartidor_1
