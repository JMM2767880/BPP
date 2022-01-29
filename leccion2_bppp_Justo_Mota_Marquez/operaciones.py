import pandas as pd
import os, csv

"""
FUNCIONES:
month_max_spent: Función que devuelve el mes que más se ha gastado
month_max_saved: Función que devuelve el mes que más se ha ahorrado
year_mean: Función que devuelve la media anual
sent_total_year: Función que devuelve el gasto anual
saved_total_year: Función que devuelve el ingreso anual
num_columns_csv: Función que devuelve el número de columnas del fichero csv
"""


def month_max_spent():
	"""
	month_max_spent: Función que devuelve el mes que más se ha gastado
	"""
	try: # Intento leer y abrir la ruta del fichero csv
		actual_path = os.path.dirname(os.path.realpath(__file__)) # Guardo el directorio actual del fichero
		file_csv = actual_path + "/finanzas2020(1).csv" # Creo y guardo la ruta del fichero csv
		open_file = open(file_csv, 'r') # Abro el fichero csv en modo lectura 

	except IOError as e: # Si no encuentro el fichero lanzo una excepción
		print(f"Error, no encuentro el fichero: {e}")
	else:
		df = pd.read_csv(file_csv, sep="\t") # Creo el Dataframe de finanzas2020.csv
		columns_names = df.columns.tolist() # Guardo el nombre de las columnas en una lista

		# Recojo el nombre y el valor del mes que que tenga el valor mas pequeño (del mes que más se haya gastado)
		month_spent_max = df[columns_names].min(numeric_only=True).idxmin()

		return month_spent_max

def month_max_saved():
	"""
	month_max_saved: Función que devuelve el mes que más se ha ahorrado
	"""
	try: # Intento leer y abrir la ruta del fichero csv
		actual_path = os.path.dirname(os.path.realpath(__file__)) # Guardo el directorio actual del fichero
		file_csv = actual_path + "/finanzas2020(1).csv" # Creo y guardo la ruta del fichero csv
		open_file = open(file_csv, 'r') # Abro el fichero csv en modo lectura 

	except IOError as e: # Si no encuentro el fichero lanzo una excepción
		print(f"Error, no encuentro el fichero: {e}")
	else:
		df = pd.read_csv(file_csv, sep="\t") # Creo el Dataframe de finanzas2020.csv
		columns_names = df.columns.tolist() # Guardo el nombre de las columnas en una lista

		# Recojo el nombre y el valor del mes que que tenga el valor mas pequeño (del mes que más se haya gastado)
		month_saved_max = df[columns_names].max(numeric_only=True).idxmax()

		return month_saved_max


def year_mean():
	"""
	year_mean: Función que devuelve la media anual
	"""
	try: # Intento leer y abrir la ruta del fichero csv
		actual_path = os.path.dirname(os.path.realpath(__file__)) # Guardo el directorio actual del fichero
		file_csv = actual_path + "/finanzas2020(1).csv" # Creo y guardo la ruta del fichero csv
		open_file = open(file_csv, 'r') # Abro el fichero csv en modo lectura 

	except IOError as e: # Si no encuentro el fichero lanzo una excepción
		print(f"Error, no encuentro el fichero: {e}")
	else: # Si todo está correcto, sigo con la ejecución del programa
		with open_file as csv_file: # Abro el fichero
			csv_reader = csv.reader(csv_file, delimiter='\t') # Especifico el separador que voy a emplear en el fichero csv
			count = 0 # Guarda el número de filas que tiene el fichero
			data_number = 0 # Guarda el número de datos numéricos que hay en el fichero csv
			sum_all_values = 0 # Suma todos los valores numéricos del fichero

			for row in csv_reader: # Recorro el fichero csv
				if count != 0: # Si la fila no es la primera, es decir que no es el nombre del mes, empiezo a operar
					for data in row: # Recorro cada columna de la fila
						try: # Intento operar
							sum_all_values += int(data) # Sumo cada columna
							data_number += 1 # Sumo la columna para después dividir el total para calcular la media
						except: # Si no puedo operar
							pass
					count+=1
				else:
					count+=1

			mean_all_values = sum_all_values/data_number # Guardo la media de todo el año


			return mean_all_values

