"""
Servicios que implementan la lógica de negocio para operaciones matemáticas.
"""
from fastapi import HTTPException

def sumar(a: float, b: float) -> float:
    """
    Suma dos números.

    Args:
        a (float): Primer número.
        b (float): Segundo número.

    Returns:
        float: Resultado de la suma.
    """
    return a + b

def multiplicar(a: float, b:float) -> float:
	"""
	Multiplicar dos numeros
	"""
	return a * b

def dividir(a: float, b: float) -> float:
	if b == 0:
		raise HTTPException(status_code=400, detail="No se puede dividir entre 0."
	return a / b
