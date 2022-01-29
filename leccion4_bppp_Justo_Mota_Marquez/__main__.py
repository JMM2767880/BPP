import pdb

if __name__ == "__main__":
	# PRIMER EJERCICIO ------------------------------------------------------------------------------------------------------
	matrix = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]] # Creo una matriz de números

	numberMaxList = [['\033[1m' + str(j) + '\033[0m' if j == max(i) else str(j) for j in i] for i in matrix] # Creo una comprensión de listas en la que en los valores mayores de cada lista, concateno en secuencia de escape ANSI los carácteres necesarios para escribir en negrita

	print("1. Números mayores de cada lista de la matriz señalados en negrita: :")
	print("[", end="") # Pinto el corchete inicial de la matriz
	for lis in numberMaxList: # Recorro los valores de la matriz
		print("[", end="") # Pinto el corchete del inicio de cada lista que contiene la matriz
		for element in lis: # Recorro cada elemento de las listas de la matriz
			if element == lis[len(lis)-1]: # Si el valor del elemento es igual al valor de la última posición de la lista
				print(element, end="") # Pinto el valor del elemento 
			else: # Si el valor del elemento no es igual al valor de la última posición de la lista	
				print(element + ", ", end="") # Pinto el valor del elemento con una coma al final
		if lis == numberMaxList[len(numberMaxList)-1]: # Si el valor de lis es igual al valor de la última posición de la matriz 
			print("]", end="") # Pinto el corchete de separación entre lista y lista
		else: # Si el valor de lis no es igual al valor de la última posición de la matriz 
			print("], ", end="") # Pinto el corchete de separación entre lista y lista con una coma al final
	print("]") # Pinto el corchete final de la matriz

	# SEGUNDO EJERCICIO ------------------------------------------------------------------------------------------------------
	
	def is_number_prime(num): # Función que devuelve si el número que le pasamos a la función es primo
		for n in range(2, num): # Creo un bucle que valla desde el numero 2 hasta el número que le pasamos a la función menos uno
			if num % n == 0: # Si algún número entre el 2 y el número-1 dividido entre el numero el modulo es 0, quiere decir que el número no es primo
				return False
		return True # Si el numero entre los valores que adopta el bucle no da su módulo 0, quiere decir que es primo

	numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # Creo una lista con valores entre el 1 y el 20

	listPrimeNumber = list(filter(is_number_prime, numberList)) # Creo una lista filtrada que me guarda los números primos que hay entre el 1 y el 20

	print("2. Números primos entre el 1 y el 20:")
	print(listPrimeNumber) # Pinto la lista que contiene los números primos

	
