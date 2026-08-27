from datetime import datetime
from uuid import uuid4

from fastapi import HTTPException, status

from app.shared.in_memory_store import InMemoryStore
from app.students.students_schemas import CreateStudentDto, Student, UpdateStudentDto


class StudentsService:
    def __init__(self) -> None:
        self.store: InMemoryStore[Student] = InMemoryStore()

    def find_all(self) -> list[Student]:
        return sorted(self.store.find_all(), key=lambda s: s.createdAt, reverse=True)

    def find_by_id(self, student_id: str) -> Student:
        student = self.store.get(student_id)

        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Estudiante no encontrado",
            )

        return student

    def create(self, data: CreateStudentDto) -> Student:
        self.assert_email_available(data.email)

        now = datetime.now()
        student = Student(
            id=str(uuid4()),
            name=data.name,
            email=data.email,
            age=data.age,
            createdAt=now,
            updatedAt=now,
        )

        self.store.set(student)
        return student

    def update(self, student_id: str, data: UpdateStudentDto) -> Student:
        existing = self.find_by_id(student_id)

        if data.email and data.email != existing.email:
            self.assert_email_available(data.email)

        updated = existing.model_copy(
            update={
                **data.model_dump(exclude_none=True),
                "updatedAt": datetime.now(),
            }
        )

        self.store.set(updated)
        return updated

    def delete(self, student_id: str) -> Student:
        existing = self.find_by_id(student_id)
        self.store.delete(student_id)

        return existing

    def assert_email_available(self, email: str) -> None:
        exists = any(student.email == email for student in self.store.find_all())

        if exists:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="El correo electrónico ya está en uso",
            )


students_service = StudentsService()
