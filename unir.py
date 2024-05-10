import os
import pandas as pd
import numpy as np  # Importar numpy

# Directorio donde están los archivos csv
dir_csv = './'

# Lista para almacenar los dataframes
dfs = []
filas = 0

# Iterar sobre cada archivo en el directorio
for filename in os.listdir(dir_csv):
    if filename.endswith('.csv'):
        # print(filename)
        df = pd.read_csv(os.path.join(dir_csv, filename), sep=';', dtype=str)
        
        df = df.replace('', np.nan)  # Reemplazar las cadenas vacías con NaN
        df = df.dropna(how='all')  # Eliminar filas vacías
        
        # df_final = df.replace('', np.nan)  # Reemplazar las cadenas vacías con NaN
        # df_final = df_final.dropna(how='all')  # Eliminar filas vacías
        
        print (filename, "cantidad filas: ", len(df))
        filas += len(df)
        dfs.append(df)

# Concatenar todos los dataframes
df_final = pd.concat(dfs, ignore_index=True)
df_final = df_final.dropna(how='all')  # Eliminar filas vacías


# Escribir el dataframe final a un nuevo archivo csv
df_final.to_csv('archivo_final.csv', index=False)

print ("suma de filas de todos los arhivos: ", filas)
print ("suma de filas del archivo final: ", len(df_final))
input("Presione cualquier tecla para continuar...")