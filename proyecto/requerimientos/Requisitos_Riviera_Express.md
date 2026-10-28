# Fase 1: Especificación de Requisitos · "Riviera Express"

> **Caso de estudio (#8)**: "Riviera Express" es una empresa de envíos urbanos que transporta paquetes y documentos pequeños. Necesitan un sistema que calcule el costo de envío basándose en el peso, volumen y la distancia de entrega del paquete. El software debe validar que no existan pesos o medidas negativas, permitir agrupar varios paquetes bajo una misma hoja de ruta de entrega y asignar un repartidor responsable para optimizar las operaciones diarias.

---

## 1. Requisitos Funcionales (RF)

| Código | Requisito Funcional | Descripción | Prioridad |
| :--- | :--- | :--- | :---: |
| **RF-01** | **Registro de envíos (Paquetes y Documentos)** | El sistema debe permitir registrar envíos identificando su código único, peso (kg) y distancia de entrega (km), diferenciando entre paquetes (con volumen en $m^3$) y documentos pequeños (con indicador de urgencia). | **Alta** |
| **RF-02** | **Validación de medidas y pesos positivos** | El sistema debe validar mediante encapsulamiento que el peso, el volumen y la distancia sean estrictamente mayores a cero, impidiendo valores nulos o negativos. | **Alta** |
| **RF-03** | **Cálculo automático de costo de envío** | El sistema debe calcular el costo de cada envío basándose en su peso, distancia y volumen (o recargo de urgencia), permitiendo opcionalmente sumar un cargo por seguro. | **Alta** |
| **RF-04** | **Agrupación en Hoja de Ruta** | El sistema debe permitir agrupar múltiples paquetes y documentos dentro de una misma hoja de ruta identificada por folio y zona de reparto. | **Alta** |
| **RF-05** | **Asignación de repartidor responsable** | El sistema debe permitir registrar repartidores (ID, nombre y vehículo) y asignar un repartidor responsable a cada hoja de ruta. | **Alta** |
| **RF-06** | **Consolidación de costos y pesos con sobrecarga** | El sistema debe permitir sumar y restar costos de envíos directamente mediante sobrecarga de operadores (`+` y `-`) y emitir el resumen total de la hoja de ruta. | **Media** |

---

## 2. Requisitos No Funcionales (RNF)

| Código | Requisito No Funcional | Criterio de Especificación | Prioridad |
| :--- | :--- | :--- | :---: |
| **RNF-01** | **Modularidad arquitectónica** | El código debe organizarse bajo la regla `1 Archivo = 1 Clase`, separando las definiciones de clases del archivo principal de ejecución (`main.py`). | **Alta** |
| **RNF-02** | **Integridad de datos por encapsulamiento** | Todos los atributos de las clases deben ser privados (`__atributo`) y accederse mediante métodos `get`/`set` tradicionales y propiedades `@property`. | **Alta** |
| **RNF-03** | **Validación condicional sin excepciones** | Todas las validaciones de negocio deben resolverse con estructuras condicionales (`if/else`), sin emplear bloques `try/except` ni lanzar errores de ejecución. | **Alta** |
| **RNF-04** | **Rendimiento de cálculo** | El cálculo de tarifas individuales y el consolidado de una hoja de ruta deben ejecutarse de forma inmediata en memoria (< 1 segundo). | **Media** |
