import pandas as pd

# Carga los dos archivos CSV
csv1 = pd.read_csv('MUNS.csv')
csv2 = pd.read_csv('MUNS2.csv')

# Concatenar los archivos
combinado = pd.concat([csv1, csv2], ignore_index=True)

# Guardar el resultado en un nuevo archivo
combinado.to_csv('MUNS_DEF.csv', index=False)

print("Archivos combinados correctamente.")
