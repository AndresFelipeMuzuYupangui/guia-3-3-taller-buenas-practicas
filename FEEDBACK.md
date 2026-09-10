# Feedback Guia 3-3: Taller de buenas practicas de programacion

```
RUBRICA

Criterio                              Maximo   Obtenido
Ruff sin problemas                    2.0      1.0
Docstrings y README                   1.0      1.0
Estructura MVC                        1.0      1.0
Pruebas pytest                        1.0      1.0
Total                                 5.0      4.0

INTEGRANTES

Estudiante                                 Evidencia               Nota
Andres Felipe Muzu Yupangui (20242020021)  Propietario, commits    4.0
Diana Lisseth Franco Delgado (20251020035) Commits (luna0906LI)    4.0
```

## Observaciones

- Ruff reporta 1 error: I001 (imports sin ordenar) en tests/test_order.py. Se
  descuenta 1.0 en el criterio de Ruff. Se corrige con: ruff check --fix .
- Hay commits con autor "di" (git mal configurado).
- El README documenta correctamente la arquitectura MVC y los principios
  SOLID, y las 8 pruebas pasan.

## Accion requerida

Corregir el orden de imports (ruff check --fix .) y agregar los codigos
estudiantiles al README (solo estan los nombres). Se sugiere configurar
user.name y user.email en git.