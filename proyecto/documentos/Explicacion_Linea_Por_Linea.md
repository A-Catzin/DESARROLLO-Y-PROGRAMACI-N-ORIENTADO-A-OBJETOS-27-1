# Guía Explicada Línea por Línea: Proyecto "Riviera Express"

Este documento explica **exactamente qué hace cada archivo y cada línea de código** del proyecto para que cualquier integrante del equipo pueda exponerlo y responder preguntas del profesor.

---

## 1. Resumen Rápido: ¿Cómo cumplimos lo que pidió el profesor?

| Concepto pedido | ¿Dónde está en nuestro código? |
| :--- | :--- |
| **1 Archivo = 1 Clase** | `Envio.py`, `Paquete.py`, `Documento.py`, `Repartidor.py`, `HojaRuta.py` |
| **1 `main` = Objetos** | `main.py` importa las clases con `from Archivo import Clase` y crea los objetos |
| **Constructores y Destructores** | Todas las clases tienen `def __init__` y `def __del__` |
| **Herencia** | `Paquete` y `Documento` heredan de la clase padre `Envio` |
| **Encapsulamiento 1 (`get`/`set`)** | En `Envio.py` (`get_peso`, `set_peso`, `get_distancia`, `set_distancia`) y `Repartidor.py` |
| **Encapsulamiento 2 (`@property`)** | En `Paquete.py` (`@property def volumen`) y `HojaRuta.py` (`@property def repartidor`) |
| **Sobrecarga de operadores** | En `Envio.py` con `def __add__` para sumar dos envíos usando `+` (`paquete_1 + paquete_2`) |
| **Sin `try/except`** | Validamos que no haya números negativos usando solo `if nuevo_peso > 0:` |

---

## 2. Explicación Archivo por Archivo (Línea por Línea)

### Archivo 1: `Envio.py` (La Clase Padre / Superclase)

Representa cualquier envío de la paquetería. De aquí van a heredar `Paquete` y `Documento`.

```python
class Envio:
    def __init__(self, codigo, peso, distancia):
        self.codigo = codigo          # Público (+)
        self.__peso = peso            # Privado (-)
        self.__distancia = distancia  # Privado (-)
```
* **`class Envio:`**: Define la clase padre.
* **`def __init__(self, codigo, peso, distancia):`**: Es el **constructor**. Se ejecuta automáticamente cuando creamos un envío.
* **`self.codigo = codigo`**: Atributo **público** (no lleva guiones bajos). Cualquiera puede leerlo directamente.
* **`self.__peso` y `self.__distancia`**: Atributos **privados** (llevan doble guion bajo `__`). Nadie puede modificarlos directamente desde afuera; obligamos a pasar por los métodos `set` para evitar valores negativos.

```python
    def __del__(self):
        print(f"Envío {self.codigo} eliminado")
```
* **`def __del__(self):`**: Es el **destructor**. Se ejecuta cuando borramos el objeto con `del` o cuando termina el programa.

```python
    # Encapsulamiento 1: get y set
    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self.__peso = nuevo_peso
        else:
            print("El peso no puede ser negativo")
```
* **`get_peso(self)`**: Método **getter** para leer el valor privado `__peso`.
* **`set_peso(self, nuevo_peso)`**: Método **setter** para cambiar el peso. Antes de guardarlo, el `if nuevo_peso > 0:` revisa que sea positivo. Si intentan meter `-5`, muestra `"El peso no puede ser negativo"` y **no lo cambia**. (Lo mismo hacen `get_distancia` y `set_distancia`).

```python
    def calcular_costo(self):
        return (self.__peso * 10) + (self.__distancia * 5)

    # Sobrecarga del operador '+' para sumar costos de dos envíos
    def __add__(self, otro_envio):
        return self.calcular_costo() + otro_envio.calcular_costo()
```
* **`calcular_costo(self)`**: Calcula el costo base: cobra **$10 por cada kg de peso** más **$5 por cada km de distancia**.
* **`def __add__(self, otro_envio):`**: Es la **sobrecarga del operador `+`**. Le enseña a Python qué hacer cuando escribimos `paquete_1 + paquete_2`: suma el costo del primer envío más el costo del segundo.

