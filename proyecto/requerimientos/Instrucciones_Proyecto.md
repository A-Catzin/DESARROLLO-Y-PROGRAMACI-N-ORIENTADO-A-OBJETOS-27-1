# Instrucciones y Reglas de Entrega del Proyecto · Desarrollo POO

## Caso de Estudio Asignado (#8)
**Sistema de Gestión de Envíos para Paquetería Local ("Riviera Express")**
> "Riviera Express" es una empresa de envíos urbanos que transporta paquetes y documentos pequeños. Necesitan un sistema que calcule el costo de envío basándose en el peso, volumen y la distancia de entrega del paquete. El software debe validar que no existan pesos o medidas negativas, permitir agrupar varios paquetes bajo una misma hoja de ruta de entrega y asignar un repartidor responsable para optimizar las operaciones diarias.

---

## Parte 1. Estructura del Documento PDF (Arial #12, interlineado 1.15–1.5, justificado)

1. **Portada Institucional**:
   - Nombre de la institución educativa y materia/asignatura.
   - Título del proyecto.
   - Nombre completo de los integrantes del equipo.
   - Fecha de entrega y grupo.
2. **Planteamiento del Problema**:
   - Descripción clara de la problemática a resolver y alcance de la solución.
3. **Fases del Desarrollo Orientado a Objetos**:
   - **Fase 1 - Requisitos**: Funcionales y No Funcionales con su **justificación técnica**.
   - **Fase 2 - Análisis**: Diagrama de Casos de Uso y Lista de objetos identificados.
   - **Fase 3 - Diseño**: Diagrama de Clases UML con visibilidad (`+`, `-`).
   - **Fase 4 - Implementación**: Capturas de pantalla del código y de la ejecución.

---

## Parte 2. Especificaciones del Código Fuente (Python)

- [x] **1 clase = 1 archivo** (`Envio.py`, `Paquete.py`, `Documento.py`, `Repartidor.py`, `HojaRuta.py`).
- [x] **Mínimo de clases**: $\text{Clases} \ge \text{Integrantes}$.
- [x] **1 archivo `main.py`**: Creación de objetos y operaciones.
- [x] **Constructores y Destructores**: `__init__` y `__del__` en todas las clases.
- [x] **Herencia**: `Paquete` y `Documento` heredan de `Envio`.
- [x] **Encapsulamiento**: 2 `@property` (`volumen` en `Paquete`, `repartidor` en `HojaRuta`) + `get`/`set` (`Envio`, `Repartidor`).
- [x] **Sobrecarga de 4 operadores (`+`, `-`, `*`, `/`)**: `__add__`, `__sub__`, `__mul__`, `__truediv__` en `Envio.py`.
- [x] **Sin comentarios**: Cero líneas con `#` dentro de los archivos `.py`.
- [x] **Sin Excepciones/Errores**: Sin `try`/`except` y ejecución limpia de principio a fin.
