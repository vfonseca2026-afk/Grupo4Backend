# CRUD Students & Pets (FastAPI)

Proyecto FastAPI que implementa un **CRUD en memoria** para la entidad `Student` y sus mascotas (`Pet`). No requiere base de datos ni contenedores: los datos viven en un diccionario dentro del servicio y se pierden al reiniciar la aplicación.

## Requerimientos

- Python 3.13+ (gestionado automáticamente por [uv](https://docs.astral.sh/uv/))
- uv

## Resumen funcional

La API expone operaciones CRUD completas:

- **Estudiantes** bajo `/api/students`:
    - **Crear**: `POST /api/students`
    - **Listar**: `GET /api/students`
    - **Buscar por id**: `GET /api/students/:id`
    - **Actualizar**: `PATCH /api/students/:id`
    - **Eliminar**: `DELETE /api/students/:id` (también elimina sus mascotas)
- **Mascotas** anidadas bajo `/api/students/:studentId/pets`:
    - **Listar**: `GET /api/students/:studentId/pets`
    - **Crear**: `POST /api/students/:studentId/pets`
    - **Actualizar**: `PATCH /api/students/:studentId/pets/:petId`
    - **Eliminar**: `DELETE /api/students/:studentId/pets/:petId`

Cada estudiante tiene `id` (UUID), `name`, `email`, `age`, `createdAt` y `updatedAt`. El `email` es único: se rechaza con `409 Conflict` si ya existe.

Cada mascota tiene `id` (UUID), `studentId`, `name`, `species`, `age` (opcional), `createdAt` y `updatedAt`. Solo puede operar sobre su estudiante dueño.

Las respuestas devuelven los datos crudos, sin envoltorios. Los errores de validación usan el formato nativo de FastAPI (`422`) y las excepciones HTTP los códigos estándar (`404`, `409`).

## Contexto técnico

- **Backend**: FastAPI
- **Almacenamiento**: en memoria (sin persistencia)
- **Validación**: Pydantic v2
- **Gestor de dependencias**: uv
- **Documentación**: Swagger en `/docs`

## Ejecución local

1. Instalar dependencias:

    ```bash
    make install
    ```

    O directamente con uv:

    ```bash
    uv sync
    ```

2. Levantar el servidor en modo desarrollo:

    ```bash
    make dev
    ```

    O usando uv:

    ```bash
    uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 3000
    ```

La aplicación queda disponible en:

- `http://localhost:3000`
- `http://localhost:3000/docs`

## Comandos útiles

- `make install` — sincroniza dependencias con uv
- `make dev` — arranca uvicorn en modo reload
- `make lint` — ejecuta Ruff (con autocorrección)
- `make format` — formatea el código con Ruff
- `make format-check` — verifica el formato
- `make clean` — elimina `.venv`, cachés y artefactos
