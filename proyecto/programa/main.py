from Paquete import Paquete
from Documento import Documento
from Repartidor import Repartidor
from HojaRuta import HojaRuta

paquete_1 = Paquete("PAQ-01", 5, 10, 2)
paquete_2 = Paquete("PAQ-02", 3, 8, 1)
doc_1 = Documento("DOC-01", 1, 4, True)

print(f"Costo Paquete 1: ${paquete_1.calcular_costo()}")
print(f"Costo Paquete 2: ${paquete_2.calcular_costo()}")
print(f"Costo Documento 1: ${doc_1.calcular_costo()}")

paquete_1.set_peso(-5)
paquete_1.volumen = -3

paquete_1.set_peso(6)
paquete_1.volumen = 3
print(f"Nuevo costo Paquete 1: ${paquete_1.calcular_costo()}")

suma_envios = paquete_1 + paquete_2
resta_envios = paquete_1 - paquete_2
multiplicacion_envios = paquete_1 * paquete_2
division_envios = paquete_1 / paquete_2

print(f"Suma (+): ${suma_envios}")
print(f"Resta (-): ${resta_envios}")
print(f"Multiplicación (*): {multiplicacion_envios}")
print(f"División (/): {division_envios}")

repartidor_1 = Repartidor("REP-01", "Carlos", "Moto")
ruta_1 = HojaRuta("RUTA-100", "Centro")

ruta_1.repartidor = repartidor_1
ruta_1.agregar_envio(paquete_1)
ruta_1.agregar_envio(paquete_2)
ruta_1.agregar_envio(doc_1)

ruta_1.mostrar_ruta()

del paquete_1
del paquete_2
del doc_1
del ruta_1
del repartidor_1
