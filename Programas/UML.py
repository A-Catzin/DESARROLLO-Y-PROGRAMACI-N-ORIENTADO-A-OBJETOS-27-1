class CuentaBancaria:
    """Clase base que representa una cuenta bancaria general."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self._saldo = max(0.0, saldo_inicial)  # Atributo protegido

    def depositar(self, monto: float) -> None:
        if monto > 0:
            self._saldo += monto
            print(f"Depósito de ${monto:.2f} exitoso en la cuenta de {self.titular}.")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def retirar(self, monto: float) -> bool:
        if 0 < monto <= self._saldo:
            self._saldo -= monto
            print(f"Retiro de ${monto:.2f} procesado. Saldo restante: ${self._saldo:.2f}")
            return True
        print(f"Fondos insuficientes o monto inválido para {self.titular}.")
        return False

    def consultar_saldo(self) -> float:
        return self._saldo


class CuentaAhorros(CuentaBancaria):
    """Clase derivada que hereda de CuentaBancaria y agrega tasa de interés."""

    def __init__(self, titular: str, saldo_inicial: float = 0.0, interes_anual: float = 0.05):
        super().__init__(titular, saldo_inicial)
        self.interes_anual = interes_anual

    def aplicar_interes(self) -> None:
        ganancia = self._saldo * self.interes_anual
        self._saldo += ganancia
        print(f"Interés anual aplicado (+${ganancia:.2f}). Nuevo saldo: ${self._saldo:.2f}")


# Demostración del funcionamiento
if __name__ == "__main__":
    cuenta = CuentaAhorros(titular="Carlos Méndez", saldo_inicial=1000.0, interes_anual=0.04)
    
    print(f"Titular: {cuenta.titular} | Saldo inicial: ${cuenta.consultar_saldo():.2f}")
    cuenta.depositar(500.0)
    cuenta.retirar(200.0)
    cuenta.aplicar_interes()
    print(f"Saldo final: ${cuenta.consultar_saldo():.2f}")