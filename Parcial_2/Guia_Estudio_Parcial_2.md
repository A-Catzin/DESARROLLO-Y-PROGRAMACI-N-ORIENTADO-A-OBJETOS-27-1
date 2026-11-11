# Guía de Estudio Completa · Examen y Proyecto Parcial 2 (POO)

Esta guía resume **todos los conceptos teóricos y prácticos** trabajados en `Parcial_2/` y aplicados en `proyecto/` ("Riviera Express") para el examen y la defensa del proyecto.

---

## 1. Las 4 Fases del Desarrollo Orientado a Objetos

En el pizarrón y en las prácticas vimos que todo sistema POO se construye en **4 fases en orden**:

| Fase | ¿Qué se hace? | Entregable / Ejemplo en clase |
| :--- | :--- | :--- |
| **1. Requisitos** | Definir qué necesita el sistema antes de programar. Se dividen en:<br>• **Funcionales (RF)**: qué hace el sistema (registrar, calcular costo, validar).<br>• **No Funcionales (RNF)**: restricciones y calidad (rendimiento, modularidad, seguridad). | Tablas RF y RNF en [Especificación de Requisitos.md](<Especificación de Requisitos.md>) y [Requisitos_Riviera_Express.md](<../proyecto/requerimientos/Requisitos_Riviera_Express.md>). |
| **2. Análisis** | Identificar los **objetos/clases candidatas** del problema, sus responsabilidades, reglas de negocio y cómo interactúan los actores. | **Lista de Objetos** y **Diagrama de Casos de Uso** en [Analisis_Reservaciones_Hotel.md](<Analisis_Reservaciones_Hotel.md>). |
| **3. Diseño** | Modelar la estructura técnica de las clases (atributos, métodos, visibilidad y relaciones). | **Diagrama de Clases UML** con visibilidad `+` (público) y `-` (privado). |
| **4. Implementación** | Traducir el diseño a código Python siguiendo la regla **`1 Archivo = 1 Clase`** y un archivo **`main.py`** para los objetos. | Carpetas [Aerolinea/](<Aerolinea/main.py>), [Contratos_Operadores/](<Contratos_Operadores/main.py>) y [proyecto/programa/](<../proyecto/programa/main.py>). |

---

## 2. Constructores (`__init__`) y Destructores (`__del__`)

Controlan el **ciclo de vida** de un objeto (cuándo nace y cuándo muere en memoria).

### Concepto
- **Constructor (`__init__`)**: Método especial que se ejecuta **automáticamente al crear (instanciar)** un objeto. Sirve para inicializar sus atributos.
- **Destructor (`__del__`)**: Método especial que se ejecuta **automáticamente cuando el objeto se elimina** de la memoria (usando `del objeto` o cuando termina el programa). Sirve para liberar recursos o cerrar sesiones.

### Ejemplo de clase ([Const_Dest.py](<Const_Dest.py>) y [Cajero_Automatico.py](<Cajero_Automatico.py>))

```python
class Archivo:
    # Constructor: se ejecuta al hacer Archivo("datos.txt")
    def __init__(self, nombre):
        self.nombre = nombre
        print("Objeto creado")

    # Destructor: se ejecuta al hacer del HojaTXT
    def __del__(self):
        print("Objeto eliminado")


HojaTXT = Archivo("datos.txt")  # Imprime: Objeto creado
print(HojaTXT.nombre)           # Imprime: datos.txt
del HojaTXT                     # Imprime: Objeto eliminado
```

---

## 3. Encapsulamiento (Visibilidad `+` Público y `-` Privado)

### Concepto
El **encapsulamiento** consiste en ocultar y proteger los datos sensibles de un objeto para que nadie los modifique directamente desde fuera con valores inválidos (por ejemplo, un saldo negativo o un peso negativo).

- **Público (`+` en UML)**: Se escribe normal (`self.codigo`). Se puede leer y modificar desde fuera.
- **Privado (`-` en UML)**: Se escribe con **doble guion bajo** al inicio (`self.__peso`, `self.__saldo`). Si intentás hacer `objeto.__saldo` desde fuera, Python bloquea el acceso.

En clase vimos **2 formas de acceder y modificar atributos privados**:

### Forma 1: Métodos tradicionales `get` y `set` ([Hospital.py](<Hospital.py>), [Pagos.py](<Pagos.py>), [Envio.py](<../proyecto/programa/Envio.py>))
- **`get_` (Getter)**: Devuelve el valor del atributo privado.
- **`set_` (Setter)**: Modifica el atributo privado, permitiendo validar con un `if` antes de guardarlo.

