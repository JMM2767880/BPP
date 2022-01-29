import pytest 
import operaciones

def test_month_max_spent():
	"""
	test_month_max_spent.Test que valida el mes que más se ha gastado
	"""
	assert operaciones.month_max_spent() == "Diciembre"

def test_month_max_saved():
	"""
	test_month_max_saved: Test que valida el mes que más se ha ahorrado
	"""
	assert operaciones.month_max_saved() == "Marzo"

def test_year_mean():
	"""
	test_year_mean: Test que valida que la media anual sea correcta
	"""
	assert operaciones.year_mean() == -13.246861924686192

def test_sent_total_year():
	"""
	test_sent_total_year: Test que valida el gasto total anual
	"""
	assert operaciones.sent_total_year() == -296791

def test_saved_total_year():
	"""
	test_saved_total_year: Test que valida el ingreso total anual
	"""
	assert operaciones.saved_total_year() == 280961

def test_num_columns_csv():
	"""
	test_num_columns_csv: Test que valida el número de columnas que tiene el csv
	"""
	assert operaciones.num_columns_csv() == 12