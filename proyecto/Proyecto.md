# Proyecto: Sistema de Gestión de Envíos para Paquetería Local ("Riviera Express")

## 1. Carpeta `requerimientos/`
- [Instrucciones y Reglas del Proyecto](<requerimientos/Instrucciones_Proyecto.md>)
- [Especificación de Requisitos (Funcionales y No Funcionales)](<requerimientos/Requisitos_Riviera_Express.md>)

## 2. Carpeta `documentos/`
- [Reporte Oficial del Proyecto con Membrete TUP (PDF)](<documentos/Reporte_Proyecto_Riviera_Express.pdf>)
- [Reporte Oficial del Proyecto con Membrete TUP (DOCX)](<documentos/Reporte_Proyecto_Riviera_Express.docx>)
- [Análisis (Objetos y Diagrama de Casos de Uso) y Diseño (Diagrama de Clases UML)](<documentos/Analisis_y_Diseno_Riviera_Express.md>)
- [Explicación Línea por Línea para Exposición (Markdown)](<documentos/Explicacion_Linea_Por_Linea.md>)
- [Explicación Línea por Línea para Exposición (PDF)](<documentos/Explicacion_Linea_Por_Linea.pdf>)

## 3. Carpeta `programa/`
- [Clase `Envio` (Superclase, `get`/`set`, sobrecarga `+` y `-`)](<programa/Envio.py>)
- [Clase `Paquete` (Herencia de `Envio`, `@property` volumen)](<programa/Paquete.py>)
- [Clase `Documento` (Herencia de `Envio`, `@property` urgente)](<programa/Documento.py>)
- [Clase `Repartidor` (`get`/`set`)](<programa/Repartidor.py>)
- [Clase `HojaRuta` (`@property`, agrupación de envíos y asignación de repartidor)](<programa/HojaRuta.py>)
- [Archivo Principal `main.py` (Objetos y datos de prueba)](<programa/main.py>)