```python
class Envio:
    def __init__(self, codigo, peso):
        self.codigo = codigo  # Público (+)
        self.__peso = peso    # Privado (-)

    def get_peso(self):
        return self.__peso

    def set_peso(self, nuevo_peso):
        if nuevo_peso > 0:
            self.__peso = nuevo_peso
        else:
            print("El peso no puede ser negativo")


envio_1 = Envio("PAQ-01", 5)
print(envio_1.get_peso())   # Leer con getter -> 5
envio_1.set_peso(-10)       # Imprime: El peso no puede ser negativo
envio_1.set_peso(8)         # Cambio válido -> 8
```

### Forma 2: Decoradores `@property` y `@setter` ([Sistema_Reservaciones_Hotel.py](<Sistema_Reservaciones_Hotel.py>), [Aerolinea/Reserva.py](<Aerolinea/Reserva.py>), [Paquete.py](<../proyecto/programa/Paquete.py>))
Permite usar métodos getter y setter como si fueran un atributo normal (sin escribir paréntesis `()`).

```python
class Habitacion:
    def __init__(self, precio_por_noche):
        self.__precio_por_noche = precio_por_noche  # Privado (-)

    # Getter con @property
    @property
    def precio_por_noche(self):
        return self.__precio_por_noche

    # Setter con @nombre.setter
    @precio_por_noche.setter
    def precio_por_noche(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio_por_noche = nuevo_precio
        else:
            print("El precio debe ser mayor a 0.")


hab = Habitacion(1000)
print(hab.precio_por_noche)  # Llama a @property -> 1000
hab.precio_por_noche = -500  # Llama a @setter -> Imprime error y no lo cambia
hab.precio_por_noche = 1200  # Llama a @setter -> Lo actualiza a 1200
```

> **Diferencia clave para pregunta de examen**:
> Con `get`/`set` llamás funciones con paréntesis: `obj.get_peso()` y `obj.set_peso(10)`.
> Con `@property` accedés y asignás directo con `=`: `obj.volumen` y `obj.volumen = 10`.

---

## 4. Herencia y uso de `super()`

### Concepto
La **herencia** permite crear nuevas clases (**subclases / clases hijas**) a partir de una clase existente (**superclase / clase padre**), heredando sus atributos y métodos para no repetir código. En UML se dibuja con una flecha de punta triangular hueca apuntando al padre (`Envio <|-- Paquete`).

- **`class Hija(Padre):`**: Indica que `Hija` hereda de `Padre`.
- **`super().__init__(...)`**: Llama al constructor de la clase padre para que inicialice los atributos heredados.
- **`super().metodo()`**: Llama a un método de la clase padre para reutilizar su resultado.

### Ejemplo ([Paquete.py](<../proyecto/programa/Paquete.py>) y [Documento.py](<../proyecto/programa/Documento.py>))

```python
class Envio:
    def __init__(self, codigo, peso, distancia):
        self.codigo = codigo
        self.__peso = peso
        self.__distancia = distancia

    def calcular_costo(self):
        return (self.__peso * 10) + (self.__distancia * 5)


class Paquete(Envio):
    def __init__(self, codigo, peso, distancia, volumen):
        # 1. Mandamos codigo, peso y distancia al constructor del padre (Envio)
        super().__init__(codigo, peso, distancia)
        # 2. Guardamos solo el atributo nuevo exclusivo de Paquete
        self.__volumen = volumen

    def calcular_costo(self):
        # Reutilizamos el cálculo del padre y le sumamos el costo del volumen
        return super().calcular_costo() + (self.__volumen * 20)
```

---

## 5. Sobrecarga (De Métodos vs. De Operadores)

¡Mucho cuidado en el examen! Vimos **dos tipos de sobrecarga** distintos:

### 5.1. Sobrecarga de Métodos (Parámetros con valor por defecto)
Visto en [Hotel_Sobrecarga.py](<Hotel_Sobrecarga.py>). Permite llamar a un mismo método con **1 o más argumentos** poniéndole un valor opcional por defecto (`descuento=0` o `precio_maximo=None`).

```python
class Habitacion:
    def __init__(self, numero, precio_por_noche):
        self.numero = numero
        self.precio_por_noche = precio_por_noche

    # Se puede llamar con 1 dato (solo noches) o con 2 datos (noches y descuento)
    def calcularCosto(self, num_noches, descuento=0):
        total = self.precio_por_noche * num_noches
        return total - (total * descuento / 100)


h1 = Habitacion(101, 1000)
print(h1.calcularCosto(3))      # Sin descuento -> 3000
print(h1.calcularCosto(3, 10))  # Con 10% de descuento -> 2700
```

