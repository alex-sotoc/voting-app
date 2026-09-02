# Retrospectiva del Proyecto - Voting App

## 1. Que funciono bien
* La separacion entre el backend en FastAPI y el frontend en Flutter facilito el desarrollo modular y las pruebas independientes.
* La documentacion automatica en Swagger redujo el tiempo necesario para verificar el funcionamiento de las rutas HTTP.
* La vinculacion de cada commit con su respectivo Issue en GitHub Projects aseguro una trazabilidad clara del flujo de trabajo.

## 2. Que se complico o se puede mejorar
* La resolucion de la direccion IP local (`10.0.2.2`) para conectar la comunicacion de red entre el emulador de Android y la API local en FastAPI.
* Se identifica como mejora a futuro la implementacion de validacion de usuarios para restringir un voto por persona y el uso de graficos interactivos.

## 3. Lecciones aprendidas
* La utilidad de aplicar la metodologia Kanban para priorizar tareas y limitar el trabajo en proceso sin depender de ciclos estructurados.
* El impacto positivo de mantener la estructura del repositorio organizada por responsabilidades especificas (`backend`, `frontend`, `docs`).
