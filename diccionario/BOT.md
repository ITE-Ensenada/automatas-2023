# BOT ITE

Link: [Link a este design doc](#)

Author(s): Charlie L

Status: [Draft, Ready for review, In Review, Reviewed]

Ultima actualización: YYYY-MM-DD

## Contenido

Descripción
Este código proporciona una API simple para responder preguntas en español utilizando el modelo de lenguaje de spaCy. La aplicación Flask expone un endpoint '/pregunta' que acepta preguntas en formato JSON, realiza un análisis de similitud utilizando el modelo de spaCy y devuelve la respuesta más adecuada de un conjunto predefinido de respuestas.

Requisitos Previos
Tener instalada la biblioteca spaCy y el modelo de lenguaje en español (es_core_news_md).
Tener Flask instalado.
bash
Copy code
pip install spacy
python -m spacy download es_core_news_md
pip install Flask

Uso

1.- Ejecutar el Código:

Asegúrate de que las bibliotecas necesarias están instaladas.
Ejecuta el código en un entorno de Python.
bash
Copy code
python nombre_del_archivo.py

2.- Realizar Consultas:

Utiliza un cliente HTTP (como cURL, Postman, o cualquier otro) para realizar solicitudes POST al endpoint /pregunta.
Envía las preguntas en formato JSON con la clave "pregunta".
bash
Copy code
curl -X POST -H "Content-Type: application/json" -d '{"pregunta": "¿Dónde puedo consultar mi kardex?"}' http://localhost:5000/pregunta

3.- Obtener Respuestas:

Recibirás una respuesta en formato JSON que contiene la respuesta más cercana basada en la similitud semántica.
json
Copy code
{"respuesta": "¿Dónde puedo consultar mi kardex?"}

Notas Importantes

-Asegúrate de que la aplicación esté en ejecución antes de realizar solicitudes.
-La pregunta no puede estar vacía; asegúrate de proporcionar una pregunta válida en el cuerpo de -la solicitud JSON.
-Este código utiliza un conjunto predefinido de preguntas y respuestas; puedes personalizar el -diccionario respuestas según tus necesidades.

## Links

- [Un link](#)
- [Otro link](#)

## Objetivo

El objetivo de este código es proporcionar una API simple para responder preguntas en español utilizando el modelo de lenguaje de spaCy. La aplicación Flask expone un endpoint '/pregunta' que acepta preguntas en formato JSON, realiza un análisis de similitud utilizando el modelo de spaCy y devuelve la respuesta más adecuada de un conjunto predefinido de respuestas.

## Goals

Proporcionar Respuestas Automáticas: Crear un sistema que pueda interpretar preguntas en español y proporcionar respuestas automáticas basadas en la similitud semántica.

## Non-Goals

- Non-Goals

## Background

Este código utiliza el modelo de lenguaje en español de spaCy para comparar la similitud semántica entre la pregunta proporcionada por el usuario y un conjunto predefinido de preguntas y respuestas. La aplicación Flask expone un endpoint que acepta preguntas en formato JSON, realiza la comparación semántica y devuelve la respuesta más cercana.

## Overview

Proporcionar Respuestas Automáticas: Crear un sistema que pueda interpretar preguntas en español y proporcionar respuestas automáticas basadas en la similitud semántica.

## Detailed Design

El diseño del código se centra en la utilización de la biblioteca spaCy para procesar el lenguaje natural y determinar la similitud semántica. Aquí hay un resumen de cómo funciona:

Carga del Modelo: Se carga el modelo de lenguaje en español de spaCy (es_core_news_md).

Definición de Preguntas y Respuestas: Un conjunto predefinido de preguntas y respuestas se establece en el diccionario respuestas.

API Flask: Se utiliza Flask para crear una API web. La ruta '/pregunta' acepta solicitudes POST con preguntas en formato JSON.

Procesamiento de Preguntas: La pregunta del usuario se procesa con spaCy y se compara la similitud semántica con cada pregunta predefinida.

Selección de Respuesta: La respuesta con la mayor similitud se selecciona como la respuesta final.

Respuesta JSON: La respuesta se devuelve al usuario en formato JSON a través de la API.

## Solution 1

### Frontend

_Frontend…_

### Backend

_Backend…_

## Solution 2

### Frontend

_Frontend…_

### Backend

_Backend…_

## Consideraciones

_Preocupaciones / trade-offs / tech debt_

## Métricas

_Que información necesitas para validar antes de lanzar este feature?_
