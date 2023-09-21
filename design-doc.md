# BOT DE TELEGRAM QUIZ DE POKEMON
Link: [Link a este design doc](#)

Author(s): Juan Carlos Salazar Silva

Status: [Draft, Ready for review, In Review, Reviewed]

Ultima actualización: 2023-09-12

## Contenido
- Objetivo
- Reglas del juego
- Características
- Diseño Detallado
- Frontend
- Backend
- Consideraciones
- Métricas

## Links
- [Un link](#)
- [Otro link](#)

## Objetivo
Crear un bot de Telegram que permita a los usuarios jugar un quiz de Pokémon, donde deben adivinar el nombre del Pokémon basado en una imagen y recibir retroalimentación sobre sus respuestas.

## Reglas del juego
El bot enviará una imagen de un Pokémon al usuario.
El usuario debe adivinar el nombre del Pokémon en un tiempo limitado.
El usuario puede proporcionar su respuesta en texto.
El bot verificará la respuesta del usuario y proporcionará retroalimentación.
El usuario acumulará puntos por respuestas correctas.
El usuario puede ver su puntuación actual en cualquier momento

## Características
Sistema de puntuación.
Temporizador para limitar el tiempo de respuesta.
Amplia base de datos de imágenes de Pokémon.
Retroalimentación inmediata después de cada respuesta.
Comandos de inicio y ayuda.

## Diseño Detallado
Frontend
El frontend del bot de Telegram consistirá en la interfaz de usuario que interactúa con los usuarios a través de mensajes de Telegram. Deberá proporcionar las siguientes funcionalidades:

Comando "/start" para iniciar el juego.
Comando "/help" para obtener instrucciones y reglas del juego.
Envío de imágenes de Pokémon a los usuarios.
Recepción de respuestas de los usuarios en forma de texto.
Backend
El backend del bot de Telegram se encargará de gestionar el juego, verificar respuestas, llevar un registro de la puntuación y enviar retroalimentación. Deberá proporcionar las siguientes funcionalidades:

Base de datos que almacena información sobre Pokémon, incluyendo imágenes y nombres.
Temporizador para limitar el tiempo de respuesta del usuario.
Lógica para verificar si las respuestas del usuario son correctas.
Sistema de puntuación que registra y actualiza la puntuación del usuario.
Generación de imágenes aleatorias de Pokémon para cada pregunta.
Envío de mensajes de retroalimentación al usuario después de cada respuesta.

## Consideraciones
Se requiere acceso a una base de datos de Pokémon con imágenes y nombres.
Se debe manejar la interacción con múltiples usuarios de forma simultánea.
Se debe garantizar que el bot sea fácil de usar y proporcione instrucciones claras.

## Métricas
Número de usuarios que inician el juego.
Número de usuarios que completan el juego.
Puntuación promedio de los usuarios.
Tiempo promedio de juego por usuario.
Retroalimentación de los usuarios sobre la experiencia de juego.
Este diseño proporciona una visión general de cómo se podría desarrollar un bot de Telegram para un juego de quiz de Pokémon. Los detalles específicos de la implementación pueden variar según las preferencias y recursos disponibles del desarrollador.

## Solucion 2
Podemos reusar los mismos métodos de la solución 1, con los siguientes cambios

### Aplicar el quiz con un bot de discord
En lugar de usar un bot de telegram se usaria uno de discord
Esto necesitaría otro design doc enfocado a la solucion 2, si se elige esta solución

## Consideraciones
- La librería solo esta en Python. Tal vez podemos entender como funciona para implementarla por nuestra cuenta en otro lenguaje si es necesario

## Métricas
- Checar Web Vitals para entender si la app carga de forma adecuada y tiene buen performance
- Validar cuantos usuarios terminan el proceso de migración de una playlist