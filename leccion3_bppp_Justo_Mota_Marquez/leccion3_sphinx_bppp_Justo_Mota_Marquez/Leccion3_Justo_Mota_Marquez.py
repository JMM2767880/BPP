# Actividad lección 4: Programación avanzada en python, autor: Justo Mota Márquez
# Ejecutar con python3 en vez de python porque en mi script incluyo acentos

#Esta importación la utilizo para limpiar con el comando 'clear' la terminal de ubuntu
import subprocess

# CReo la clase calculadora
class Calculadora:
	"""Calculadora.

    Esta clase implementa operaciones matemáticas

    Atributos
    =========
	    num1: int
	    	Primer valor con el que vamos a operar.
	    num2: int
	       	Segundo valor con el que vamos a operar. 

    Métodos
    =======
	getNum1: 
		Devuelve el primer operando (num1).
	getNum2: 
		Devuelve el segundo operando (num2).
	setNum1: 
		Asigna un valor al primer operando (num1).
	setNum2: 
		Asigna un valor al segundo operando (num2).
	sumar: 
		Realiza la operación de sumar los operandos.
	multiplicar:
		Realiza la operación de multiplicar los operandos.
	restar:
		Realiza la operación de restar los operandos.
	dividir: 
		Realiza la operación de dividir los operandos.
	tablasMultiplicar: 
		Función que dibuja las tablas de multiplicar que hay entre los dos operandos.

	Ejemplos
	========
	>>> numero1 = 5
	>>> numero2 = 4 
	>>> calculadora = Calculadora(numero1, numero2)
	>>> suma = calculadora.sumar()
	>>> print(f"El resultado de sumar {numero1} mas {numero2} es igual a {suma}")
    """
	num1 = 0 # Inicializo el valor del primer número a 0
	num2 = 0 # Inicializo el valor del segundo número a 0

	# CONSTRUCTORES:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	# GETTERS:
	def getNum1(self):
		"""
		Método getNum1. Devuelve el primer operando.
		Outputs:
			self.num1: Primer operando.
		Ejemplo:
			>>> numero1 = 5
			>>> numero2 = 4 
			>>> calculadora = Calculadora(numero1, numero2)
			>>> print(f"El primer operando es {calculadora.getNum1()}")
		"""
		return self.num1

	def getNum2(self):
		"""
		Método getNum2. Devuelve el segundo operando.
		Outputs:
			self.num2: Segundo operando.
		Ejemplo:
			>>> numero1 = 5
			>>> numero2 = 4 
			>>> calculadora = Calculadora(numero1, numero2)
			>>> print(f"El segundo operando es {calculadora.getNum2()}")
		"""
		return self.num2

	# SETTERS:
	def setNum1(self, num1):
		"""
		Método setNum1. Asigna un valor al primer operando.
		Inputs:
			self.num1: Primer operando.
		Ejemplo:
			>>> numero1 = 5
			>>> calculadora = Calculadora()
			>>> calculadora.setNum1(numero1)
		"""
		self.num1 = num1

	def setNum2(self, num2):
		"""
		Método setNum2. Asigna un valor al segundo operando.
		Inputs:
			self.num2: Segundo operando.
		Ejemplo:
			>>> numero2 = 4 
			>>> calculadora = Calculadora()
			>>> calculadora.setNum2(numero2)
		"""
		self.num2 = num2

	# FUNCIONES:
	def sumar(self): # Función que realiza la suma de los dos números
		"""
		Método suma. Suma de los dos operandos.
		Inputs:
			self.num1: Primer operando.
			self.num2: Segundo operando.
		Outputs:
			resultado: Resultado entero de la suma.
		Ejemplo:
			>>> numero1 = 5
			>>> numero2 = 4 
			>>> calculadora = Calculadora(numero1, numero2)
			>>> resultado = calculadora.sumar()
			>>> print(f"El resultado de sumar {numero1} mas {numero2} es igual a {resultado}")
		"""
		return self.num1 + self.num2

	def multiplicar(self):
		"""
		Método multiplicar. Multiplicación de los dos operandos.
		Inputs:
			self.num1: Primer operando.
			self.num2: Segundo operando.
		Outputs:
			resultado: Resultado entero de la multiplicación.
		Ejemplo:
			>>> numero1 = 5
			>>> numero2 = 4 
			>>> calculadora = Calculadora(numero1, numero2)
			>>> resultado = calculadora.multiplicar()
			>>> print(f"El resultado de multiplicar {numero1} por {numero2} es igual a {resultado}")
		"""
		return self.num1 * self.num2 # Función que realiza la multiplicación de los dos números

	def restar(self): # Función que realiza la resta de los dos números
		"""
		Método restar. Resta de los dos operandos.
		Inputs:
			self.num1: Primer operando.
			self.num2: Segundo operando.
		Outputs:
			resultado: Resultado entero de la resta.
		Ejemplo:
			>>> numero1 = 5
			>>> numero2 = 4 
			>>> calculadora = Calculadora(numero1, numero2)
			>>> resultado = calculadora.restar()
			>>> print(f"El resultado de restar {numero1} menos {numero2} es igual a {resultado}")
		"""
		return self.num1 - self.num2

	def dividir(self): # Función que realiza la división de los dos números
		"""
		Método dividir. División de los dos operandos.
		Inputs:
			self.num1: Primer operando.
			self.num2: Segundo operando.
		Outputs:
			resultado: Resultado de la división.
		Ejemplo:
			>>> numero1 = 5
			>>> numero2 = 4 
			>>> calculadora = Calculadora(numero1, numero2)
			>>> resultado = calculadora.dividir()
			>>> print(f"El resultado de dividir {numero1} entre {numero2} es igual a {resultado}")
		"""
		return round(float(self.num1) / float(self.num2), 2) # Devuelvo un decimal para también mostrar si el resultado no es entero y que no me de a 0

	def tablasMultiplicar(self): # Función que realiza la suma de los dos números
		"""
		Método tablasMultiplicar. Dibuja las tablas de multiplicar que hay entre los dos números
		Inputs:
			self.num1: Primer operando.
			self.num2: Segundo operando.
		Outputs:
			Las tablas de multiplicar que hay entre los dos números
		Ejemplo:
			>>> numero1 = 5
			>>> numero2 = 4 
			>>> calculadora = Calculadora(numero1, numero2)
			>>> calculadora.tablasMultiplicar()
		"""
		status = True # Esta variable me va a servir para comprobar si hay numeros entre medias de las tablas

		# Compruebo que número es mayor, menor o si son iguales
		if self.num1 > self.num2:
			menor = self.num2
			mayor = self.num1
		elif self.num1 < self.num2:
			menor = self.num1
			mayor = self.num2
		else: # Si son iguales se va a mostrar el siguiente mensaje
			print("No hay ninguna tabla de multiplicar entre el " + str(self.num1) + " y el " + str(self.num2))
			status = False

		# Si hay números entre los dos números vamos a pintar las tablas de multiplicar
		if status:
			for x in range(int(menor), int(mayor+1)):
				print("Tabla de multiplicar del " + str(x) + ": ------")
				for y in range(1, 11):
					resultado = y * x
					print(str(x) + " x " + str(y)  + " = " + str(resultado))

subprocess.call("clear") # Limpio al inicio del script la terminal

# Pido los valores y me aseguro de que sean enteros, si no lo son repito el introducir los numeros
num1 = input("Introduce el primer número: ")
while not num1.isnumeric():
	num1 = input("El valor tiene que ser numérico y mayor que o igual que 0. Vuelve a introducir el primer número: ")

num2 = input("Introduce el segundo número: ")
while not num2.isnumeric():
	num2 = input("El valor tiene que ser numérico y mayor que o igual que 0. Vuelve a introducir el segundo número: ")

# Instancio una clase
calculadora = Calculadora(int(num1), int(num2))

# Muestro las funciones que la clase contiene
print("OPERACIONES: ----------------------")
print(f"{num1} + {num2} = " + str(calculadora.sumar()))
print(f"{num1} x {num2} = " + str(calculadora.multiplicar()))
print(f"{num1} - {num2} = :" + str(calculadora.restar()))
print(f"{num1} / {num2} = " + str(calculadora.dividir()))
print("Todas las tablas de multiplicar que hay entre estos dos números: -------")
print(str(calculadora.tablasMultiplicar()))