### 5.2. Sobrecarga de Operadores (`+`, `-`, `*`, `/`)
Visto en [Sobrecarga/con_add.py](<Sobrecarga/con_add.py>), [Devolucion.py](<Devolucion.py>), [Contratos_Operadores/ContratoRenta.py](<Contratos_Operadores/ContratoRenta.py>) y [Envio.py](<../proyecto/programa/Envio.py>).

Por defecto, Python no sabe sumar ni restar dos objetos tuyos (`contrato_1 + contrato_2` lanza `TypeError`). Para enseñarle qué hacer con cada signo aritmético, usamos **métodos mágicos (dunder methods)**:

| Operador | Método Mágico en la Clase | ¿Cuándo se activa? | Método reflejado (si hay un número a la izquierda) |
| :---: | :--- | :--- | :--- |
| **`+`** | `def __add__(self, otro):` | `objeto_1 + objeto_2` | `def __radd__(self, monto):` (`3800 + objeto_3`) |
| **`-`** | `def __sub__(self, otro):` | `objeto_1 - objeto_2` | `def __rsub__(self, monto):` (`3800 - objeto_1`) |
| **`*`** | `def __mul__(self, otro):` | `objeto_1 * objeto_2` | `def __rmul__(self, monto):` |
| **`/`** | `def __truediv__(self, otro):` | `objeto_1 / objeto_2` | `def __rtruediv__(self, monto):` |

### Ejemplo completo de los 4 operadores ([ContratoRenta.py](<Contratos_Operadores/ContratoRenta.py>))

```python
class ContratoRenta:
    def __init__(self, folio, total):
        self.folio = folio
        self.total = total

    def __add__(self, otro_contrato):
        return self.total + otro_contrato.total

    def __sub__(self, otro_contrato):
        return self.total - otro_contrato.total

    def __mul__(self, otro_contrato):
        return self.total * otro_contrato.total

    def __truediv__(self, otro_contrato):
        return self.total / otro_contrato.total


c1 = ContratoRenta(101, 2000)
c2 = ContratoRenta(102, 1000)

print(c1 + c2)  # Llama a __add__     -> 3000
print(c1 - c2)  # Llama a __sub__     -> 1000
print(c1 * c2)  # Llama a __mul__     -> 2000000
print(c1 / c2)  # Llama a __truediv__ -> 2.0
```

---

## 6. Arquitectura Modular (`1 Archivo = 1 Clase` y `1 Main`)

Regla obligatoria tanto para el examen práctico como para el proyecto:

1. **Cada clase va en su propio archivo `.py`** (por ejemplo `Pago.py` contiene únicamente `class Pago:` y `Reserva.py` contiene únicamente `class Reserva:`).
2. **Si una clase hija necesita a su clase padre**, la importa arriba:
   ```python
   from Envio import Envio
   ```
3. **El archivo `main.py` NO define clases**: solo importa las clases que va a instanciar, crea los objetos y ejecuta las pruebas:
   ```python
   from Paquete import Paquete
   from Documento import Documento
   from Repartidor import Repartidor
   from HojaRuta import HojaRuta
   ```

---

## 7. Preguntas Típicas de Examen (Repaso Rápido)

1. **¿Qué pasa si intento hacer `contrato_1 + contrato_2` sin definir `__add__`?**
   Python arroja `TypeError: unsupported operand type(s) for +` porque no sabe cómo sumar dos objetos de esa clase (como vimos en [sin_add.py](<Sobrecarga/sin_add.py>)).
2. **¿Cómo se llama el método mágico para la división `/` en Python 3?**
   Se llama **`__truediv__`** (no `__div__`).
3. **¿Cómo se declara un atributo privado en Python y cómo se representa en el Diagrama de Clases UML?**
   En Python con doble guion bajo (`self.__monto`) y en el diagrama UML con un signo menos adelante (`-monto`).
4. **¿Para qué sirve `super().__init__(...)` en una subclase?**
   Para llamar al constructor de la superclase (clase padre) e inicializar los atributos heredados sin repetir código.
5. **¿Cuándo se ejecuta `__init__` y cuándo se ejecuta `__del__`?**
   `__init__` se ejecuta al crear el objeto y `__del__` al eliminarlo con `del objeto` o al finalizar la ejecución del programa.
