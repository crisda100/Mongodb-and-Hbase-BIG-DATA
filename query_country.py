import happybase

# Conectar a HBase
connection = happybase.Connection('localhost') 
connection.open()

# Conectar a la tabla 'c02_emissions'
table = connection.table('c02_emissions')

# Filtrar por el prefijo de row_key para obtener todas las filas para un país específico
country = 'Afghanistan'
rows = table.scan(row_prefix=country.encode('utf-8'))

# Recorrer e imprimir las filas que pertenecen a ese país
for row_key, data in rows:
    print(f"Row Key: {row_key.decode('utf-8')}")
    for column, value in data.items():
        print(f"  {column.decode('utf-8')}: {value.decode('utf-8')}")

# Cerrar la conexión
connection.close()

