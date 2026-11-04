# Fases 2 y 3: Análisis y Diseño · "Riviera Express"

## Fase 2: Análisis

### 2.1 Lista de Objetos Identificados en el Dominio

1. **`Envio` (Superclase)**:
   - **Atributos**: `+codigo`, `-peso`, `-distancia`.
   - **Responsabilidades**: Inicializar y destruir el objeto (`__init__`, `__del__`), validar que peso y distancia no sean negativos (`get`/`set`), calcular el costo base y sobrecargar los 4 operadores aritméticos (`+`, `-`, `*`, `/`).
2. **`Paquete` (Subclase de `Envio`)**:
   - **Atributos propios**: `-volumen`.
   - **Responsabilidades**: Heredar de `Envio`, validar que el volumen no sea negativo mediante `@property` y calcular el costo sumando el volumen al costo base.
3. **`Documento` (Subclase de `Envio`)**:
   - **Atributos propios**: `+urgente`.
   - **Responsabilidades**: Heredar de `Envio` y calcular el costo sumando un cargo adicional cuando el documento es urgente.
4. **`Repartidor`**:
   - **Atributos**: `+nombre`, `+vehiculo`, `-id_repartidor`.
   - **Responsabilidades**: Representar al repartidor responsable de la entrega y encapsular su identificador mediante `get`/`set`.
5. **`HojaRuta`**:
   - **Atributos**: `+folio`, `+zona`, `-repartidor`, `-envios`.
   - **Responsabilidades**: Encapsular al repartidor asignado mediante `@property`, agrupar múltiples paquetes y documentos en una lista y mostrar en pantalla los datos de la ruta.

### 2.2 Diagrama de Casos de Uso

```mermaid
flowchart LR
    Operador["👤 Operador"]
    RepartidorActor["👤 Repartidor"]

    subgraph Sistema["Sistema de Envíos 'Riviera Express'"]
        UC1(["Registrar Paquete o Documento"])
        UC2(["Validar Peso, Volumen y Distancia > 0"])
        UC3(["Calcular y Operar Costos (+, -, *, /)"])
        UC4(["Agrupar Envíos en Hoja de Ruta"])
        UC5(["Asignar Repartidor"])
        UC6(["Mostrar Resumen de Hoja de Ruta"])
    end

    Operador --> UC1
    Operador --> UC3
    Operador --> UC4
    Operador --> UC5
    Operador --> UC6
    RepartidorActor --> UC6

    UC1 -. "include" .-> UC2
```

---

## Fase 3: Diseño

### 3.1 Diagrama de Clases UML

```mermaid
classDiagram
    direction TB

    class Envio {
        +String codigo
        -float peso
        -float distancia
        +__init__(codigo, peso, distancia)
        +__del__()
        +get_peso()
        +set_peso(nuevo_peso)
        +get_distancia()
        +set_distancia(nueva_distancia)
        +calcular_costo()
        +__add__(otro_envio)
        +__sub__(otro_envio)
        +__mul__(otro_envio)
        +__truediv__(otro_envio)
    }

    class Paquete {
        -float volumen
        +__init__(codigo, peso, distancia, volumen)
        +__del__()
        +volumen()
        +volumen(nuevo_volumen)
        +calcular_costo()
    }

    class Documento {
        +bool urgente
        +__init__(codigo, peso, distancia, urgente)
        +__del__()
        +calcular_costo()
    }

    class Repartidor {
        +String nombre
        +String vehiculo
        -String id_repartidor
        +__init__(id_repartidor, nombre, vehiculo)
        +__del__()
        +get_id_repartidor()
        +set_id_repartidor(nuevo_id)
    }

    class HojaRuta {
        +String folio
        +String zona
        -Repartidor repartidor
        -List envios
        +__init__(folio, zona)
        +__del__()
        +repartidor()
        +repartidor(nuevo_repartidor)
        +agregar_envio(envio)
        +mostrar_ruta()
    }

    Envio <|-- Paquete : Herencia
    Envio <|-- Documento : Herencia
    HojaRuta o-- Envio : Agrupa
    HojaRuta --> Repartidor : Asigna
```