---

### Archivo 2: `Paquete.py` (Subclase con Herencia y `@property`)

Representa una caja o paquete que, además de peso y distancia, tiene **volumen**.

```python
from Envio import Envio


class Paquete(Envio):
    def __init__(self, codigo, peso, distancia, volumen):
        super().__init__(codigo, peso, distancia)
        self.__volumen = volumen  # Privado (-)
```
* **`from Envio import Envio`**: Importa la clase padre desde su archivo.
* **`class Paquete(Envio):`**: Los paréntesis `(Envio)` indican **Herencia**: `Paquete` es hijo de `Envio`.
* **`super().__init__(codigo, peso, distancia)`**: Llama al constructor del padre (`Envio`) para que guarde el código, el peso y la distancia sin repetir código.
* **`self.__volumen = volumen`**: Guarda el atributo privado exclusivo de los paquetes.

```python
    # Encapsulamiento 2: @property
    @property
    def volumen(self):
        return self.__volumen

    @volumen.setter
    def volumen(self, nuevo_volumen):
        if nuevo_volumen > 0:
            self.__volumen = nuevo_volumen
        else:
            print("El volumen no puede ser negativo")
```
* **`@property`**: Es la segunda forma de encapsulamiento vista en clase. Permite leer `__volumen` escribiendo `paquete_1.volumen` como si fuera un atributo normal.
* **`@volumen.setter`**: Se activa cuando hacemos `paquete_1.volumen = nuevo_valor`. Valida con `if nuevo_volumen > 0:` que el volumen no sea negativo.

```python
    def calcular_costo(self):
        return super().calcular_costo() + (self.__volumen * 20)
```
* **`calcular_costo(self)`**: Toma el costo base del padre (`super().calcular_costo()`) y le suma **$20 por cada unidad de volumen**.

---

### Archivo 3: `Documento.py` (Segunda Subclase con Herencia)

Representa un sobre o documento pequeño.

```python
from Envio import Envio


class Documento(Envio):
    def __init__(self, codigo, peso, distancia, urgente):
        super().__init__(codigo, peso, distancia)
        self.urgente = urgente  # Público (+)

    def __del__(self):
        print(f"Documento {self.codigo} eliminado")

    def calcular_costo(self):
        costo = super().calcular_costo()
        if self.urgente:
            return costo + 30
        return costo
```
* Hereda de `Envio` igual que `Paquete`.
* **`self.urgente`**: Es un booleano (`True` o `False`) público.
* **`calcular_costo(self)`**: Si el documento es urgente (`if self.urgente:`), le suma **$30 extra** al costo base.

---

### Archivo 4: `Repartidor.py` (Clase del Repartidor Responsable)

```python
class Repartidor:
    def __init__(self, id_repartidor, nombre, vehiculo):
        self.nombre = nombre                 # Público (+)
        self.vehiculo = vehiculo             # Público (+)
        self.__id_repartidor = id_repartidor # Privado (-)

    def __del__(self):
        print(f"Repartidor {self.nombre} eliminado")

    def get_id_repartidor(self):
        return self.__id_repartidor

    def set_id_repartidor(self, nuevo_id):
        self.__id_repartidor = nuevo_id
```
* Guarda el `nombre` y `vehiculo` como atributos públicos (`+`) porque se consultan todo el tiempo en la hoja de ruta, y protege `__id_repartidor` como privado (`-`) con su `get` y `set`.

---

### Archivo 5: `HojaRuta.py` (Agrupa los Envíos y Asigna al Repartidor)

Cumple el requisito de agrupar varios paquetes en una misma ruta y asignarle un repartidor.

```python
class HojaRuta:
    def __init__(self, folio, zona):
        self.folio = folio        # Público (+)
        self.zona = zona          # Público (+)
        self.__repartidor = None  # Privado (-)
        self.__envios = []        # Privado (-): Lista vacía para guardar paquetes
```
* **`self.__envios = []`**: Es una lista privada donde iremos metiendo los paquetes y documentos de esa ruta.

