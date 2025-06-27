"""
Router de operaciones matemáticas para la API de calculadora.
"""

from fastapi import APIRouter
from models.request_models import SumaRequest
from services.operaciones_service import sumar, multiplicacion

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
