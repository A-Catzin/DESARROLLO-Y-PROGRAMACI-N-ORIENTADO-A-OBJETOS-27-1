# Pseudocódigo: Preparar un café matutino

## Objetivo

Representar el proceso de despertar, preparar un café y tomarlo antes de comenzar el día.

## Algoritmo

```text
Proceso PrepararCafeMatutino

    Definir energia Como Entero
    Definir hayCafeListo Como Logico

    energia <- 10
    hayCafeListo <- Falso

    // Escena 1: Recámara
    Imprimir "Suena la alarma: ¡A levantarse!"
    Caminar("Recámara", "Cocina")

    // Escena 2: Cocina
    Imprimir "Voy a preparar café"

    Si hayCafeListo = Falso Entonces
        Imprimir "Calentar agua"
        CalentarAgua()

        Imprimir "Agregar café molido"
        AgregarCafeMolido()

        Imprimir "Servir café en la taza"
        ServirEnTaza()

        hayCafeListo <- Verdadero
    FinSi

    // Escena 3: Sala
    TomarTaza()
    Caminar("Cocina", "Sala")

    Mientras energia < 50 Hacer
        BeberCafe()
        energia <- energia + 20
    FinMientras

    Imprimir "¡Qué buen café! Listo para empezar el día"

FinProceso
```

## Descripción de las escenas

| Escena | Lugar | Acción principal |
| --- | --- | --- |
| 1 | Recámara | Suena la alarma y el personaje camina a la cocina. |
| 2 | Cocina | Se calienta el agua, se agrega café y se sirve en una taza. |
| 3 | Sala | El personaje toma el café hasta recuperar energía. |