```python
    @property
    def repartidor(self):
        return self.__repartidor

    @repartidor.setter
    def repartidor(self, nuevo_repartidor):
        self.__repartidor = nuevo_repartidor

    def agregar_envio(self, envio):
        self.__envios.append(envio)

    def mostrar_ruta(self):
        print(f"--- Hoja de Ruta: {self.folio} ({self.zona}) ---")
        print(f"Repartidor: {self.__repartidor.nombre} - Vehículo: {self.__repartidor.vehiculo}")
        print(f"Cantidad de envíos: {len(self.__envios)}")
```
* **`@repartidor.setter`**: Permite asignar el objeto `Repartidor` a la hoja de ruta haciendo `ruta_1.repartidor = repartidor_1`.
* **`agregar_envio(self, envio)`**: Usa `.append(envio)` para meter un `Paquete` o `Documento` a la lista de la ruta.
* **`mostrar_ruta(self)`**: Imprime el folio, la zona, el nombre y vehículo del repartidor, y cuántos envíos lleva en total (`len(self.__envios)`).

---

### Archivo 6: `main.py` (Creación de Objetos y Datos de Prueba)

Es el archivo que se ejecuta. Conecta todas las clases y demuestra que todo funciona:

```python
from Paquete import Paquete
from Documento import Documento
from Repartidor import Repartidor
from HojaRuta import HojaRuta
```
* Cumple la regla de pizarrón: **`from Archivo import Clase`**.

```python
# 1. Crear objetos (Herencia de Envio)
paquete_1 = Paquete("PAQ-01", 5, 10, 2)
paquete_2 = Paquete("PAQ-02", 3, 8, 1)
doc_1 = Documento("DOC-01", 1, 4, True)

print(f"Costo Paquete 1: ${paquete_1.calcular_costo()}")
print(f"Costo Paquete 2: ${paquete_2.calcular_costo()}")
print(f"Costo Documento 1: ${doc_1.calcular_costo()}")
```
* Crea dos paquetes y un documento urgente.
* Por ejemplo, en `paquete_1`: peso `5 * 10 = 50`, distancia `10 * 5 = 50`, volumen `2 * 20 = 40`. Total = **`$140`**.

```python
# 2. Probar encapsulamiento y validación de negativos (get/set y @property)
paquete_1.set_peso(-5)     # No permite negativo (get/set)
paquete_1.volumen = -3     # No permite negativo (@property)

paquete_1.set_peso(6)      # Cambio válido con set
paquete_1.volumen = 3      # Cambio válido con @property
print(f"Nuevo costo Paquete 1: ${paquete_1.calcular_costo()}")
```
* Primero intentamos meter valores negativos (`-5` y `-3`) para demostrarle al profesor que el sistema los rechaza.
* Luego metemos valores positivos (`6` y `3`) y el costo sube a **`$170`**.

```python
# 3. Sobrecarga de operador '+' (__add__)
suma_envios = paquete_1 + paquete_2
print(f"Suma de Paquete 1 y Paquete 2: ${suma_envios}")
```
* Usa el signo `+` entre dos objetos gracias a `__add__`. Suma `$170 + $90 = $260`.

```python
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
```
* Crea al repartidor `"Carlos"`, crea la hoja de ruta `"RUTA-100"`, le asigna a Carlos, mete los 3 envíos a la hoja de ruta y muestra el resumen.
* Finalmente, `del` destruye los objetos y dispara los mensajes de `__del__`.

---

## 3. Salida Exacta en Consola al Ejecutar `main.py`

```text
Costo Paquete 1: $140
Costo Paquete 2: $90
Costo Documento 1: $60
El peso no puede ser negativo
El volumen no puede ser negativo
Nuevo costo Paquete 1: $170
Suma de Paquete 1 y Paquete 2: $260
--- Hoja de Ruta: RUTA-100 (Centro) ---
Repartidor: Carlos - Vehículo: Moto
Cantidad de envíos: 3
Hoja de ruta RUTA-100 eliminada
Documento DOC-01 eliminado
Paquete PAQ-02 eliminado
Paquete PAQ-01 eliminado
Repartidor Carlos eliminado
```
