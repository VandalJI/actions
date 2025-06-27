"""
Router de operaciones matemáticas para la API de calculadora.
"""

from fastapi import APIRouter
from models.request_models import SumaRequest
from services.operaciones_service import sumar, multiplicar, dividir

router = APIRouter()

@router.post("/suma")
def ruta_suma(datos: SumaRequest):
    """
    Calcula la suma de dos números.

    Args:
        datos (SumaRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la suma.
    """

    resultado = sumar(datos.a, datos.b)
    return {"resultado": resultado}

@router.post("/multiplicacion")
def ruta_multiplicaicon(datos: MultiplicacionRequest):
	"""
	Calcula la multiplicacion de dos nuermos
	"""
	resultado = multiplicar(datos.a, datos.b)
	return {"resultado": resultado}

@router.post("/division")
def ruta_division(datos: DivisionRequest):
	"""
	Calcula la division de dos numeros, pero uno no puede ser 0
	Raises: HTTPException: Si el divisor es 0
	"""
	
	resultado = dividir(datos.a, datos.b)
	return {"resultado": resultado}

