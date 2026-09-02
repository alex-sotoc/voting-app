# Voting App - Sistema de Votacion en Tiempo Real
Sistema de votaciones en tiempo real con FastAPI y Flutter

## 1. Arquitectura y Tecnologias Utilizadas

El proyecto utiliza una arquitectura desacoplada basada en servicios Web:

* **Backend:** FastAPI (Python) para la construccion de la API REST asincrona y generacion de documentacion interactiva OpenAPI/Swagger.
* **Frontend:** Flutter (Dart) orientado a la ejecucion en dispositivos Android.
* **Base de Datos:** SQLite embebida para el almacenamiento persistente de candidatos y conteo de votos.

## 2. Requisitos del Sistema (User Stories)

* **US01:** Como usuario, quiero visualizar el listado de candidatos y sus votos actuales para conocer el estado de la eleccion.
* **US02:** Como usuario, quiero presionar un boton de votacion para registrar mi eleccion en tiempo real.
* **US03:** Como administrador, quiero disponer de una documentacion interactiva Swagger para validar los endpoints expuestos por la API.

## 3. Metodologia de Desarrollo

Se aplico una **Metodologia Agil** utilizando el marco de trabajo **Kanban**.

* **Tipo de Metodologia:** Agil (Kanban).
* **¿En que consiste?:** La metodologia Kanban se enfoca en la visualizacion continua del flujo de trabajo a traves de un tablero dividido en columnas (por hacer, en proceso, hecho). Permite gestionar las tareas mediante tarjetas (Issues) sin iteraciones de tiempo fijo (como los Sprints de Scrum), limitando el trabajo en curso (WIP) para evitar cuellos de botella y optimizar la entrega continua del software.

## 4. Herramientas CASE e Integracion

* **GitHub Projects:** Administracion y seguimiento del tablero Kanban del proyecto.
* **GitHub Issues:** Registro detallado de requerimientos, tareas de desarrollo y documentacion.
* **GitHub Desktop:** Gestion visual del control de versiones mediante commits referenciados a cada Issue (trazabilidad).

## 5. Guia de Ejecucion

### Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

cd frontend
flutter pub get
flutter run
