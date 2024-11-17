import pandas as pd
import happybase

# Cargar el dataset 
df = pd.read_csv('co2_emissions.csv')

# Conectar a HBase
connection = happybase.Connection('localhost')  
connection.open()

# Verificar si la tabla existe
tables = connection.tables()
if b'c02_emissions' not in tables:
    # Crear la tabla solo si no existe
    connection.create_table(
        'c02_emissions',
        {
            'geo': dict(),
            'emissions': dict(),
            'time': dict()
        }
    )

# Conectar a la tabla 'c02_emissions'
table = connection.table('c02_emissions')

# Iterar sobre las filas del dataset y agregar los datos a la tabla
for _, row in df.iterrows():
    # Definir el row_key (por ejemplo, combinando el país y la fecha)
    row_key = f"{row['Country']}_{row['Date']}"

    # Datos para cada familia de columnas
    data = {
        'geo:country': str(row['Country']).encode('utf-8'),
        'geo:region': str(row['Region']).encode('utf-8'),
        'emissions:total': str(row['Kilotons of Co2']).encode('utf-8'),
        'emissions:per_capita': str(row['Metric Tons Per Capita']).encode('utf-8'),
        'time:date': str(row['Date']).encode('utf-8')
    }

    # Insertar los datos en HBase
    table.put(row_key.encode('utf-8'), data)

# Cerrar la conexión
connection.close()

