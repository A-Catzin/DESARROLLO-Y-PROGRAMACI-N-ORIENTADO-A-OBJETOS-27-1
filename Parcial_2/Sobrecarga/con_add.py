class ContratoRenta:
    def __init__(self, folio, total):
        self.folio = folio
        self.total = total

    # Sobrecargamos el operador '+' usando el método mágico __add__
    def __add__(self, otro_contrato):
        # Sumamos el total del contrato actual con el total del otro
        return self.total + otro_contrato.total


# --- PRUEBA DE USO ---
contrato_1 = ContratoRenta(101, 1500)
contrato_2 = ContratoRenta(102, 2300)

suma_totales = contrato_1 + contrato_2

print(f"La suma de ambas rentas es: ${suma_totales}")
# Imprime: La suma de ambas rentas es: $3800
