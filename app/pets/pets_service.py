from datetime import datetime
from uuid import uuid4

from fastapi import HTTPException, status

from app.pets.pets_schemas import CreatePetDto, Pet, UpdatePetDto
from app.shared.in_memory_store import InMemoryStore
from app.students.students_service import StudentsService, students_service


class PetsService:
    def __init__(self, students: StudentsService) -> None:
        self.students_service = students
        self.store: InMemoryStore[Pet] = InMemoryStore()

    def find_all_for_student(self, student_id: str) -> list[Pet]:
        self.assert_student_exists(student_id)
        pets = self.store.find_by(lambda pet: pet.studentId == student_id)
        return sorted(pets, key=lambda p: p.createdAt, reverse=True)

    def create(self, student_id: str, data: CreatePetDto) -> Pet:
        self.assert_student_exists(student_id)

        now = datetime.now()
        pet = Pet(
            id=str(uuid4()),
            studentId=student_id,
            name=data.name,
            species=data.species,
            age=data.age,
            createdAt=now,
            updatedAt=now,
        )

        self.store.set(pet)
        return pet

    def update(self, student_id: str, pet_id: str, data: UpdatePetDto) -> Pet:
        existing = self.find_owned(student_id, pet_id)

        updated = existing.model_copy(
            update={
                **data.model_dump(exclude_none=True),
                "updatedAt": datetime.now(),
            }
        )

        self.store.set(updated)
        return updated

    def delete(self, student_id: str, pet_id: str) -> Pet:
        existing = self.find_owned(student_id, pet_id)
        self.store.delete(pet_id)

        return existing

    def delete_all_for_student(self, student_id: str) -> None:
        self.store.delete_by(lambda pet: pet.studentId == student_id)

    def find_owned(self, student_id: str, pet_id: str) -> Pet:
        self.assert_student_exists(student_id)

        pet = self.store.get(pet_id)

        if pet is None or pet.studentId != student_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mascota no encontrada",
            )

        return pet

    def assert_student_exists(self, student_id: str) -> None:
        self.students_service.find_by_id(student_id)


pets_service = PetsService(students_service)
