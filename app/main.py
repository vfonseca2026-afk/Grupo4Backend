from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.pets.pets_controller import router as pets_router
from app.students.students_controller import router as students_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI CRUD Students & Pets",
        description=(
            "API de un CRUD en memoria para la entidad Student y sus mascotas (Pet)"
        ),
        version="1.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(students_router)
    app.include_router(pets_router)

    return app


app = create_app()
