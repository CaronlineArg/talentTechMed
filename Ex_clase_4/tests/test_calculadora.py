
""" 
Pytest

1-Casos de prueba por operación Crea dos tests para cada función (sumar, restar, multiplicar, dividir):

Éxito : resultado correcto.

Error : comportamiento esperado ante fallo (p. ej. dividir debe lanzar ValueError al dividir por 0)

2-Fixtures

Conserva el fixture de enteros existente.

Añade un segundo fixture con valores flotantes (0.1, 0.2) y utilízalo donde corresponda.

Markers

3-ParametrizaciónPara sumar y restar, usa @pytest.mark.parametrize con al menos tres datasets distintos.

Etiqueta los tests de sumar con @pytest.mark.smoke.

Etiqueta los tests de dividir que validan la excepción con @pytest.mark.exception.

4-Muestra cómo filtrar la ejecución:

pytest -m smoke        # solo tests “sumar”

pytest -m exception    # solo tests “dividir” con error

5-Reporte HTML

Genera el informe con: pytest --html=report.html.

Sube report.html junto con tu Pull Request.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from Ex_clase_3.calculadora import sumar, restar, dividir, multiplicar
import pytest 
@pytest.fixture
def numeros():
    return (10, 5)
@pytest.fixture
def numeros_float():
    return (10.5, 5.5)

#@pytest.mark.smoke
def test_sumar_negativos(numeros):
    a, b = numeros
    assert sumar(-a, -b) == -15 

#@pytest.mark.smoke
def test_sumar(numeros):
    a, b = numeros
    assert  sumar (a, b) == 15

#@pytest.mark.smoke
def test_sumar_floats(numeros_float):
    a, b = numeros_float
    assert sumar(a, b) == 16
   
def test_restar_negativos(numeros):
    a, b = numeros
    assert restar(-a, -b) == -5 

def test_restar(numeros):
    a, b = numeros
    assert restar(a, b) == 5

def test_multiplicar(numeros):
    a, b = numeros
    assert  multiplicar( a, b) == 50
   
def test_restar_dividir(numeros):
    a, b = numeros
    assert dividir(a, b) == 2 

@pytest.mark.exception
def test_dividir_por_cero(): 
    with pytest.raises(ValueError): 
      dividir(1, 0)