# Diagrama de flujo: Preparar un café matutino

> El bloque con forma de rombo representa una decisión. Las flechas indican el orden del proceso.

## Diagrama visual

```mermaid
flowchart TD
    A([Inicio]) --> B[Escena 1: Recámara<br/>Suena la alarma]
    B --> C{¿Despertó el personaje?}
    C -- No --> D[Sonar alarma nuevamente]
    D --> C
    C -- Sí --> E[Caminar hacia la cocina]
    E --> F[Escena 2: Cocina]
    F --> G{¿Hay café listo?}
    G -- No --> H[Calentar agua]
    H --> I[Agregar café molido]
    I --> J[Servir café en la taza]
    J --> K[Tomar la taza]
    G -- Sí --> K
    K --> L[Caminar de la cocina a la sala]
    L --> M[Escena 3: Sala<br/>Sentarse y beber café]
    M --> N{¿Energía menor que 50?}
    N -- Sí --> O[Beber café]
    O --> P[Incrementar energía en 20]
    P --> N
    N -- No --> Q([Fin])

    classDef inicio fill:#b7e1cd,stroke:#208454,stroke-width:2px,color:#000;
    classDef proceso fill:#d9eaf7,stroke:#2672a8,stroke-width:1px,color:#000;
    classDef decision fill:#fff2cc,stroke:#b8860b,stroke-width:2px,color:#000;
    classDef escena fill:#eadcf8,stroke:#7b4aa5,stroke-width:2px,color:#000;

    class A,Q inicio;
    class B,F,M escena;
    class C,G,N decision;
    class D,E,H,I,J,K,L,O,P proceso;
```

## Versión por bloques

```text
╭──────────────╮
│    INICIO    │
╰──────┬───────╯
       ▼
┌─────────────────────────────┐
│ ESCENA 1: RECÁMARA          │
│ Suena la alarma             │
└──────────────┬──────────────┘
               ▼
        ◇ ¿Despertó? ◇
          │ Sí     │ No
          │        ▼
          │  ┌───────────────┐
          │  │ Sonar alarma  │
          │  │ nuevamente    │
          │  └───────┬───────┘
          │          │
          │          └──────► Volver a la decisión
          ▼
┌─────────────────────────────┐
│ Caminar hacia la cocina     │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ ESCENA 2: COCINA            │
└──────────────┬──────────────┘
               ▼
       ◇ ¿Hay café listo? ◇
          │ Sí        │ No
          │           ▼
          │   ┌──────────────────┐
          │   │ Calentar agua    │
          │   ├──────────────────┤
          │   │ Agregar café     │
          │   ├──────────────────┤
          │   │ Servir en taza   │
          │   └────────┬─────────┘
          └────────────┘
               ▼
┌─────────────────────────────┐
│ Tomar la taza               │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│ ESCENA 3: SALA              │
│ Sentarse y beber café       │
└──────────────┬──────────────┘
               ▼
       ◇ ¿Energía < 50? ◇
          │ Sí        │ No
          ▼           ▼
┌──────────────────┐  ╭──────────────╮
│ Beber café       │  │     FIN      │
│ Energía += 20    │  ╰──────────────╯
└────────┬─────────┘
         │
         └────────► Volver a la decisión
```

## Formas utilizadas

| Forma | Significado |
| --- | --- |
| Ovalado | Inicio o fin del proceso |
| Rectángulo | Acción o proceso |
| Rombo | Decisión con opciones Sí/No |
| Flecha | Dirección del flujo |
