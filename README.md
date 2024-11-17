# Mongodb-and-Hbase-BIG-DATA

# Proyecto: Emisiones de CO2 Mongodb

## Nombre de la base de datos: emissions
La base de datos contiene información sobre las emisiones de CO2 a nivel mundial.

## Colección: co2_emissions

### Estructura de la colección co2_emissions:

- **Campo 1:** `Country` (String): Representa el nombre del país.
- **Campo 2:** `Region` (String): Representa la región geográfica del país.
- **Campo 3:** `Date` (String): Fecha en la que se registran los datos, en formato DD/MM/YYYY.
- **Campo 4:** `Kilotons of Co2` (Number): Emisiones de CO2 en kilotoneladas.
- **Campo 5:** `Metric Tons Per Capita` (Number): Emisiones de CO2 per cápita en toneladas métricas.

Este diseño refleja la estructura de un conjunto de datos sobre emisiones de CO2 a nivel mundial, con información clave sobre el país, región, fecha, emisiones totales y emisiones per cápita. Utilizando el dataset de referencia "CO2 Emissions" que nos brinda información relevante sobre este caso de uso.

# Proyecto HBase: Gestión de Emisiones de CO2

## Nombre de la tabla: `co2_emissions`
La tabla en HBase almacena información sobre las emisiones de CO2 a nivel mundial, organizada en familias de columnas: `geo`, `emissions` y `time`.

## Operaciones Realizadas:

### 1. Inserción de Datos:
- **Operación:** Insertamos una nueva fila con la `row key` `Afghanistan_01/01/2020` y los valores correspondientes a las familias de columnas `geo`, `emissions`, `time`.
- **Resultado:** La fila fue insertada correctamente con los datos especificados. HBase creó una nueva entrada para el país "Afghanistan" en la fecha "01/01/2020", con las emisiones de CO2 y la región.

### 2. Actualización de Datos:
- **Operación:** Actualizamos la fila con la `row key` `Afghanistan_01/01/2020` para modificar los valores de las emisiones totales (`emissions:total`) y las emisiones per cápita (`emissions:per_capita`).
- **Resultado:** Los datos de la fila existente fueron sobrescritos con los nuevos valores, reflejando un cambio en las emisiones de CO2 totales y per cápita.

### 3. Eliminación de Fila:
- **Operación:** Eliminamos la fila completa con la `row key` `Afghanistan_01/01/2020`.
- **Resultado:** La fila fue eliminada exitosamente de la tabla `co2_emissions`. Ya no se encuentran los datos de "Afghanistan" para la fecha "01/01/2020" en la tabla.

### 4. Eliminación de Celda Específica:
- **Operación:** Eliminamos la celda que contenía la columna `emissions:total` para la fila con la `row key` `Afghanistan_01/01/2020`.
- **Resultado:** Solo la celda correspondiente a `emissions:total` fue eliminada, mientras que el resto de los datos en la fila permanecen intactos. La columna `emissions:per_capita` y la información de la región y fecha no fueron modificadas.
