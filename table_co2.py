import happybase

# Conectar al servidor Thrift de HBase
connection = happybase.Connection('localhost')
connection.open()

# Nombre de la tabla
table_name = 'co2_emissions'

# Verificar si la tabla ya existe
if table_name.encode('utf-8') not in connection.tables():
    # Crear la tabla con las familias de columnas
    connection.create_table(
        table_name,
        {
            'geo': dict(),         # Familia de columnas para país y región
            'emissions': dict(),   # Familia de columnas para datos de emisiones
            'time': dict()         # Familia de columnas para la fecha
        }
    )
    print(f"Tabla '{table_name}' creada exitosamente.")
else:
    print(f"La tabla '{table_name}' ya existe.")

# Cerrar la conexión
connection.close()

