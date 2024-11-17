import happybase

# Conectar a HBase
connection = happybase.Connection('localhost') 
connection.open()

# Conectar a la tabla 'c02_emissions'
table = connection.table('c02_emissions')

# Filtro de emisiones: solo mostrar registros con emisiones mayores a 8000
min_emissions = 8000

# Escanear la tabla para todas las filas
rows = table.scan()

for row_key, data in rows:
    # Obtener las emisiones totales
    emissions_str = data.get(b'emissions:total', b'').decode('utf-8')
    if emissions_str:
        emissions = float(emissions_str)
        
        # Si las emisiones son mayores que 8000, mostrar la fila
        if emissions > min_emissions:
            # Obtener la región de la columna 'geo:region'
            region = data.get(b'geo:region', b'').decode('utf-8')
            
            # Imprimir la región y las emisiones
            print(f"Row Key: {row_key.decode('utf-8')}")
            print(f"  Region: {region}")
            print(f"  Emissions: {emissions}")

# Cerrar la conexión
connection.close()

