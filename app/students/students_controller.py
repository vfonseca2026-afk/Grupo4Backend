from fastapi import APIRouter, status

from app.pets.pets_service import pets_service
from app.shared.api_response import ApiResponse
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service

router = APIRouter(prefix="/api/students", tags=["Students"])

@router.get("", response_model=ApiResponse[list[Student]])
def find_all():
    return ApiResponse.ok(data=students_service.find_all(), message="Lista de estudiantes obtenida exitosamente")

@router.get("/{student_id}", response_model=ApiResponse[Student])
def find_by_id(student_id: str):
    return ApiResponse.ok(data=students_service.find_by_id(student_id), message="Estudiante obtenido exitosamente")

@router.post("", status_code=status.HTTP_201_CREATED, response_model=ApiResponse[Student])
def create(body: CreateStudentDto):
    return ApiResponse.ok(
        data=students_service.create(body), 
        message="Estudiante creado exitosamente", 
        status_code=status.HTTP_201_CREATED
    )

@router.patch("/{student_id}", response_model=ApiResponse[Student])
def update(student_id: str, body: UpdateStudentDto):
    return ApiResponse.ok(data=students_service.update(student_id, body), message="Estudiante actualizado exitosamente")

@router.delete("/{student_id}", response_model=ApiResponse[Student])
def delete(student_id: str):
    deleted = students_service.delete(student_id)
    pets_service.delete_all_for_student(student_id)
    return ApiResponse.ok(data=deleted, message="Estudiante eliminado exitosamente")