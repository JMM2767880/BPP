# AUTOR: JUSTO MOTA MÁRQUEZ
import pandas as pd
import os, csv

# Excepciones personalizadas:
class Error(Exception):
	pass

class ValidateNumberColumnsError(Error): # Clase que valida elnúmero de columnas
	pass

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
		aux = 0 # Guarda el número de errores
		data_number = 0 # Guarda el número de datos numéricos que hay en el fichero csv
		sum_all_values = 0 # Suma todos los valores numéricos del fichero
		expenses = 0 # Guarda los gastos anuales
		income = 0 # Guarda los ingresos anuales

		for row in csv_reader: # Recorro el fichero csv
			if count != 0: # Si la fila no es la primera, es decir que no es el nombre del mes, empiezo a operar
				for data in row: # Recorro cada columna de la fila
					try: # Intento operar
						sum_all_values += int(data) # Sumo cada columna
						data_number += 1 # Sumo la columna para después dividir el total para calcular la media

						value = int(data) # Guardo el valor de la columna

						if value > 0: # Si el valor es positivo es un ingreso
							income += value
						else: # Si el valor es negativo es un gasto
							expenses += value
					except: # Si no puedo operar
						if aux == 0:
							print("ERRORES:")
						print(f"{data}: No es un valor con el que se pueda operar") # Saco un mensaje de excepción
						aux += 1

				count+=1
			else: # Si la fila es la primera
				try: # Intento comprobar cuantas columnas tiene el fichero
					if len(row) < 12 or len(row) > 12:
						raise ValidateNumberColumnsError # Si no tiene 12 columnas saco la excepción
				except ValidateNumberColumnsError:
					print("Error: El fichero no tiene 12 columnas")
					exit()
				else:
					count+=1


		mean_all_values = sum_all_values/data_number # Guardo la media de todo el año

	# ------------------------------------------------------------------------
	df = pd.read_csv(file_csv, sep="\t") # Creo el Dataframe de finanzas2020.csv
	columns_names = df.columns.tolist() # Guardo el nombre de las columnas en una lista

	print("-------------------------------------------------------------------------------------------------------------")
	# 1. Recojo los valores mínimos de todas las columnas (numeric_only: especifico que lo haga solo con los valores numéricos)
	# 2. Recojo el nombre y el valor del mes que que tenga el valor mas pequeño (del mes que más se haya gastado)
	month_spent_max = df[columns_names].min(numeric_only=True).idxmin()
	val_spent_max = df[columns_names].min(numeric_only=True).min()
	print("¿Qué mes se ha gastado más?")
	print(f"El mes que más se ha gastado es {month_spent_max} y ha quedado un total de {val_spent_max}€")
	df[columns_names].min(numeric_only=True)
	print("-------------------------------------------------------------------------------------------------------------")
	# ------------------------------------------------------------------------
	# 1. Recojo los valores máximos de todas las columnas (numeric_only: especifico que lo haga solo con los valores numéricos)
	# 2. Recojo el nombre y el valor del mes que que tenga el valor mas alto (del mes que más se haya ahorrado)
	month_saved_max = df[columns_names].max(numeric_only=True).idxmax()
	val_saved_max = df[columns_names].max(numeric_only=True).max()
	print("¿Qué mes se ha ahorrado más?")
	print(f"El mes que más se ha ahorrado es {month_saved_max} y ha quedado un total de {val_saved_max}€")
	# ------------------------------------------------------------------------
	print("-------------------------------------------------------------------------------------------------------------")
	print("¿Cuál es la media de gastos al año?")
	print(f"La Media de gastos al año es {mean_all_values}€")
	print("-------------------------------------------------------------------------------------------------------------")
	print("¿Cuál ha sido el gasto total a lo largo del año?")
	print(f"El gasto anual total es de {expenses}€")
	print("-------------------------------------------------------------------------------------------------------------")
	print("¿Cuál ha sido el ingreso total a lo largo del año?")
	print(f"El ingreso anual total es de {income}€")



