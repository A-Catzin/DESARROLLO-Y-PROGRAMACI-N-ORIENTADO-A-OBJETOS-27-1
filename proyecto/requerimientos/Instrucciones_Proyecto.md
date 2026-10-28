# Instrucciones y Reglas del Proyecto · Desarrollo POO

## Caso de Estudio Asignado (#8)
**Sistema de Gestión de Envíos para Paquetería Local ("Riviera Express")**
> **Caso de estudio**: "Riviera Express" es una empresa de envíos urbanos que transporta paquetes y documentos pequeños. Necesitan un sistema que calcule el costo de envío basándose en el peso, volumen y la distancia de entrega del paquete. El software debe validar que no existan pesos o medidas negativas, permitir agrupar varios paquetes bajo una misma hoja de ruta de entrega y asignar un repartidor responsable para optimizar las operaciones diarias.

---

## Fechas de Evaluación
- **Miércoles**: Examen
- **Jueves**: Entrega de Proyecto

---

## 1. Fases del Proyecto (Ciclo de Desarrollo)

El proyecto debe documentar y cumplir las siguientes **4 fases** en orden:

1. **Requisitos**:
   - Requisitos **Funcionales** (qué hace el sistema).
   - Requisitos **No Funcionales** (restricciones, rendimiento, reglas operativas).
2. **Análisis**:
   - Identificación de **Objetos / Clases candidatas**.
   - **Diagrama de Casos de Uso** (actores e interacciones principales).
3. **Diseño**:
   - **Diagrama de Clases UML**:
     - Nombre de la clase, atributos y métodos.
     - Visibilidad: `+` público, `-` privado.
     - Relaciones (herencia, asociación/composición).
4. **Implementación**:
   - **Estructura modular**: `1 Archivo = 1 Clase`.
   - **Archivo principal (`main.py`)**: creación de objetos (instancias) y datos de prueba.
   - **Importación estándar**: `from Archivo import Clase`.

---

## 2. Reglas Técnicas de Implementación (Lo que DEBE contener)

- [x] **Constructores y Destructores**: uso de `__init__` y `__del__` en todas las clases.
- [x] **Herencia**: `Envio` (superclase) $\rightarrow$ `Paquete` y `Documento` (subclases).
- [x] **Encapsulamiento** (aplicar ambos métodos vistos en clase):
  1. Métodos tradicionales `get` y `set` (en `Envio.py` y `Repartidor.py`).
  2. Decoradores `@property` y `@setter` (en `Paquete.py`, `Documento.py` y `HojaRuta.py`).
- [x] **Sobrecarga**: sobrecarga de métodos (`calcular_costo(self, seguro=0.0)`) y sobrecarga de operadores (`__add__`, `__radd__`, `__sub__`, `__rsub__` en `Envio.py`).
- [x] **Estructura 1 Archivo / 1 Clase**: cada clase en su propio `.py` (`Envio.py`, `Paquete.py`, `Documento.py`, `Repartidor.py`, `HojaRuta.py`) y las pruebas en `main.py`.
- [x] **Datos de prueba**: instanciación y demostración funcional completa en `main.py`.

---

## 3. Restricciones (Lo que NO se debe agregar)

- **Sin manejo de errores ni excepciones**: NO usar bloques `try` / `except` ni lanzar excepciones (`raise`).
- Mantener el código directo y apegado únicamente a los conceptos vistos en clase.
