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
