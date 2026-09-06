"""
Módulo de lógica de negocio de la calculadora.
Aquí SOLO vive la lógica matemática, separada de la API (Paso 1 y 2 del taller).
"""


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de dos números."""
    return a + b


def restar(a: float, b: float) -> float:
    """Devuelve la resta entre dos números (a - b)."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Devuelve el producto de dos números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Devuelve el cociente de dos números (a / b).
    Lanza ValueError si b es 0, porque no se puede dividir entre cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
