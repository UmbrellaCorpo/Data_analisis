import pandas as pd
import json

# Cargar el dataset
dataset_path = './data/Evolution_DataSets.csv'
data = pd.read_csv(dataset_path)

# Realizar el análisis: Ejemplo de estadística simple (ajustable según necesidad)
species_group = data.groupby('Genus_&_Specie').agg({
    'Cranial_Capacity': 'mean',
    'Height': 'mean',
    'Diet': pd.Series.mode
}).reset_index()

# Exportar los datos procesados a un archivo JSON
processed_data_path = './results/processed_data.json'
species_group.to_json(processed_data_path, orient='records', indent=4)

# Generar un reporte de análisis
report_path = './results/analysis_report.txt'
with open(report_path, 'w') as report_file:
    report_file.write("Análisis de Datos Evolutivos\n")
    report_file.write(f"Total de especies procesadas: {species_group.shape[0]}\n")
    report_file.write("Resumen por especie:\n")
    report_file.write(species_group.to_string(index=False))

print("Procesamiento completado y datos exportados a JSON.")
