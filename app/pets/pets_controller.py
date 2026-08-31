from fastapi import APIRouter, status

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.pets.pets_service import pets_service
from app.shared.api_response import ApiResponse

router = APIRouter(prefix="/api/students/{studentId}/pets", tags=["Pets"])

@router.get("", response_model=ApiResponse[list[Pet]])
def find_all(studentId: str):
    return ApiResponse.ok(data=pets_service.find_all_for_student(studentId), message="Mascotas obtenidas exitosamente")

@router.post("", status_code=status.HTTP_201_CREATED, response_model=ApiResponse[Pet])
def create(studentId: str, body: CreatePetDto):
    return ApiResponse.ok(
        data=pets_service.create(studentId, body),
        message="Mascota creada exitosamente",
        status_code=status.HTTP_201_CREATED
    )

@router.patch("/{petId}", response_model=ApiResponse[Pet])
def update(studentId: str, petId: str, body: UpdatePetDto):
    return ApiResponse.ok(data=pets_service.update(studentId, petId, body), message="Mascota actualizada exitosamente")

@router.delete("/{petId}", response_model=ApiResponse[Pet])
def delete(studentId: str, petId: str):
    return ApiResponse.ok(data=pets_service.delete(studentId, petId), message="Mascota eliminada exitosamente")