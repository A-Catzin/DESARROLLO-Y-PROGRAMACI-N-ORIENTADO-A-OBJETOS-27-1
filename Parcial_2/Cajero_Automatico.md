# Práctica: Cajero Automático en Python
**Materia:** Desarrollo y Programación Orientada a Objetos  
**Parcial 2**

---

## 1. Conceptos Clave
* **Constructor (`__init__`)**: Inicializa la cuenta (titular, saldo y PIN) y se ejecuta al crear la instancia.
* **Destructor (`__del__`)**: Se invoca al destruir el objeto con `del` o al terminar el programa, simulando el cierre de sesión.
* **Encapsulamiento**: Se declaran atributos privados (`__saldo` y `__pin`) con doble guion bajo (`__`), controlando su acceso mediante métodos públicos con validaciones.

---

## 2. Código Fuente (`Cajero_Automatico.py`)

```python
class CajeroAutomatico:
    # Constructor
    def __init__(self, titular, saldo_inicial, pin):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado (Encapsulamiento)
        self.__pin = pin              # Atributo privado (Encapsulamiento)
        print(f"Bienvenido {self.titular}. Cuenta iniciada con éxito.")

    # Destructor
    def __del__(self):
        print(f"Cerrando sesión de {self.titular}. ¡Gracias por usar el cajero automático!")

    def consultar_saldo(self, pin_ingresado):
        if pin_ingresado == self.__pin:
            print(f"Saldo actual de {self.titular}: ${self.__saldo}")
            return self.__saldo
        else:
            print("PIN incorrecto. No se puede mostrar el saldo.")

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito de ${monto} exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("El monto a depositar debe ser mayor a $0.")

    def retirar(self, monto, pin_ingresado):
        if pin_ingresado != self.__pin:
            print("PIN incorrecto. Retiro cancelado.")
            return

        if monto <= 0:
            print("El monto a retirar debe ser mayor a $0.")
        elif monto > self.__saldo:
            print("Fondos insuficientes. No se puede realizar el retiro.")
        else:
            self.__saldo -= monto
            print(f"Retiro de ${monto} exitoso. Saldo restante: ${self.__saldo}")


if __name__ == "__main__":
    # Creación del objeto (Constructor)
    mi_cajero = CajeroAutomatico("Angel", 1000, 1234)

    mi_cajero.consultar_saldo(1234)
    mi_cajero.consultar_saldo(9999)

    mi_cajero.depositar(500)
    mi_cajero.depositar(-50)

    mi_cajero.retirar(300, 1234)
    mi_cajero.retirar(2000, 1234)
    mi_cajero.retirar(100, 0000)

    # Demostración de encapsulamiento
    try:
        print(mi_cajero.__saldo)
    except AttributeError:
        print("Acceso denegado: No se puede acceder a '.__saldo' directamente porque es privado.")

    # Eliminación del objeto (Destructor)
    del mi_cajero
```

---

## 3. Salida en Consola

```text
Bienvenido Angel. Cuenta iniciada con éxito.
Saldo actual de Angel: $1000
PIN incorrecto. No se puede mostrar el saldo.
Depósito de $500 exitoso. Nuevo saldo: $1500
El monto a depositar debe ser mayor a $0.
Retiro de $300 exitoso. Saldo restante: $1200
Fondos insuficientes. No se puede realizar el retiro.
PIN incorrecto. Retiro cancelado.
Acceso denegado: No se puede acceder a '.__saldo' directamente porque es privado.
Cerrando sesión de Angel. ¡Gracias por usar el cajero automático!
```
