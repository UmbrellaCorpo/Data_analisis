import pandas as pd
import sqlalchemy

# Configuración de la base de datos (ajustar según tu configuración)
db_connection = sqlalchemy.create_engine('mysql+pymysql://user:password@localhost/datadb')

# Cargar el archivo procesado
processed_data_path = './results/processed_data.json'
processed_data = pd.read_json(processed_data_path)

# Exportar a la base de datos
processed_data.to_sql('evolution_analysis', con=db_connection, if_exists='replace', index=False)

print("Datos exportados a la base de datos.")
