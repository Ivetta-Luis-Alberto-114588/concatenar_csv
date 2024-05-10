# Dependencias
os
pandas
numpy
pyinstaller (generar archivo ejecutable)


# Forma de uso
El ejecutable va a leer todos los arhivos .CSV 
Los va a concatenar
Va a generar un archivo llamado: archivo_final.csv
Va a mostrar la cantidad de filas de cada archivo, la suma de filas de todos ellos 
Va a mostrar la cantidad de filas del archivo final


# Generarcion del ejecutable
python -m venv env
.\env\Scripts\activate
pip install pandas numpy pyinstaller
pyinstaller --onefile unir.py 