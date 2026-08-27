from fastapi import APIRouter

from app.pets.pets_service import pets_service
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto
from app.students.students_service import students_service

router = APIRouter(prefix="/api/students", tags=["Students"])


@router.get("")
def find_all() -> list[Student]:
    return students_service.find_all()


@router.get("/{student_id}")
def find_by_id(student_id: str) -> Student:
    return students_service.find_by_id(student_id)


@router.post("", status_code=201)
def create(body: CreateStudentDto) -> Student:
    return students_service.create(body)


@router.patch("/{student_id}")
def update(student_id: str, body: UpdateStudentDto) -> Student:
    return students_service.update(student_id, body)


@router.delete("/{student_id}")
def delete(student_id: str) -> Student:
    deleted = students_service.delete(student_id)
    pets_service.delete_all_for_student(student_id)

    return deleted
