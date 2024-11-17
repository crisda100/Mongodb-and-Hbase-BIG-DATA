import happybase

# Conectar a HBase
def connect_to_hbase():
    connection = happybase.Connection('localhost') 
    connection.open()
    return connection

# Insertar datos en la tabla
def insert_data(connection):
    # Conectar a la tabla 'c02_emissions'
    table = connection.table('c02_emissions')

    # Datos para insertar
    row_key = 'Afghanistan_01/01/2020'  # Ejemplo de row key
    data = {
        'geo:country': 'Afghanistan',
        'geo:region': 'Asia',
        'emissions:total': '7000',
        'emissions:per_capita': '0.20',
        'time:date': '01/01/2020',
    }

    # Insertar la fila
    table.put(row_key.encode('utf-8'), data)
    print("Datos insertados correctamente.")

# Actualizar datos en la tabla
def update_data(connection):
    # Conectar a la tabla 'c02_emissions'
    table = connection.table('c02_emissions')

    # Row key de la fila a actualizar
    row_key = 'Afghanistan_01/01/2020'

    # Nuevos datos para actualizar
    updated_data = {
        'emissions:total': '7500',  # Actualizamos las emisiones totales
        'emissions:per_capita': '0.22',  # Actualizamos las emisiones per cápita
    }

    # Actualizar la fila
    table.put(row_key.encode('utf-8'), updated_data)
    print("Datos actualizados correctamente.")

# Eliminar datos en la tabla
def delete_data(connection):
    # Conectar a la tabla 'c02_emissions'
    table = connection.table('c02_emissions')

    # Row key de la fila a eliminar
    row_key = 'Afghanistan_01/01/2020'

    # Eliminar la fila
    table.delete(row_key.encode('utf-8'))
    print("Fila eliminada correctamente.")

# Eliminar una celda específica
def delete_cell(connection):
    # Conectar a la tabla 'c02_emissions'
    table = connection.table('c02_emissions')

    # Row key de la fila
    row_key = 'Afghanistan_01/01/2020'

    # Eliminar una celda específica (por ejemplo, la columna 'emissions:total')
    table.delete(row_key.encode('utf-8'), columns=[b'emissions:total'])
    print("Celda 'emissions:total' eliminada correctamente.")

# Función principal
def main():
    # Conectar a HBase
    connection = connect_to_hbase()

    # Insertar datos
    insert_data(connection)

    # Actualizar datos
    update_data(connection)

    # Eliminar datos (fila completa)
    delete_data(connection)

    # Eliminar una celda específica
    delete_cell(connection)

    # Cerrar la conexión
    connection.close()

# Ejecutar el script
if __name__ == '__main__':
    main()

