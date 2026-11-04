# Fases 2 y 3: Análisis y Diseño · "Riviera Express"

## Fase 2: Análisis

### 2.1 Identificación de Objetos / Clases Candidatas

1. **`Envio` (Superclase)**:
   - **Atributos**: `+codigo`, `-peso`, `-distancia`.
   - **Responsabilidades**: Validar que peso y distancia no sean negativos (`get`/`set`), calcular el costo base y sobrecargar el operador `+` (`__add__`) para sumar el costo de dos envíos.
2. **`Paquete` (Subclase de `Envio`)**:
   - **Atributos propios**: `-volumen`.
   - **Responsabilidades**: Validar que el volumen no sea negativo (`@property`) y calcular el costo sumando el volumen al costo base heredado.
3. **`Documento` (Subclase de `Envio`)**:
   - **Atributos propios**: `+urgente`.
   - **Responsabilidades**: Calcular el costo sumando un cargo extra si el documento es urgente.
4. **`Repartidor`**:
   - **Atributos**: `+nombre`, `+vehiculo`, `-id_repartidor`.
   - **Responsabilidades**: Guardar los datos del repartidor responsable y proteger su ID con `get`/`set`.
5. **`HojaRuta`**:
   - **Atributos**: `+folio`, `+zona`, `-repartidor`, `-envios`.
   - **Responsabilidades**: Agrupar varios paquetes/documentos, asignar un repartidor responsable (`@property`) y mostrar el resumen de la ruta.

### 2.2 Diagrama de Casos de Uso

```mermaid
flowchart LR
    Operador["👤 Operador"]
    RepartidorActor["👤 Repartidor"]

    subgraph Sistema["Sistema de Envíos 'Riviera Express'"]
        UC1(["Registrar Paquete o Documento"])
        UC2(["Validar Peso, Volumen y Distancia > 0"])
        UC3(["Calcular Costo de Envío"])
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
