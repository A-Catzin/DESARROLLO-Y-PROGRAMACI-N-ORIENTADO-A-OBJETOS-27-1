class ContratoRenta:
    def __init__(self, folio, total):
        self.folio = folio
        self.total = total

    # Sin __add__: método normal para sumar contratos
    def sumar_contrato(self, otro_contrato):
        return self.total + otro_contrato.total


# --- PRUEBA DE USO ---
contrato_1 = ContratoRenta(101, 1500)
contrato_2 = ContratoRenta(102, 2300)

suma_totales = contrato_1.sumar_contrato(contrato_2)

print(f"La suma de ambas rentas es: ${suma_totales}")
# Imprime: La suma de ambas rentas es: $3800
