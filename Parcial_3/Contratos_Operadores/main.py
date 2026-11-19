from ContratoRenta import ContratoRenta

# --- 1. SUMA Y RESTA ---
contrato_1 = ContratoRenta(101, 1500)
contrato_2 = ContratoRenta(102, 2300)

suma_totales = contrato_1 + contrato_2
print(f"La suma de ambas rentas es: ${suma_totales}")

devolucion = suma_totales - contrato_1
print(f"Total después de devolver la primera renta: ${devolucion}")

contrato_3 = ContratoRenta(104, 5000)
suma_totales_2 = devolucion + contrato_3
print(f"La suma de la devolución y la tercera renta es: ${suma_totales_2}")

del contrato_1
del contrato_2
del contrato_3

# --- 2. MULTIPLICACIÓN Y DIVISIÓN ---
contrato_1 = ContratoRenta(1, 15)
contrato_2 = ContratoRenta(2, 25)
contrato_3 = ContratoRenta(3, 50)

multiplicacion_1 = contrato_1 * contrato_2
multiplicacion_2 = contrato_2 * contrato_3

print(f"El resultado de la multiplicación de contrato_1 y contrato_2 es: {multiplicacion_1}")
print(f"El resultado de la multiplicación de contrato_2 y contrato_3 es: {multiplicacion_2}")

try:
    division_1 = contrato_2 / contrato_1
    division_2 = contrato_3 / contrato_2

    print(f"El resultado de la división de contrato_2 entre contrato_1 es: {division_1}")
    print(f"El resultado de la división de contrato_3 entre contrato_2 es: {division_2}")
except ZeroDivisionError as e:
    print(f"Error de división: {e}")

# --- 3. PRUEBA DE EXCEPCIONES ---
try:
    contrato_invalido = ContratoRenta(4, -500)
except ValueError as e:
    print(f"Error al crear contrato: {e}")

try:
    contrato_cero = ContratoRenta(5, 0)
    resultado = contrato_1 / contrato_cero
except ZeroDivisionError as e:
    print(f"Error de división: {e}")
