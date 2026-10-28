# Fases 2 y 3: Análisis y Diseño · "Riviera Express"

## Fase 2: Análisis

### 2.1 Identificación de Objetos / Clases Candidatas

1. **`Envio` (Superclase)**:
   - **Atributos**: `codigo`, `peso`, `distancia`.
   - **Responsabilidades**: Validar que peso y distancia no sean negativos (`get`/`set`), calcular el costo base por peso y distancia, y sobrecargar los operadores `+` y `-` para sumar o descontar envíos.
2. **`Paquete` (Subclase de `Envio`)**:
   - **Atributos propios**: `volumen`.
   - **Responsabilidades**: Validar que el volumen no sea negativo (`@property`) y calcular el costo total sumando el cargo por volumen al costo base heredado.
3. **`Documento` (Subclase de `Envio`)**:
   - **Atributos propios**: `urgente`.
   - **Responsabilidades**: Gestionar el estado de urgencia (`@property`) y calcular el costo sumando una tarifa adicional si el documento es urgente.
4. **`Repartidor`**:
   - **Atributos**: `id_repartidor`, `nombre`, `vehiculo`.
   - **Responsabilidades**: Almacenar y validar los datos del repartidor responsable (`get`/`set`) y mostrar su ficha de identificación.
5. **`HojaRuta`**:
   - **Atributos**: `folio`, `zona`, `repartidor`, `envios`.
   - **Responsabilidades**: Agrupar varios envíos, asignar un repartidor responsable, calcular el peso y costo total acumulado de la ruta y mostrar el resumen diario.

### 2.2 Diagrama de Casos de Uso

```mermaid
flowchart LR
    Operador["👤 Operador Logístico"]
    RepartidorActor["👤 Repartidor"]

    subgraph Sistema["Sistema de Gestión de Envíos 'Riviera Express'"]
        UC1(["Registrar Paquete o Documento"])
        UC2(["Validar Peso, Volumen y Distancia > 0"])
        UC3(["Calcular Costo de Envío"])
        UC4(["Crear Hoja de Ruta y Agrupar Envíos"])
        UC5(["Asignar Repartidor Responsable"])
        UC6(["Consultar Resumen y Total de Ruta"])
    end

    Operador --> UC1
    Operador --> UC3
    Operador --> UC4
    Operador --> UC5
    Operador --> UC6
    RepartidorActor --> UC6

    UC1 -. "include" .-> UC2
    UC4 -. "include" .-> UC3
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
        +get_peso() float
        +set_peso(nuevo_peso) void
        +get_distancia() float
        +set_distancia(nueva_distancia) void
        +calcular_costo(seguro) float
        +__add__(otro_envio) float
        +__radd__(monto_acumulado) float
        +__sub__(otro_envio) float
        +__rsub__(monto_acumulado) float
    }

    class Paquete {
        +String descripcion
        -float volumen
        +__init__(codigo, peso, distancia, volumen, descripcion)
        +__del__()
        +volumen() float
        +volumen(nuevo_volumen) void
        +calcular_costo(seguro) float
    }

    class Documento {
        +String tipo_sobre
        -bool urgente
        +__init__(codigo, peso, distancia, urgente, tipo_sobre)
        +__del__()
        +urgente() bool
        +urgente(es_urgente) void
        +calcular_costo(seguro) float
    }

    class Repartidor {
        +String nombre
        +String vehiculo
        -String id_repartidor
        +__init__(id_repartidor, nombre, vehiculo)
        +__del__()
        +get_id_repartidor() String
        +set_id_repartidor(nuevo_id) void
        +mostrar_datos() String
    }

    class HojaRuta {
        +String folio
        +String zona
        -Repartidor repartidor
        -List~Envio~ envios
        +__init__(folio, zona)
        +__del__()
        +repartidor() Repartidor
        +repartidor(nuevo_repartidor) void
        +agregar_envio(envio) void
        +calcular_total_ruta() float
        +calcular_peso_total() float
        +mostrar_resumen() void
    }

    Envio <|-- Paquete : Herencia (es un)
    Envio <|-- Documento : Herencia (es un)
    HojaRuta o-- "1..*" Envio : Agrupa
    HojaRuta --> "1" Repartidor : Asigna responsable
```
