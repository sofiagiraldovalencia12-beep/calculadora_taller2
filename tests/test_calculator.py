"""
Pruebas unitarias de la lógica de la calculadora (Paso 4 del taller).
Se prueban números positivos, negativos y el caso límite de división entre cero.

Para ejecutar:
    pytest -v
"""

import pytest
from app.calculator import sumar, restar, multiplicar, dividir


# ---------- SUMA ----------

def test_sum_positive_numbers():
    assert sumar(5, 3) == 8


def test_sum_negative_numbers():
    assert sumar(-5, -3) == -8


# ---------- RESTA ----------

def test_subtract_positive_numbers():
    assert restar(10, 4) == 6


def test_subtract_negative_numbers():
    assert restar(-10, -4) == -6


# ---------- MULTIPLICACIÓN ----------

def test_multiply_positive_numbers():
    assert multiplicar(6, 7) == 42


def test_multiply_negative_numbers():
    assert multiplicar(-6, -7) == 42


# ---------- DIVISIÓN ----------

def test_divide_positive_numbers():
    assert dividir(20, 5) == 4


def test_divide_negative_numbers():
    assert dividir(-20, -5) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
