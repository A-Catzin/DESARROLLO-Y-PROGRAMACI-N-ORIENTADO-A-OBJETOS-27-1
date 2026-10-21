# Arquitectura UML de una Aerolínea

> **Aclaración:** en UML, el diagrama de distribución también se conoce como **diagrama de despliegue**. Representa dispositivos, servidores, componentes y conexiones de red.

## Sistema propuesto

El sistema permite administrar vuelos, pasajeros, reservas, pagos, check-in y pases de abordar.

## Índice

1. [Fase 1: Identificación de actores](#fase-1-identificación-de-actores)
2. [Fase 2: Diagrama de casos de uso](#fase-2-diagrama-de-casos-de-uso)
3. [Fase 3: Diagrama de clases](#fase-3-diagrama-de-clases)
4. [Fase 4: Diagrama de secuencia](#fase-4-diagrama-de-secuencia)
5. [Fase 5: Diagrama de estados](#fase-5-diagrama-de-estados)
6. [Fase 6: Diagrama de colaboración y comunicación](#fase-6-diagrama-de-colaboración-y-comunicación)
7. [Fase 7: Diagrama de distribución o despliegue](#fase-7-diagrama-de-distribución-o-despliegue)
8. [Diagrama complementario de actividad](#diagrama-complementario-de-actividad)

---

# Fase 1: Identificación de actores

## Actores del sistema

| Actor | Descripción |
| :--- | :--- |
| **Pasajero** | Busca vuelos, realiza reservas, paga boletos y hace check-in. |
| **Agente de ventas** | Realiza reservas y cancelaciones en nombre de los pasajeros. |
| **Administrador** | Gestiona vuelos, aviones, aeropuertos, empleados y pasajeros. |
| **Personal de aeropuerto** | Valida pasajeros, realiza check-in y controla el embarque. |
| **Pasarela de pago** | Procesa pagos, reembolsos y devuelve el resultado de las transacciones. |
| **Servicio de notificaciones** | Envía confirmaciones, cambios de horario y avisos por correo o SMS. |

## Casos de uso principales

1. Buscar vuelos.
2. Consultar disponibilidad de asientos.
3. Comprar boleto.
4. Crear reserva.
5. Pagar reserva.
6. Cancelar reserva.
7. Realizar check-in.
8. Emitir pase de abordar.
9. Gestionar vuelos.
10. Gestionar pasajeros.
11. Enviar confirmaciones y notificaciones.

---

# Fase 2: Diagrama de casos de uso

El caso de uso más importante es **Comprar boleto**, porque integra la búsqueda de vuelos, la selección de un asiento, la reserva, el pago y la confirmación.

```mermaid
flowchart LR
    Pasajero[👤 Pasajero]
    Agente[👤 Agente de ventas]
    Administrador[👤 Administrador]
    Personal[👤 Personal de aeropuerto]
    Pago[⚙️ Pasarela de pago]
    Notificaciones[⚙️ Servicio de notificaciones]

    subgraph Sistema["Sistema de Gestión de Aerolínea"]
        UC1([Buscar vuelos])
        UC2([Consultar asientos])
        UC3([Comprar boleto])
        UC4([Crear reserva])
        UC5([Pagar reserva])
        UC6([Enviar confirmación])
        UC7([Cancelar reserva])
        UC8([Realizar check-in])
        UC9([Emitir pase de abordar])
        UC10([Gestionar vuelos])
        UC11([Gestionar pasajeros])
    end

    Pasajero --> UC1
    Pasajero --> UC2
    Pasajero --> UC3
    Pasajero --> UC7
    Pasajero --> UC8

    Agente --> UC3
    Agente --> UC7
    Administrador --> UC10
    Administrador --> UC11
    Personal --> UC8
    Personal --> UC9
    Pago --> UC5
    Notificaciones --> UC6

    UC3 -. "include" .-> UC1
    UC3 -. "include" .-> UC2
    UC3 -. "include" .-> UC4
    UC3 -. "include" .-> UC5
    UC3 -. "include" .-> UC6
    UC8 -. "include" .-> UC9

    classDef actor fill:#241902,stroke:#ffea00,stroke-width:2px,color:#fffde6;
    classDef principal fill:#051923,stroke:#00f0ff,stroke-width:3px,color:#e0f7ff;
    classDef secundario fill:#240318,stroke:#ff007f,stroke-width:2px,color:#ffe6f2;

    class Pasajero,Agente,Administrador,Personal,Pago,Notificaciones actor;
    class UC3 principal;
    class UC1,UC2,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11 secundario;
```

## Descripción del caso de uso principal: Comprar boleto

1. El pasajero ingresa el origen, el destino y la fecha.
2. El sistema muestra los vuelos disponibles.
3. El pasajero selecciona un vuelo y un asiento.
4. El sistema crea una reserva temporal.
5. El pasajero realiza el pago.
6. La pasarela de pago aprueba o rechaza la transacción.
7. Si el pago es aprobado, el sistema confirma la reserva.
8. El sistema envía la confirmación al pasajero.

---

# Fase 3: Diagrama de clases

```mermaid
classDiagram
    direction TB

    class Usuario:::neonAmarillo {
        <<abstract>>
        #String id
        #String nombre
        #String email
        #String password
        +iniciarSesion() boolean
        +cerrarSesion() void
    }

    class Pasajero:::neonRosa {
        -String numeroPasaporte
        -String telefono
        +buscarVuelos(origen: String, destino: String) List~Vuelo~
        +crearReserva(vuelo: Vuelo) Reserva
        +realizarCheckIn(reserva: Reserva) PaseAbordar
    }

    class Empleado:::neonAmarillo {
        -String numeroEmpleado
        -String cargo
        +gestionarOperacion() void
    }

    class Vuelo:::neonCyan {
        -String numeroVuelo
        -LocalDateTime fechaSalida
        -LocalDateTime fechaLlegada
        -String estado
        +consultarDisponibilidad() List~Asiento~
        +actualizarEstado(estado: String) void
    }

    class Aeropuerto:::neonMorado {
        -String codigoIATA
        -String nombre
        -String ciudad
        +consultarVuelos() List~Vuelo~
    }

    class Avion:::neonMorado {
        -String matricula
        -String modelo
        -int capacidad
        +consultarAsientos() List~Asiento~
    }

    class Asiento:::neonCyan {
        -String numero
        -String clase
        -String estado
        +reservar() boolean
        +liberar() void
    }

    class Reserva:::neonRosa {
        -String codigo
        -LocalDateTime fechaCreacion
        -String estado
        -double total
        +confirmar() void
        +cancelar() boolean
        +calcularTotal() double
    }

    class Pago:::neonVerde {
        -String idPago
        -double monto
        -String metodo
        -String estado
        +procesar() boolean
        +reembolsar() boolean
    }

    class PaseAbordar:::neonVerde {
        -String codigo
        -LocalDateTime fechaEmision
        +generar() String
        +validar() boolean
    }

    Usuario <|-- Pasajero : es_un
    Usuario <|-- Empleado : es_un

    Pasajero "1" --> "0..*" Reserva : realiza
    Reserva "1" --> "1" Vuelo : corresponde_a
    Reserva "1" o-- "1..*" Asiento : selecciona
    Reserva "1" *-- "0..1" Pago : registra
    Reserva "1" *-- "0..1" PaseAbordar : genera

    Vuelo "1" --> "1" Avion : utiliza
    Vuelo "1" --> "1" Aeropuerto : tiene_origen
    Vuelo "1" --> "1" Aeropuerto : tiene_destino
    Avion "1" *-- "1..*" Asiento : contiene

    classDef neonAmarillo fill:#241902,stroke:#ffea00,stroke-width:2.5px,color:#fffde6;
    classDef neonRosa fill:#240318,stroke:#ff007f,stroke-width:2.5px,color:#ffe6f2;
    classDef neonCyan fill:#051923,stroke:#00f0ff,stroke-width:2.5px,color:#e0f7ff;
    classDef neonVerde fill:#021c10,stroke:#00ff88,stroke-width:2.5px,color:#e6fff0;
    classDef neonMorado fill:#1f032b,stroke:#d000ff,stroke-width:2.5px,color:#f8e6ff;
```

## Descripción de las clases principales

- **Usuario:** clase abstracta para las personas que acceden al sistema.
- **Pasajero:** usuario que compra boletos y realiza check-in.
- **Empleado:** usuario que administra operaciones de la aerolínea.
- **Vuelo:** representa un viaje entre dos aeropuertos.
- **Reserva:** relaciona al pasajero con un vuelo y uno o más asientos.
- **Pago:** registra la operación económica de una reserva.
- **PaseAbordar:** documento que permite al pasajero abordar el avión.

## Relaciones UML empleadas

1. **Generalización:** `Pasajero` y `Empleado` heredan de `Usuario`.
2. **Agregación:** una `Reserva` selecciona uno o más `Asiento`.
3. **Composición:** una `Reserva` contiene el `Pago` y el `PaseAbordar` asociados.
4. **Asociación:** el `Pasajero` realiza reservas y el `Vuelo` utiliza un avión.

---

# Fase 4: Diagrama de secuencia

## Escenario: compra de un boleto

```mermaid
sequenceDiagram
    actor Pasajero
    participant App as Aplicación web o móvil
    participant Vuelos as Servicio de vuelos
    participant Reservas as Servicio de reservas
    participant BD as Base de datos
    participant Pago as Pasarela de pago
    participant Notificacion as Servicio de notificaciones

    Pasajero->>App: Ingresar origen, destino y fecha
    App->>Vuelos: Buscar vuelos
    Vuelos->>BD: Consultar vuelos disponibles
    BD-->>Vuelos: Lista de vuelos
    Vuelos-->>App: Mostrar resultados

    Pasajero->>App: Seleccionar vuelo y asiento
    App->>Reservas: Crear reserva temporal
    Reservas->>BD: Guardar reserva pendiente
    BD-->>Reservas: Código de reserva
    Reservas-->>App: Mostrar importe a pagar

    Pasajero->>App: Confirmar pago
    App->>Pago: Procesar pago
    Pago-->>App: Resultado del pago

    alt Pago aprobado
        App->>Reservas: Confirmar reserva
        Reservas->>BD: Actualizar estado a CONFIRMADA
        Reservas->>Notificacion: Enviar confirmación
        Notificacion-->>Pasajero: Email o SMS de confirmación
        App-->>Pasajero: Mostrar boleto confirmado
    else Pago rechazado
        App-->>Pasajero: Mostrar error de pago
    end
```

---

# Fase 5: Diagrama de estados

Este diagrama representa el ciclo de vida de una **reserva**.

```mermaid
stateDiagram-v2
    [*] --> Pendiente

    Pendiente --> Confirmada: pago aprobado
    Pendiente --> Cancelada: pago rechazado
    Pendiente --> Cancelada: tiempo expirado

    Confirmada --> EnCheckIn: iniciar check-in
    Confirmada --> Cancelada: solicitar cancelación

    EnCheckIn --> PaseEmitido: datos validados
    PaseEmitido --> Embarcada: pasajero aborda
    PaseEmitido --> NoShow: pasajero no se presenta

    Embarcada --> Completada: vuelo finalizado
    Cancelada --> Reembolsada: reembolso aprobado

    Completada --> [*]
    Reembolsada --> [*]
    NoShow --> [*]

    classDef pendiente fill:#241902,stroke:#ffea00,stroke-width:2px,color:#fffde6;
    classDef confirmado fill:#021c10,stroke:#00ff88,stroke-width:2px,color:#e6fff0;
    classDef cancelado fill:#240318,stroke:#ff007f,stroke-width:2px,color:#ffe6f2;

    class Pendiente pendiente
    class Confirmada,EnCheckIn,PaseEmitido,Embarcada,Completada confirmado
    class Cancelada,Reembolsada,NoShow cancelado
```

## Estados de la reserva

| Estado | Descripción |
| :--- | :--- |
| **Pendiente** | La reserva fue creada, pero todavía no fue pagada. |
| **Confirmada** | El pago fue aprobado. |
| **EnCheckIn** | El pasajero comenzó el proceso de check-in. |
| **PaseEmitido** | El sistema generó el pase de abordar. |
| **Embarcada** | El pasajero abordó el avión. |
| **Completada** | El vuelo finalizó correctamente. |
| **Cancelada** | La reserva fue cancelada. |
| **Reembolsada** | Se devolvió el dinero al pasajero. |
| **NoShow** | El pasajero no se presentó al vuelo. |

---

# Fase 6: Diagrama de colaboración y comunicación

El diagrama de comunicación muestra cómo colaboran los objetos y el orden de los mensajes.

```mermaid
flowchart LR
    Pasajero["pasajero: Pasajero"]
    Aplicacion["aplicacion: Aplicación"]
    ServicioVuelos["servicioVuelos: ServicioVuelos"]
    ServicioReservas["servicioReservas: ServicioReservas"]
    BaseDatos[("baseDatos: Base de datos")]
    PasarelaPago["pasarelaPago: PasarelaPago"]
    Notificaciones["notificaciones: Notificaciones"]

    Pasajero -->|"1: buscarVuelo()"| Aplicacion
    Aplicacion -->|"2: consultarDisponibilidad()"| ServicioVuelos
    ServicioVuelos -->|"3: obtenerVuelos()"| BaseDatos
    BaseDatos -->|"4: devolverVuelos()"| ServicioVuelos
    ServicioVuelos -->|"5: mostrarResultados()"| Aplicacion

    Pasajero -->|"6: seleccionarVuelo()"| Aplicacion
    Aplicacion -->|"7: crearReserva()"| ServicioReservas
    ServicioReservas -->|"8: guardarReservaPendiente()"| BaseDatos

    Pasajero -->|"9: pagar()"| Aplicacion
    Aplicacion -->|"10: procesarPago()"| PasarelaPago
    PasarelaPago -->|"11: pagoAprobado()"| Aplicacion

    Aplicacion -->|"12: confirmarReserva()"| ServicioReservas
    ServicioReservas -->|"13: actualizarReserva()"| BaseDatos
    ServicioReservas -->|"14: enviarConfirmacion()"| Notificaciones
    Notificaciones -->|"15: enviarEmail()"| Pasajero

    classDef actor fill:#241902,stroke:#ffea00,stroke-width:2px,color:#fffde6;
    classDef servicio fill:#051923,stroke:#00f0ff,stroke-width:2px,color:#e0f7ff;
    classDef externo fill:#1f032b,stroke:#d000ff,stroke-width:2px,color:#f8e6ff;
    classDef datos fill:#021c10,stroke:#00ff88,stroke-width:2px,color:#e6fff0;

    class Pasajero actor;
    class Aplicacion,ServicioVuelos,ServicioReservas servicio;
    class PasarelaPago,Notificaciones externo;
    class BaseDatos datos;
```

---

# Fase 7: Diagrama de distribución o despliegue

El diagrama de despliegue muestra dónde se ejecutan los componentes del sistema.

```mermaid
flowchart TB
    Cliente["Dispositivo del pasajero<br/>Navegador web / App móvil"]
    Terminal["Terminal de aeropuerto<br/>Sistema de mostrador"]

    subgraph Servidor["Servidor de aplicaciones"]
        API["API de aerolínea"]
        ServicioVuelos["Servicio de vuelos"]
        ServicioReservas["Servicio de reservas"]
        ServicioUsuarios["Servicio de usuarios"]
        ServicioCheckIn["Servicio de check-in"]
    end

    BD[("Base de datos central")]
    Pago["Pasarela de pago externa"]
    Notificaciones["Servicio de correo y SMS"]

    Cliente -->|HTTPS| API
    Terminal -->|HTTPS| API

    API --> ServicioVuelos
    API --> ServicioReservas
    API --> ServicioUsuarios
    API --> ServicioCheckIn

    ServicioVuelos -->|SQL| BD
    ServicioReservas -->|SQL| BD
    ServicioUsuarios -->|SQL| BD
    ServicioCheckIn -->|SQL| BD

    ServicioReservas -->|API segura| Pago
    ServicioReservas -->|API de mensajes| Notificaciones

    classDef dispositivo fill:#241902,stroke:#ffea00,stroke-width:2px,color:#fffde6;
    classDef servidor fill:#051923,stroke:#00f0ff,stroke-width:2px,color:#e0f7ff;
    classDef datos fill:#021c10,stroke:#00ff88,stroke-width:2px,color:#e6fff0;
    classDef externo fill:#1f032b,stroke:#d000ff,stroke-width:2px,color:#f8e6ff;

    class Cliente,Terminal dispositivo;
    class API,ServicioVuelos,ServicioReservas,ServicioUsuarios,ServicioCheckIn servidor;
    class BD datos;
    class Pago,Notificaciones externo;
```

## Componentes de despliegue

- **Dispositivo del pasajero:** navegador web o aplicación móvil.
- **API de aerolínea:** punto de entrada para las solicitudes del sistema.
- **Servicio de vuelos:** consulta y administra vuelos.
- **Servicio de reservas:** crea, confirma y cancela reservas.
- **Servicio de usuarios:** administra autenticación y perfiles.
- **Servicio de check-in:** valida pasajeros y genera pases de abordar.
- **Base de datos central:** almacena vuelos, pasajeros, reservas y pagos.
- **Pasarela de pago:** sistema externo para procesar transacciones.
- **Servicio de notificaciones:** envía emails y mensajes SMS.

---

# Diagrama complementario de actividad

Aunque no aparece como una fase independiente, el diagrama de actividad permite mostrar el flujo completo de compra de un boleto.

```mermaid
flowchart TD
    Inicio((Inicio))
    Datos["Ingresar origen, destino y fecha"]
    Buscar["Buscar vuelos disponibles"]
    Disponibles{"¿Hay vuelos disponibles?"}
    Seleccionar["Seleccionar vuelo y asiento"]
    DatosPasajero["Ingresar datos del pasajero"]
    Reserva["Crear reserva temporal"]
    Pagar["Realizar pago"]
    PagoAprobado{"¿Pago aprobado?"}
    Confirmar["Confirmar reserva"]
    Boleto["Generar boleto"]
    Enviar["Enviar confirmación"]
    Rechazo["Informar rechazo del pago"]
    Cancelar["Cancelar reserva temporal"]
    SinVuelos["Mostrar vuelos no disponibles"]
    Fin((Fin))

    Inicio --> Datos
    Datos --> Buscar
    Buscar --> Disponibles

    Disponibles -->|Sí| Seleccionar
    Disponibles -->|No| SinVuelos
    SinVuelos --> Fin

    Seleccionar --> DatosPasajero
    DatosPasajero --> Reserva
    Reserva --> Pagar
    Pagar --> PagoAprobado

    PagoAprobado -->|Sí| Confirmar
    PagoAprobado -->|No| Rechazo
    Confirmar --> Boleto
    Boleto --> Enviar
    Enviar --> Fin
    Rechazo --> Cancelar
    Cancelar --> Fin

    classDef inicio fill:#021c10,stroke:#00ff88,stroke-width:2px,color:#e6fff0;
    classDef proceso fill:#051923,stroke:#00f0ff,stroke-width:2px,color:#e0f7ff;
    classDef decision fill:#241902,stroke:#ffea00,stroke-width:2px,color:#fffde6;
    classDef error fill:#240318,stroke:#ff007f,stroke-width:2px,color:#ffe6f2;

    class Inicio,Fin inicio;
    class Datos,Buscar,Seleccionar,DatosPasajero,Reserva,Pagar,Confirmar,Boleto,Enviar proceso;
    class Disponibles,PagoAprobado decision;
    class Rechazo,Cancelar,SinVuelos error;
```

---

# Conclusión

La arquitectura propuesta incluye:

- 6 actores externos.
- Más de 5 casos de uso.
- 10 clases principales.
- El flujo completo de compra de boletos.
- El ciclo de vida de una reserva.
- La comunicación entre objetos.
- La distribución física y lógica del sistema.
- 7 diagramas UML nativos de Markdown mediante Mermaid:
  1. Casos de uso.
  2. Clases.
  3. Secuencia.
  4. Estados.
  5. Comunicación.
  6. Despliegue o distribución.
  7. Actividad.
