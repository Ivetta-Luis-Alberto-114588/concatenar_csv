# Dependencias
* os
* pandas
* numpy
* pyinstaller (generar archivo ejecutable)


# Forma de uso
1) El ejecutable va a leer todos los arhivos .CSV 
2) Los va a concatenar
3) Va a generar un archivo llamado: archivo_final.csv
4) Va a mostrar la cantidad de filas de cada archivo, la suma de filas de todos ellos 
5) Va a mostrar la cantidad de filas del archivo final


# Generacion del ejecutable
* python -m venv env
* .\env\Scripts\activate
* pip install pandas numpy pyinstaller
* pyinstaller --onefile unir.py 