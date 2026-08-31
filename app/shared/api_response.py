from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    success: bool
    status_code: int
    message: str
    data: Optional[T] = None

    @classmethod
    def ok(cls, data: T = None, message: str = "Operación exitosa", status_code: int = 200) -> "ApiResponse[T]":
        return cls(
            success=True,
            status_code=status_code,
            message=message,
            data=data
        )

    @classmethod
    def error(cls, message: str = "Error en la solicitud", status_code: int = 400, data: Any = None) -> "ApiResponse[Any]":
        return cls(
            success=False,
            status_code=status_code,
            message=message,
            data=data
        )