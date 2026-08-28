"""
Este archivo define la plantilla única para todas las respuestas de la API

Garantiza que cualquier respuesta (exito/error) se envíe siempre 
con el mismo formato estandarizado. La casilla 'data' es flexible y puede 
guardar un solo elemento, una lista completa o ir vacía si ocurrió un errorgi
"""

from typing import Generic, TypeVar, Optional, List, Any
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    statusCode: int
    message: str
    data: Optional[T] = None
    errors: Optional[List[Any]] = None

    @classmethod
    def ok(cls, data: T = None, message: str = "Operación realizada con éxito", status_code: int = 200):
        return cls(
            success=True,
            statusCode=status_code,
            message=message,
            data=data,
            errors=None
        )

    @classmethod
    def error(cls, message: str, status_code: int = 400, errors: Optional[List[Any]] = None):
        return cls(
            success=False,
            statusCode=status_code,
            message=message,
            data=None,
            errors=errors
        )