def sent_total_year():
	"""
	sent_total_year: Función que devuelve el gasto anual
	"""
	try: # Intento leer y abrir la ruta del fichero csv
		actual_path = os.path.dirname(os.path.realpath(__file__)) # Guardo el directorio actual del fichero
		file_csv = actual_path + "/finanzas2020(1).csv" # Creo y guardo la ruta del fichero csv
		open_file = open(file_csv, 'r') # Abro el fichero csv en modo lectura 

	except IOError as e: # Si no encuentro el fichero lanzo una excepción
		print(f"Error, no encuentro el fichero: {e}")
	else: # Si todo está correcto, sigo con la ejecución del programa
		with open_file as csv_file: # Abro el fichero
			csv_reader = csv.reader(csv_file, delimiter='\t') # Especifico el separador que voy a emplear en el fichero csv
			expenses = 0 # Guarda los gastos anuales
			count = 0 # Variable que guarda el número de fila

			for row in csv_reader: # Recorro el fichero csv
				if count != 0: # Si la fila no es la primera, es decir que no es el nombre del mes, empiezo a operar
					for data in row: # Recorro cada columna de la fila
						try: # Intento operar
							value = int(data) # Guardo el valor de la columna

							if value < 0: # # Si el valor es negativo es un gasto
								expenses += value
						except: # Si no puedo operar
							pass
				else: # Si la fila es la primera
					count+=1

			return expenses

def saved_total_year():
	"""
	saved_total_year: Función que devuelve el ingreso anual
	"""
	try: # Intento leer y abrir la ruta del fichero csv
		actual_path = os.path.dirname(os.path.realpath(__file__)) # Guardo el directorio actual del fichero
		file_csv = actual_path + "/finanzas2020(1).csv" # Creo y guardo la ruta del fichero csv
		open_file = open(file_csv, 'r') # Abro el fichero csv en modo lectura 

	except IOError as e: # Si no encuentro el fichero lanzo una excepción
		print(f"Error, no encuentro el fichero: {e}")
	else: # Si todo está correcto, sigo con la ejecución del programa
		with open_file as csv_file: # Abro el fichero
			csv_reader = csv.reader(csv_file, delimiter='\t') # Especifico el separador que voy a emplear en el fichero csv
			income = 0 # Guarda los ingresos anuales
			count = 0 # Variable que guarda el número de fila

			for row in csv_reader: # Recorro el fichero csv
				if count != 0: # Si la fila no es la primera, es decir que no es el nombre del mes, empiezo a operar
					for data in row: # Recorro cada columna de la fila
						try: # Intento operar
							value = int(data) # Guardo el valor de la columna

							if value > 0: # # Si el valor es positivo es un ingreso
								income += value
						except: # Si no puedo operar
							pass
				else: # Si la fila es la primera
					count+=1
					
			return income

def num_columns_csv():
	"""
	num_columns_csv: Función que devuelve el número de columnas del fichero csv
	"""
	try: # Intento leer y abrir la ruta del fichero csv
		actual_path = os.path.dirname(os.path.realpath(__file__)) # Guardo el directorio actual del fichero
		file_csv = actual_path + "/finanzas2020(1).csv" # Creo y guardo la ruta del fichero csv
		open_file = open(file_csv, 'r') # Abro el fichero csv en modo lectura 
	except IOError as e: # Si no encuentro el fichero lanzo una excepción
		print(f"Error, no encuentro el fichero: {e}")
	else: # Si todo está correcto, sigo con la ejecución del programa
		with open_file as csv_file: # Abro el fichero
			csv_reader = csv.reader(csv_file, delimiter='\t') # Especifico el separador que voy a emplear en el fichero csv
			count = 0 # Guarda el número de filas que tiene el fichero

			for row in csv_reader: # Recorro el fichero csv
				if count == 0: # Si la fila es la primera, es decir que es el nombre del mes
					if len(row) < 12 or len(row) > 12: # Si tiene mas o menos columnas que 12
						return len(row) # Devuelvo el número de columnas
					else:
						return len(row) # Devuelvo el número de columnas
					count+=1

					

