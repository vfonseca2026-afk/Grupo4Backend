# ICINF1108 - Desarrollo Backend
## Taller Evaluado I: Estándar de Respuestas HTTP JSON

**Universidad Católica de Temuco**  
**Carrera:** Ingeniería Civil en Informática  
**Framework:** FastAPI (`estudiantes_icinf-fastapi`)

---

## Integrantes del Equipo (Grupo 4)

| Nombre Completo | Rol | Correo Institucional |
| :--- | :--- | :--- |
| **Vicente Fonseca** | Líder de Grupo | `vfonseca2026@alu.uct.cl` |
| **Matías Manquelaf** | Integrante | `mmanquelaf2026@alu.uct.cl` |
| **Miguel Torres** | Integrante | `miguel.torres2026@alu.uct.cl` |
| **Danna Ramirez** | Integrante | `dramirez2026@alu.uct.cl` |

---

## Estándar de Respuesta JSON Unificado

Para asegurar la consistencia en el consumo de la API REST por parte de clientes frontend u otros servicios, se ha diseñado e implementado un **contrato único de respuesta HTTP JSON** que unifica tanto las peticiones exitosas como los errores de la aplicación.

### Estructura General del Contrato (`ApiResponse`)

Todas las respuestas de la API contienen un objeto JSON raíz con **4 campos obligatorios**:

```json
{
  "success": boolean,
  "status_code": integer,
  "message": string,
  "data": Generic (Object | Array | null)
}

```
### Descripción de Campos

**Succes(Boolean):** Indica si la operación finalizó de manera exitosa*
**(True)** o si ocurrió una falla/error **(False)**.

**Status_code(Integer):** Refleja la forma explícita el código de estado HTTP correspondiente a la respuesta(ej. 200, 201, 400, 404, 422, 500).

**Message(String):** Un mensaje descriptivo y legible sonre el resultado o el motivo del error.

**Data (Generic / Object / Array / Null):** Contenedor de la carga útil(Payload). Puede representar un objetio individual, una lista de objetos o tomar el valor **null** en respuestas sin contenido o en casos de error.

### Ejemplos de representación JSON (Casos de Uso)

**1.-Respuesta Exitosa - Objeto único(200 OK)**

```json
{
  "success": true,
  "status_code": 200,
  "message": "Estudiante obtenido exitosamente",
  "data": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "name": "Juan Pérez",
    "email": "jperez@alu.uct.cl"
  }
}

```
**2.- Respuesta Exitosa - Lista de Objetos (200 OK)**

```json
{
  "success": true,
  "status_code": 200,
  "message": "Lista de mascotas obtenida exitosamente",
  "data": [
    {
      "id": "987f6543-e21b-12d3-a456-426614174000",
      "name": "Firulais",
      "species": "Perro"
    },
    {
      "id": "876f6543-e21b-12d3-a456-426614174001",
      "name": "Michi",
      "species": "Gato"
    }
  ]
}
```

**3.-Respuesta de Error Controlado (404 Not Found)**
```json
{
  "success": false,
  "status_code": 404,
  "message": "El estudiante solicitado no existe en los registros",
  "data": null
}
```

**4.- Respuesta de Error de Validación(422 Unprocessable Entity)**
```json
{
  "success": false,
  "status_code": 422,
  "message": "Error en la validación de los datos de entrada",
  "data": [
    {
      "loc": ["body", "email"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

