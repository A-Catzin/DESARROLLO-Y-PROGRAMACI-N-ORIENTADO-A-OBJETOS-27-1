# Fase 1: Especificación de Requisitos · "Riviera Express"

## Planteamiento del Problema

La empresa de envíos urbanos **"Riviera Express"** transporta diariamente paquetes y documentos pequeños dentro de la ciudad, pero carece de un sistema automatizado que estandarice el cálculo de tarifas y el control operativo de sus entregas. Actualmente, el registro manual permite errores de captura (como ingresar pesos, volúmenes o distancias negativas) y dificulta organizar los envíos por zonas bajo la responsabilidad de un repartidor específico.

**Alcance de la solución**: Desarrollar un sistema orientado a objetos en Python que permita registrar paquetes y documentos, validar que todas las medidas físicas sean estrictamente mayores a cero mediante encapsulamiento, calcular automáticamente el costo de envío con soporte para operaciones aritméticas entre envíos (suma, resta, multiplicación y división mediante sobrecarga de operadores) y agrupar múltiples envíos dentro de una hoja de ruta asignada a un repartidor responsable.

---

## 1. Requisitos Funcionales (RF)

| Código | Requisito Funcional | Descripción | Justificación Técnica | Prioridad |
| :--- | :--- | :--- | :--- | :---: |
| **RF-01** | **Registro de envíos (Paquetes y Documentos)** | El sistema debe permitir registrar envíos con su código, peso (kg) y distancia (km), diferenciando entre paquetes (con volumen) y documentos (con urgencia). | Permite modelar una jerarquía de **herencia** donde `Paquete` y `Documento` reutilizan la estructura común de la superclase `Envio` sin duplicar código. | **Alta** |
| **RF-02** | **Validación de medidas y pesos positivos** | El sistema debe validar que el peso, el volumen y la distancia sean estrictamente mayores a cero, impidiendo valores negativos. | Garantiza la integridad de los datos de negocio mediante **encapsulamiento** (`get`/`set` y `@property`), evitando tarifas negativas o cálculos erróneos. | **Alta** |
| **RF-03** | **Cálculo automático de costo de envío** | El sistema debe calcular el costo de cada envío basándose en el peso, distancia y volumen o urgencia según el tipo de envío. | Automatiza la regla principal del negocio de "Riviera Express" y aplica **polimorfismo** al especializar el cálculo en cada subclase. | **Alta** |
| **RF-04** | **Operaciones entre envíos con sobrecarga** | El sistema debe permitir operar directamente dos objetos de envío utilizando los operadores aritméticos `+`, `-`, `*` y `/`. | Cumple el requerimiento de **sobrecarga de los 4 operadores** (`__add__`, `__sub__`, `__mul__`, `__truediv__`) para consolidar y comparar costos directamente entre objetos. | **Alta** |
| **RF-05** | **Agrupación en Hoja de Ruta** | El sistema debe permitir agrupar múltiples paquetes y documentos dentro de una misma hoja de ruta identificada por folio y zona. | Optimiza las entregas diarias centralizando varios objetos `Envio` dentro de una estructura contenedora (`HojaRuta`). | **Alta** |
| **RF-06** | **Asignación de repartidor responsable** | El sistema debe permitir registrar repartidores (ID, nombre y vehículo) y asignar uno como responsable de una hoja de ruta. | Garantiza la trazabilidad operativa al vincular formalmente un objeto `Repartidor` con los envíos de una `HojaRuta`. | **Alta** |

---

## 2. Requisitos No Funcionales (RNF)

| Código | Requisito No Funcional | Criterio de Especificación | Justificación Técnica | Prioridad |
| :--- | :--- | :--- | :--- | :---: |
| **RNF-01** | **Modularidad arquitectónica (1 Clase = 1 Archivo)** | Cada clase debe residir en su propio archivo `.py` independiente y las instancias deben ejecutarse desde `main.py`. | Facilita el mantenimiento, la legibilidad y el cumplimiento del principio de responsabilidad única en Programación Orientada a Objetos. | **Alta** |
| **RNF-02** | **Encapsulamiento mixto (`@property` y `get`/`set`)** | Los atributos sensibles deben ser privados (`-`) y gestionarse con al menos 2 propiedades `@property` además de métodos `get`/`set`. | Protege el estado interno de los objetos contra modificaciones directas no autorizadas desde fuera de la clase. | **Alta** |
| **RNF-03** | **Estabilidad sin manejo de excepciones** | Todas las validaciones deben realizarse con condicionales simples (`if/else`), sin usar bloques `try/except` y sin arrojar errores en consola. | Asegura un flujo de ejecución predecible, limpio y apegado estrictamente a los fundamentos de POO evaluados en el curso. | **Alta** |
| **RNF-04** | **Código limpio y autodocumentado** | Los archivos `.py` no deben contener líneas comentadas (`#`), utilizando nombres de clases, métodos y variables descriptivos. | Promueve buenas prácticas de código limpio (*Clean Code*) donde la estructura e identificadores explican su propósito por sí mismos. | **Media** |
