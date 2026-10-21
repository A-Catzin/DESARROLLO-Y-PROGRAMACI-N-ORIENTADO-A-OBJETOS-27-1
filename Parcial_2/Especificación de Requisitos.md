## **Problema una cafetería quiere controlar pedidos** 
## 1. Requisitos Funcionales (RF)

| Requisito Funcional                      | Descripción                                                                                                                                                                                        | Prioridad |
| :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------: |
| **Toma y registro de pedidos**           | El personal de caja o mesero debe poder registrar la orden seleccionando productos del menú, especificando variantes (tipo de leche, tamaño, endulzante) y agregando notas especiales del cliente. | **Alta**  |
| **Envío de comandas a barra/cocina**     | Al confirmar la orden en caja, el sistema debe transmitir la comanda en tiempo real hacia una pantalla de preparación (KDS) o ticketera física ubicada en la barra.                                | **Alta**  |
| **Actualización de estados de la orden** | El barista debe poder actualizar el estado del pedido a través de la interfaz (*Pendiente*, *En preparación*, *Listo para entrega*, *Entregado*).                                                  | **Alta**  |
| **Gestión de catálogo y disponibilidad** | El administrador debe poder crear, editar o desactivar productos, modificar precios y marcar insumos como "agotados" para bloquear su venta inmediata.                                             | **Media** |
| **Generación de reportes de ventas**     | El sistema debe emitir reportes de ventas por rango de fechas, productos más vendidos y resumen de corte de caja por turno.                                                                        | **Media** |

---

## 2. Requisitos No Funcionales (RNF)

| Requisito No Funcional            | Criterio de Medición                                                                                                                                                        | Prioridad |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------: |
| **Rendimiento y latencia**        | El registro y envío de un pedido a la barra debe completarse en menos de 2 segundos para evitar retrasos durante horas de alta afluencia.                                   | **Alta**  |
| **Disponibilidad y modo offline** | El sistema debe garantizar una disponibilidad del 99.5% en horario operativo y contar con soporte de contingencia local si se interrumpe la conexión a internet.            | **Alta**  |
| **Usabilidad**                    | La interfaz de usuario debe ser optimizada para pantallas táctiles y requerir menos de 15 minutos de capacitación para que un operador nuevo registre comandas sin errores. | **Media** |

---

## 3. Fuera del Alcance (Out of Scope)

* **Gestión contable y nómina:** No incluye conciliación fiscal, cálculo de salarios ni libros contables formales.
* **Control de almacén y cadena de suministro:** No incluye manejo avanzado de mermas, stock por gramos/mililitros ni órdenes de compra automáticas a proveedores (solo activación/desactivación manual de disponibilidad).
* **App móvil nativa para clientes o delivery:** No contempla una aplicación para el consumidor final ni integración con plataformas externas (Uber Eats, Rappi, etc.).
* **Pasarela de pago bancaria integrada:** El sistema registra el medio de pago (efectivo, tarjeta, transferencia), pero el cobro con tarjeta se gestiona por fuera en el datafono/terminal física del banco.