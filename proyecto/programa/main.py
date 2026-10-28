from Envio import Envio
from Paquete import Paquete
from Documento import Documento
from Repartidor import Repartidor
from HojaRuta import HojaRuta

print("=== 1. CREACIÓN DE OBJETOS Y HERENCIA (Atributos Públicos '+' y Privados '-') ===")
paquete_1 = Paquete("PAQ-101", 5.0, 10.0, 2.0, "Caja de electrónicos")
paquete_2 = Paquete("PAQ-102", 8.0, 15.0, 3.5, "Refacciones")
documento_1 = Documento("DOC-201", 0.5, 6.0, True, "Sobre manila")

print(f"Paquete 1 ({paquete_1.codigo} - {paquete_1.descripcion}) -> Peso: {paquete_1.get_peso()} kg, Volumen: {paquete_1.volumen} m3, Costo: ${paquete_1.calcular_costo()}")
print(f"Paquete 2 ({paquete_2.codigo} - {paquete_2.descripcion}) -> Peso: {paquete_2.get_peso()} kg, Volumen: {paquete_2.volumen} m3, Costo (con seguro $50): ${paquete_2.calcular_costo(50.0)}")
print(f"Documento 1 ({documento_1.codigo} - {documento_1.tipo_sobre}) -> Peso: {documento_1.get_peso()} kg, Urgente: {documento_1.urgente}, Costo: ${documento_1.calcular_costo()}")

print("\n=== 2. PRUEBA DE ENCAPSULAMIENTO Y VALIDACIÓN DE NEGATIVOS (get/set y @property) ===")
# Intento de asignar peso negativo con set_peso() y volumen negativo con @volumen.setter
paquete_1.set_peso(-4.0)
paquete_1.volumen = -1.5
print(f"Valores protegidos de {paquete_1.codigo} -> Peso sigue en: {paquete_1.get_peso()} kg | Volumen sigue en: {paquete_1.volumen} m3")

# Actualización válida con set_distancia() y @volumen.setter
paquete_1.set_distancia(12.0)
paquete_1.volumen = 2.5
print(f"{paquete_1.codigo} actualizado -> Distancia: {paquete_1.get_distancia()} km, Volumen: {paquete_1.volumen} m3, Nuevo costo: ${paquete_1.calcular_costo()}")

print("\n=== 3. SOBRECARGA DE OPERADORES (+ y -) ENTRE ENVÍOS ===")
suma_paquetes = paquete_1 + paquete_2
print(f"Suma directa de Paquete 1 + Paquete 2 (con __add__): ${suma_paquetes}")

total_tres_envios = suma_paquetes + documento_1
print(f"Suma acumulada con Documento 1 (con __radd__): ${total_tres_envios}")

despues_devolucion = total_tres_envios - documento_1
print(f"Total después de restar/devolver Documento 1 (con __rsub__): ${despues_devolucion}")

print("\n=== 4. HOJA DE RUTA Y ASIGNACIÓN DE REPARTIDOR ===")
repartidor_1 = Repartidor("REP-01", "Carlos Méndez", "Moto Cargo 150")
ruta_norte = HojaRuta("RUTA-001", "Zona Norte - Playa del Carmen")

ruta_norte.repartidor = repartidor_1
ruta_norte.agregar_envio(paquete_1)
ruta_norte.agregar_envio(paquete_2)
ruta_norte.agregar_envio(documento_1)

ruta_norte.mostrar_resumen()

print("\n=== 5. PRUEBA DE DESTRUCTORES (__del__) ===")
del paquete_1
del paquete_2
del documento_1
del ruta_norte
del repartidor_1
