class ContratoRenta:
    def __init__(self, folio, total):
        self.folio = folio
        self.total = total

    def __add__(self, otro_contrato):
        return self.total + otro_contrato.total

    def __sub__(self, monto_devolucion):
        return self.total - monto_devolucion.total


contrato_1 = ContratoRenta(101, 1500)
contrato_2 = ContratoRenta(102, 2300)

suma_totales = contrato_1 + contrato_2

print(f"La suma de ambas rentas es: ${suma_totales}")

total_acumulado = ContratoRenta(103, suma_totales)
devolucion = total_acumulado - contrato_1
print(f"Total después de devolver la primera renta: ${devolucion}")